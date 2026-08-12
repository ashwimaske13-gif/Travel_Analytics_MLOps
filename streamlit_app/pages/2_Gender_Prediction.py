import streamlit as st

st.title("👤 Gender Prediction")

st.write("""
The gender classification workflow is implemented in the existing
Flask application using the saved classification model and preprocessing artifacts.
""")

st.markdown(
    "[🌐 Open Flask Application](http://localhost:5000/gender)"
)
