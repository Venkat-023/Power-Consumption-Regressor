from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import joblib
import pandas as pd

# -------------------------
# Load model & preprocessor
# -------------------------
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"

model = joblib.load(MODEL_DIR / "xgb_model.pkl")
preprocessor = joblib.load(MODEL_DIR / "scaler.pkl")

app = FastAPI(title="Power Consumption Prediction API")

# -------------------------
# Input schema (RAW values)
# -------------------------
class ModelInput(BaseModel):
    hour: int
    weekday: int
    month: int
    season: str              # "dry", "rainy", "harmattan"
    temperature: float
    is_rain_day: int          # 0 or 1
    holiday_type_national: int  # 0 or 1

# -------------------------
# Health check
# -------------------------
@app.get("/")
def health_check():
    return {"status": "API is running"}

# -------------------------
# Prediction endpoint
# -------------------------
@app.post("/predict")
@app.post("/predict")
def predict(data: ModelInput):

    season_dry = 1 if data.season == "dry" else 0
    season_rainy = 1 if data.season == "rainy" else 0
    season_harmattan = 1 if data.season == "harmattan" else 0

    df = pd.DataFrame([{
        "hour": data.hour,
        "weekday": data.weekday,
        "month": data.month,
        "season_dry": season_dry,
        "season_rainy": season_rainy,
        "season_harmattan": season_harmattan,
        "temperature": data.temperature,
        "is_rain_day": data.is_rain_day,
        "holiday_type_national": data.holiday_type_national
    }])

    # Force exact training order
    df = df[[
        "hour",
        "weekday",
        "month",
        "season_dry",
        "season_rainy",
        "season_harmattan",
        "temperature",
        "is_rain_day",
        "holiday_type_national"
    ]]

    X_processed = preprocessor.transform(df)
    prediction = model.predict(X_processed)[0]

    return {
        "predicted_load_kw": float(prediction)
    }