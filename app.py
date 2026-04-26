import streamlit as st                           # importing the necessary packages
import joblib
import numpy as np

model = joblib.load()
st.title("student marks prediction")

courses=st.number_input("no of courses you choosen to study____Enter here:")
hours=st.number_input("how many hours take to study____Enter here:")


 
