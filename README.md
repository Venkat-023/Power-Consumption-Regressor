📊 Power Consumption Regressor
Regression Model Comparison, Optimization & Full-Stack Deployment
📌 Overview

This project builds and evaluates multiple machine learning regression models to predict a continuous target variable (mean ≈ 82,539, std ≈ 27,243).

The objective was to identify the most accurate model using MAE and RMSE, optimize performance, and deploy the best model through a full-stack application using FastAPI (backend) and Streamlit (frontend).

The final solution delivers strong predictive accuracy with production-ready API integration.

🎯 Objective

Compare multiple regression models

Evaluate performance using MAE and RMSE

Optimize hyperparameters

Deploy the best-performing model

Integrate backend API with frontend interface

🧠 Models Evaluated

The following models were trained and tested on the same dataset:

Linear ensemble trees

Bagging-based models

Random Forest

Extra Trees

Boosting-based models

XGBoost (baseline)

Gradient Boosting

LightGBM

Hyperparameter-tuned boosting models (Optuna)

📈 Performance Results

Model	MAE	RMSE

XGBoost (baseline)	2236.70	3192.72

Gradient Boosting	2237.22	3192.55

LightGBM	2262.43	3229.74

XGBoost (Optuna-tuned)	—	3229.26

Random Forest	2353.55	3436.14

Extra Trees	2369.90	3405.14

🔍 Key Findings

✅ Boosting models outperformed bagging models

XGBoost, Gradient Boosting, and LightGBM consistently achieved lower error rates.

🏆 Best Overall Performance

Lowest MAE → XGBoost (2236.70)

Lowest RMSE → Gradient Boosting (3192.55)

Difference is negligible → effectively a tie

⚠️ Hyperparameter Tuning (Optuna)

Tuned XGBoost did not outperform the baseline.

Likely due to conservative parameter selection leading to slight underfitting.

📊 Error Interpretation

MAE ≈ 2.7% of target mean

RMSE ≈ 11.7% of target standard deviation

➡️ Indicates strong predictive accuracy relative to the scale of the dataset.

🏗️ Tech Stack
🔹 Machine Learning

Python

Scikit-learn

XGBoost

LightGBM

Optuna

Pandas

NumPy

🔹 Backend

FastAPI

REST API for model inference

🔹 Frontend

Streamlit

Interactive UI for user input & predictions

🖥️ System Architecture
User Input (Streamlit UI)
        ↓
FastAPI Backend (REST API)
        ↓
Trained XGBoost Model
        ↓
Prediction Output
        ↓
Displayed on Streamlit Interface

🚀 How to Run Locally

1️⃣ Clone the Repository

git clone https://github.com/Venkat-023/Power-Consumption-Regressor.git

cd Power-Consumption-Regressor

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run FastAPI Backend

uvicorn main:app --reload

Backend runs on:

http://127.0.0.1:8000

4️⃣ Run Streamlit Frontend

streamlit run app.py

Frontend runs on:

http://localhost:8501



🔬 Future Improvements

Ensemble XGBoost + Gradient Boosting

Residual analysis for extreme values

Target transformation (if skewed)

Constrained hyperparameter tuning

Feature engineering for performance ceiling improvement

📌 Final Recommendation

Primary Model: XGBoost (baseline)
Alternative: Gradient Boosting

Further gains are expected to come from better features or advanced ensembling rather than switching algorithms.

✅ Conclusion

This project successfully demonstrates:

Comparative model evaluation

Practical ML optimization

Performance interpretation

Full-stack deployment of ML models

API–Frontend integration

It highlights real-world ML workflow from experimentation to production-ready deployment.