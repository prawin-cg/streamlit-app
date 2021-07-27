import streamlit as st
import numpy as np
import pandas as pd
import pickle as pickle

st.title('Early Diabetes Prediction')

df=pd.read_csv('diabetes_data_upload.csv')
sampl=st.checkbox('Check Sample Data')

if sampl:
    st.write(df.head())
values=['--Select--','Yes','No']
st.write('Please enter the patient details below to get the prediction.')
age=int(st.text_input('Enter the age',0))
gender=st.selectbox('Select your Gender',['--Select--','Male','Female'])
st.write('Do you experience the following?')
Polyuria=st.selectbox('Polyuria?',values)
Polydipsia=st.selectbox('Polydipsia?',values)
sudden_weight_loss=st.selectbox('Sudden weight loss?',values)
weakness=st.selectbox('Weakness?',values)
Polyphagia=st.selectbox('Polyphagia?',values)
Genital_thrush=st.selectbox('Genital thrush?',values)
visual_blurring=st.selectbox('Visual blurring?',values)
Itching=st.selectbox('Itching?',values)
Irritability=st.selectbox('Irritability?',values)
delayed_healing=st.selectbox('Delayed healing?',values)
partial_paresis=st.selectbox('Partial paresis',values)
muscle_stiffness=st.selectbox('Muscle stiffness',values)
Alopecia=st.selectbox('Alopecia',values)
Obesity=st.selectbox('Obesity',values)

input_values=[gender,Polyuria,Polydipsia,sudden_weight_loss,weakness,Polyphagia,Genital_thrush,visual_blurring,
                Itching,Irritability,delayed_healing,partial_paresis,muscle_stiffness,Alopecia,Obesity]


model = pickle.load(open('GBoost_Diabetes.pkl','rb'))

if st.button('Get Prediction!'):
    data_check=[]
    if type(age) is int:
        data_check.append(True)
    else:
        data_check.append(False)
    for i in input_values:
        if i in ['Male','Female','Yes','No']:
            data_check.append(True)
        else:
            data_check.append(False)
        if False in data_check:
            message='Oops! Invalid Input Data.'
        else:
            input_data=[age]
            input_data.extend([1 if i in ['Yes','Male'] else 0 for i in input_values])
            prediction=model.predict(np.array([input_data]))[0]
            if prediction==1:
                message='The patient is predicted to have diabetes'
            else:
                message='The patient is not predicted to have diabetes'
    st.header(message)
