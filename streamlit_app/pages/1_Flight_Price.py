import streamlit as st

st.title("✈️ Flight Price Prediction")

st.write("""
The flight price prediction model is implemented in the existing
Travel Analytics production pipeline.

Production flow:

Notebook experimentation
→ Feature Engineering
→ Random Forest Model
→ Flask REST API
→ Docker
→ Kubernetes
""")

st.success("Final production model: Random Forest Regressor")

st.markdown(
    "[🔌 Open Flight Price REST API](http://localhost:5001/api/health)"
)

st.info(
    "Use the existing Flask application for the complete flight "
    "prediction interface."
)