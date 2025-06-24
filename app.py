import streamlit as st
import numpy as np
import pickle

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# App title
st.title("📘 Student Final Score Predictor")
st.markdown("Fill in the details below to get the predicted score:")

# User input
hours = st.slider("Hours Studied", 0, 10, 5)
attendance = st.slider("Attendance (%)", 50, 100, 75)
previous_score = st.number_input("Previous Exam Score", min_value=0, max_value=100, value=80)

# Predict
if st.button("Predict"):
    input_data = np.array([[hours, attendance, previous_score]])
    prediction = model.predict(input_data)[0]
    st.success(f"🎯 Predicted Final Score: {prediction:.2f}")
