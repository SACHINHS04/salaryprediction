# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 00:46:48 2021

@author: sachin h s
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_salary(YearsExperience,interview_score):
    
    """Let's predict salary 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: YearsExperience
        in: query
        type: number
        required: true
      - name: interview_score
        in: query
        type: number
        required: true

    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[YearsExperience,interview_score]])
    print(prediction)
    return prediction



def main():
    st.title("LET'S PREDICT YOUR SALARY")
    html_temp = """
    <div style="background-color:ForestGreen;padding:10px">
    <h2 style="color:white;text-align:center;">SALARY PREDICTION ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    my_range=range(1,11)
    YearsExperience = st.select_slider("YearsExperience",options=my_range)
    my_range_=range(1,10)
    interview_score = st.select_slider("interview_score",options=my_range_)
    result=""
    if st.button("Predict"):
        result=predict_salary(YearsExperience,interview_score)
    st.success('the predicted salary {}'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
