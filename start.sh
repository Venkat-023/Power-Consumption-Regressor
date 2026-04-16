#!/bin/sh
set -eu

uvicorn Backend.app:app --host 0.0.0.0 --port 8000 &

exec streamlit run Frontend/app.py --server.address=0.0.0.0 --server.port="${PORT:-7860}"
