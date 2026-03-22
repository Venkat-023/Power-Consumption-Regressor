import streamlit as st
import requests
import plotly.graph_objects as go
from datetime import datetime

API_URL =  "http://localhost:8000/predict"

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="GridSense AI",
    page_icon="⚡",
    layout="wide"
)

# -------------------------------------------------
# Neon AI + Renewable Energy Styling
# -------------------------------------------------
st.markdown("""
<style>

/* === FULL BACKGROUND === */
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(circle at 20% 20%, rgba(14,165,233,0.35), transparent 40%),
        radial-gradient(circle at 80% 30%, rgba(34,197,94,0.35), transparent 40%),
        linear-gradient(135deg, #0f172a 0%, #111827 100%);
}

/* Remove white header */
[data-testid="stHeader"] {
    background: transparent;
}

/* Container spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* === HERO TITLE === */
.center-title {
    text-align: center;
    font-size: 64px;
    font-weight: 900;
    color: #ffffff;
    text-shadow: 0 0 25px #0ea5e9;
}

.center-subtitle {
    text-align: center;
    font-size: 22px;
    color: #cbd5e1;
    margin-bottom: 35px;
}

/* === GLASS PANELS === */
.section {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(20px);
    padding: 30px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0 0 40px rgba(34,197,94,0.25);
    color: white;
}

/* Make labels readable */
label {
    color: #e2e8f0 !important;
}

/* Subheaders */
h3 {
    color: #f1f5f9 !important;
}

/* === NEON BUTTON === */
.stButton > button {
    background: linear-gradient(90deg, #0ea5e9, #22c55e);
    color: white;
    font-weight: 700;
    border-radius: 16px;
    height: 3.2em;
    border: none;
    transition: all 0.3s ease;
    box-shadow: 0 0 25px rgba(34,197,94,0.7);
}

.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 0 45px rgba(14,165,233,0.9);
}

/* Metric styling */
[data-testid="stMetricValue"] {
    color: #22c55e;
    font-weight: 800;
    font-size: 28px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Hero Section
# -------------------------------------------------
st.markdown('<div class="center-title">⚡ GridSense AI</div>', unsafe_allow_html=True)
st.markdown('<div class="center-subtitle">Renewable Energy Load Intelligence Platform</div>', unsafe_allow_html=True)

st.divider()

# -------------------------------------------------
# Layout
# -------------------------------------------------
left, right = st.columns([1, 1.2])

# -------------------------------------------------
# Input Panel
# -------------------------------------------------
with left:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("⚙️ Input Parameters")

    hour = st.slider("Hour of Day", 0, 23, 12)
    weekday = st.selectbox("Weekday (0=Mon, 6=Sun)", list(range(7)))
    month = st.selectbox("Month", list(range(1, 13)))
    season = st.selectbox("Season", ["dry", "rainy", "harmattan"])
    temperature = st.number_input("Temperature (°C)", value=30.0)
    is_rain_day = st.toggle("Rain Day")
    holiday = st.toggle("National Holiday")

    st.markdown(" ")
    predict_btn = st.button("⚡ Run Energy Forecast", width="stretch")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# System Overview
# -------------------------------------------------
with right:
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("🧠 System Intelligence")

    st.write(f"""
    **Model:** XGBoost Regressor  
    **Preprocessing:** One-Hot Encoding + Standard Scaling  
    **Prediction Target:** Electricity Load (kW)  
    **System Timestamp:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# Prediction Section
# -------------------------------------------------
# -------------------------------------------------
# Prediction Section
# -------------------------------------------------
if predict_btn:

    payload = {
        "hour": hour,
        "weekday": weekday,
        "month": month,
        "season": season,
        "temperature": temperature,
        "is_rain_day": int(is_rain_day),
        "holiday_type_national": int(holiday)
    }

    try:
        with st.spinner("🔎 Analyzing renewable energy demand patterns..."):
            response = requests.post(API_URL, json=payload, timeout=10)

        if response.status_code != 200:
            st.error(f"Backend returned error {response.status_code}")
            st.write(response.text)
            st.stop()

        prediction = response.json()["predicted_load_kw"]

        st.divider()
        st.subheader("📊 Forecast Results")

        m1, m2, m3 = st.columns(3)
        m1.metric("Predicted Load (kW)", f"{prediction:,.2f}")
        m2.metric("Temperature (°C)", temperature)
        m3.metric("Operational Hour", hour)

        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=prediction,
            title={'text': "Forecasted Electricity Load (kW)"},
            gauge={
                'axis': {'range': [0, max(100, prediction * 1.2)]},
                'bar': {'color': "#22c55e"},
            }
        ))

        st.plotly_chart(fig, width="stretch")

    except requests.exceptions.ConnectionError:
        st.error("🚫 Backend API is not reachable from Streamlit container.")

    except requests.exceptions.Timeout:
        st.error("⏱ Backend request timed out.")

    except Exception as e:
        st.error(f"⚠️ Request failed: {e}")