import streamlit as st

st.title("📈 Model Performance")

st.subheader("Flight Price Regression")

st.write("""
The final flight-price model is Random Forest Regressor.

The model was selected after comparing:

• Linear Regression
• Decision Tree
• Random Forest
• Gradient Boosting
""")

st.metric("Final Model", "Random Forest Regressor")
st.metric("RMSE", "1.1411")
st.metric("R² Score", "0.999990")

st.markdown(
    "[📊 Open MLflow](http://127.0.0.1:5002)"
)
