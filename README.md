⚡ Power Consumption Regressor
Regression Model Comparison, Optimization & Full-Stack Deployment
📌 Overview

This project focuses on building and evaluating multiple machine learning regression models to predict power consumption (continuous target variable with mean ≈ 82,539 and std ≈ 27,243).

The workflow covers:

Model comparison

Performance evaluation (MAE, RMSE)

Hyperparameter optimization

Full-stack deployment

Containerization using Docker

Cloud deployment on AWS EC2

The final solution delivers high predictive accuracy and is deployed as a production-ready ML application.


Compare multiple regression algorithms

Evaluate using MAE and RMSE

Optimize models with hyperparameter tuning

Deploy best-performing 

Build full-stack ML system (API + UI)

Containerize using Docker

Deploy on AWS EC2

🧠 Models Evaluated

The following models were trained on the same dataset:

🔹 Bagging-Based Models

Random Forest

Extra Trees

🔹 Boosting-Based Models

XGBoost (baseline)

Gradient Boosting

LightGBM

XGBoost (Optuna-tuned)

📈 Performance Results

Model	        MAE	        RMSE

XGBoost (baseline)	2236.70	        3192.72

Gradient Boosting	2237.22	        3192.55

LightGBM	        2262.43	        3229.74

XGBoost (Optuna-tuned)	 —	        3229.26

Random Forest	        2353.55	        3436.14

Extra Trees	        2369.90	        3405.14

🔍 Key Findings

✅ Boosting > Bagging

Boosting models consistently outperform bagging models.

🏆 Best Models

Lowest MAE → XGBoost

Lowest RMSE → Gradient Boosting

➡️ Difference is negligible → effectively a tie

⚠️ Hyperparameter Tuning

Optuna-tuned XGBoost underperformed baseline

Likely due to conservative search space → slight underfitting

📊 Error Interpretation

MAE ≈ 2.7% of mean target

RMSE ≈ 11.7% of standard deviation


➡️ Indicates strong predictive performance relative to dataset scale

🏗️ Tech Stack

🔹 Machine Learning

Python

Scikit-learn

XGBoost

LightGBM

Optuna

Pandas, NumPy

🔹 Backend

FastAPI
REST API for inference
🔹 Frontend
Streamlit

Interactive UI for predictions

🔹 DevOps & Deployment

Docker

AWS EC2

Uvicorn

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

🐳 Docker Setup

1️⃣ Build Docker Image

docker build -t power-regressor .

2️⃣ Run Container

docker run -p 8000:8000 -p 8501:8501 power-regressor

☁️ AWS EC2 Deployment

Steps Followed:

Launched EC2 instance (Ubuntu)

Installed Docker:

sudo apt update

sudo apt install docker.io -y

Pulled project & built image:

git clone https://github.com/Venkat-023/Power-Consumption-Regressor.git

cd Power-Consumption-Regressor

docker build -t power-regressor .

Ran container:

docker run -d -p 8000:8000 -p 8501:8501 power-regressor

Accessed application via:

Backend API: http://<EC2-IP>:8000

Frontend UI: http://<EC2-IP>:8501

🚀 Run Locally (Without Docker)

1️⃣ Clone Repository

git clone https://github.com/Venkat-023/Power-Consumption-Regressor.git

cd Power-Consumption-Regressor

2️⃣ Install Dependencies

pip install -r requirements.txt

3️⃣ Run Backend

uvicorn main:app --reload

4️⃣ Run Frontend
streamlit run app.py

🔬 Future Improvements

Ensemble: XGBoost + Gradient Boosting

Residual error analysis (especially outliers)

Target transformation (for skewness)

Better hyperparameter search space

Advanced feature engineering

📌 Final Recommendation

Primary Model: XGBoost (baseline)

Alternative: Gradient Boosting

➡️ Future gains are more likely from:

Feature engineering

Model ensembling

rather than switching algorithms

✅ Conclusion

This project demonstrates:

End-to-end ML workflow

Model comparison & evaluation

Practical optimization

Full-stack deployment

Docker containerization

Cloud deployment on AWS

➡️ A complete pipeline from experimentation → production-ready system