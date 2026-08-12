
import streamlit as st

st.title("📊 Travel Analytics Dashboard")

st.write("""
The primary Travel Analytics dashboard is already implemented
inside the Flask application.
""")

st.markdown(
    "[🌐 Open Flask Dashboard](http://localhost:5000/dashboard)"
)

st.info(
    "This Streamlit page is only a presentation entry point. "
    "The production dashboard remains in Flask."
)