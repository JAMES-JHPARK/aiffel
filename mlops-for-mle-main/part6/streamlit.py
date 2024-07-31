import streamlit as st
import requests
import json
import re

st.title("MLOps Day4 - FastAPI")
st.subheader("Iris Prediction")

sepal_length = st.text_area("sepal_length :")
sepal_width = st.text_area("sepal_width :")
petal_length = st.text_area("petal_length :")
petal_width = st.text_area("petal_width :")

info_dict = {
  "sepal_length": sepal_length,
    "sepal_width": sepal_width,
      "petal_length": petal_length,
        "petal_width": petal_width
        }

if st.button("Predict"):
    result = requests.post(
        url = "http://127.0.0.1:8000/predict",
        data = json.dumps(info_dict),
        verify=False
        )
    
    res = re.search(r'\d+', result.text).group(0)

    if res == '0':
      prediction = 'setosa'
    elif res == '1':
       prediction = 'versicolor'
    elif res == '2':
       prediction = 'virginica'

    st.subheader(f"Result: {prediction}")
