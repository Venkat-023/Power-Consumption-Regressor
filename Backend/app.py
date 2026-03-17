import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from typing import Literal
import joblib
import pandas as pd
from xgboost import XGBRegressor

# -------------------------
# Paths
# -------------------------
BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "model"

# -------------------------
# FastAPI app
# -------------------------
app = FastAPI(title="Power Consumption Prediction API")

model = None
preprocessor = None


# -------------------------
# Load model on startup
# -------------------------
@app.on_event("startup")
def load_model():
    global model, preprocessor

    model = XGBRegressor()
    model.load_model(MODEL_DIR / "model2.json")

    preprocessor = joblib.load(MODEL_DIR / "scaler2.pkl")


# -------------------------
# Input schema
# -------------------------
class ModelInput(BaseModel):
    hour: int
    weekday: int
    month: int
    season: Literal["dry", "rainy", "harmattan"]
    temperature: float
    is_rain_day: int
    holiday_type_national: int


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