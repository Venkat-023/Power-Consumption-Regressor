# Power Consumption Regressor

Regression model comparison, optimization, and full-stack deployment for electricity load forecasting.

## Live Demo

- Hugging Face Space: [Venkat-023/Power-Consumption-Regressor](https://huggingface.co/spaces/Venkat-023/Power-Consumption-Regressor)

## Overview

This project predicts power consumption using a supervised regression pipeline and serves predictions through a FastAPI backend with a Streamlit frontend. The repo includes the trained XGBoost model, preprocessing pipeline, Docker assets, and deployment-ready configuration for Hugging Face Spaces.

## Features

- Compares multiple regression approaches for power consumption forecasting
- Serves predictions through a FastAPI inference API
- Provides an interactive Streamlit UI for manual predictions
- Includes Docker setup for both local multi-container runs and Hugging Face Spaces

## Models Evaluated

- Random Forest
- Extra Trees
- XGBoost
- Gradient Boosting
- LightGBM
- Optuna-tuned XGBoost

## Reported Results

| Model | MAE | RMSE |
| --- | ---: | ---: |
| XGBoost (baseline) | 2236.70 | 3192.72 |
| Gradient Boosting | 2237.22 | 3192.55 |
| LightGBM | 2262.43 | 3229.74 |
| XGBoost (Optuna-tuned) | - | 3229.26 |
| Random Forest | 2353.55 | 3436.14 |
| Extra Trees | 2369.90 | 3405.14 |

## Project Structure

```text
.
|-- Backend/
|   |-- app.py
|   |-- Dockerfile
|   `-- model/
|-- Frontend/
|   |-- app.py
|   `-- Dockerfile
|-- Dockerfile
|-- docker-compose.yml
`-- start.sh
```

## Local Development

### Run with Docker Compose

```bash
docker compose up --build
```

Services:

- Frontend: `http://localhost:8501`
- Backend: `http://localhost:8000`

### Run as a Single Container

This matches the Hugging Face Space deployment model.

```bash
docker build -t power-consumption-regressor .
docker run -p 7860:7860 power-consumption-regressor
```

App URL:

- Streamlit UI: `http://localhost:7860`

### Run Without Docker

Backend:

```bash
cd Backend
pip install -r requirements.txt
uvicorn app:app --reload
```

Frontend:

```bash
cd Frontend
pip install -r requirements.txt
streamlit run app.py
```

## Hugging Face Spaces Deployment

This repository now includes a root `Dockerfile` that is compatible with Hugging Face Docker Spaces.

- Space URL: [https://huggingface.co/spaces/Venkat-023/Power-Consumption-Regressor](https://huggingface.co/spaces/Venkat-023/Power-Consumption-Regressor)
- Exposed app port: `7860`
- Startup flow: FastAPI runs internally on `8000`, Streamlit is exposed publicly on `7860`

To deploy updates to the Space, push this repository contents to the Space repository or connect the Space to this GitHub repository if you want automatic rebuilds.

## Tech Stack

- Python
- FastAPI
- Streamlit
- XGBoost
- scikit-learn
- pandas
- Docker
- Hugging Face Spaces

## Recommendation

- Primary model: XGBoost baseline
- Strong alternative: Gradient Boosting

Most future gains are likely to come from feature engineering, model ensembling, and deeper error analysis rather than switching algorithms alone.
