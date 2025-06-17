###importing the necessary libraries

import streamlit as st
import joblib
import numpy as np


## loading the model

model = joblib.load("student_performance_model.h5")

def predict_marks(Hours_studied,previous_score,Extracurricular_activity,sleep_hours,sample_question_papers_solved):
    input_data= np.array([[Hours_studied,previous_score,Extracurricular_activity,sleep_hours,sample_question_papers_solved]])
    model_prediction = model.predict(input_data)
    prediction= round(float(model_prediction),2)

    ## ensuring that the max value is 100 and it doesnt exceed it
    if prediction > 100:
        prediction = 100
    return prediction


## creating the app

def main():

    st.title("Student Performance Predictor")


    name = st.text_input("Enter Your Name :")

    current_class =st.text_input("Enter Your Class :")

    ## features input data

    Hours_studied = st.number_input("Hours studied",min_value=0.0,max_value=10.0,value=0.0)
    previous_score = st.number_input("Previous Score",min_value=0.0,max_value=100.0,value=0.0)
    Extracurricular_activity = st.number_input("Extracurricular Activity",min_value=0.0,max_value=10.0,value=0.0)
    sleep_hours = st.number_input("Sleep Hours",min_value=0.0,max_value=10.0,value=0.0)
    sample_question_papers_solved = st.number_input("Sample Question Papers Solved",min_value=0.0,max_value=20.0,value=0.0)

    ##sidebar

    st.sidebar.title(f"hello..!, welcome {name} of class {current_class}.for your perfomance prediction.")




    if st.button("Predict"):
        marks = predict_marks(Hours_studied,previous_score,Extracurricular_activity,sleep_hours,sample_question_papers_solved)

        ## display of the prediction

        if marks > 90:
            st.baloons()
            st.success(f"Congrats {name}! You are performing excellently with a score of {marks}.")
        elif marks >35:
            st.warning(f"{name}! You are performing well with a score of {marks}.")
        else:
            st.error(f"{name}! You are performing poorly with a score of {marks}.")


if __name__ == "__main__":
    main()
