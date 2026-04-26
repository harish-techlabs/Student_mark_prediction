import streamlit as st                           # importing the necessary packages
import joblib
import numpy as np

model = joblib.load("linear_model.pkl")                       # loading the model
st.title("student marks prediction")

st.write("Enter the following details to predict the marks of the student")

number_of_courses = st.number_input("Enter the number of courses are enrolled in:",min_value=0,max_value=100,step=1)       # taking input from the user
study_hours = st.number_input("Enter the number of hours to study : ",min_value=0,max_value=100,step=1) 

if st.button("Predict"):
   input_data = np.array([[study_hours, number_of_courses]])
   prediction = model.predict(input_data)
   st.write(f"The predicted marks of the student is: {prediction[0]}")