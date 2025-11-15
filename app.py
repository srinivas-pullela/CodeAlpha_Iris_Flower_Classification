import streamlit as st
import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load("iris_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🌸 Iris Flower Classification App")
st.write("Enter flower measurements to get predicted species.")

# Input fields
sepal_length = st.number_input("Sepal Length (cm)", 0.0, 10.0)
sepal_width = st.number_input("Sepal Width (cm)", 0.0, 10.0)
petal_length = st.number_input("Petal Length (cm)", 0.0, 10.0)
petal_width = st.number_input("Petal Width (cm)", 0.0, 10.0)

if st.button("Predict"):
    # Create array from input
    data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

    # Scale input
    data_scaled = scaler.transform(data)

    # Prediction
    prediction = model.predict(data_scaled)[0]

    st.success(f"Predicted flower species: **{prediction}**")
