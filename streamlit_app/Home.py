import streamlit as st

st.set_page_config(
    page_title="Travel Analytics MLOps",
    page_icon="✈️",
    layout="wide",
)

st.title("✈️ Travel Analytics MLOps")
st.subheader("Machine Learning + MLOps Travel Analytics Platform")

st.write(
    "Streamlit is used as the interactive presentation layer. "
    "The actual ML, Flask, REST API, Docker and Kubernetes logic "
    "remains in the existing project."
)

st.divider()

st.subheader("Open Existing Services")

st.markdown(
    "[🌐 Open Flask Application](http://localhost:5000)"
)

st.markdown(
    "[🔌 Open REST API](http://localhost:5001)"
)

st.markdown(
    "[📊 Open MLflow](http://127.0.0.1:5002)"
)

st.divider()

st.info(
    "Make sure the Flask application, REST API and MLflow server "
    "are running before opening these links."
)