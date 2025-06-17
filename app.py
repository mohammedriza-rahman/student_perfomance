# ###importing the necessary libraries

# import streamlit as st
# import joblib
# import numpy as np


# ## loading the model

# model = joblib.load("student_performance_model.h5")

# def predict_marks(Hours_studied,previous_score,Extracurricular_activity,sleep_hours,sample_question_papers_solved):
#     input_data= np.array([[Hours_studied,previous_score,Extracurricular_activity,sleep_hours,sample_question_papers_solved]])
#     model_prediction = model.predict(input_data)
#     prediction= round(float(model_prediction),2)

#     ## ensuring that the max value is 100 and it doesnt exceed it
#     if prediction > 100:
#         prediction = 100
#     return prediction


# ## creating the app

# def main():

#     st.title("Student Performance Predictor")


#     name = st.text_input("Enter Your Name :")

#     current_class =st.text_input("Enter Your Class :")

#     ## features input data

#     Hours_studied = st.number_input("Hours studied",min_value=0.0,max_value=10.0,value=0.0)
#     previous_score = st.number_input("Previous Score",min_value=0.0,max_value=100.0,value=0.0)
#     Extracurricular_activity = st.number_input("Extracurricular Activity",min_value=0.0,max_value=10.0,value=0.0)
#     sleep_hours = st.number_input("Sleep Hours",min_value=0.0,max_value=10.0,value=0.0)
#     sample_question_papers_solved = st.number_input("Sample Question Papers Solved",min_value=0.0,max_value=20.0,value=0.0)

#     ##sidebar

#     st.sidebar.title(f"hello..!, welcome {name} of class {current_class}.for your perfomance prediction.")




#     if st.button("Predict"):
#         marks = predict_marks(Hours_studied,previous_score,Extracurricular_activity,sleep_hours,sample_question_papers_solved)

#         ## display of the prediction

#         if marks > 90:
#             st.balloons()
#             st.success(f"Congrats {name}! You are performing excellently with a score of {marks}.")
#         elif marks >35:
#             st.warning(f"{name}! You are performing well with a score of {marks}.")
#         else:
#             st.error(f"{name}! You are performing poorly with a score of {marks}.")


# if __name__ == "__main__":
#     main()

import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("student_performance_model.h5")

# Prediction function
def predict_marks(Hours_studied, previous_score, Extracurricular_activity, sleep_hours, sample_question_papers_solved):
    input_data = np.array([[Hours_studied, previous_score, Extracurricular_activity, sleep_hours, sample_question_papers_solved]])
    model_prediction = model.predict(input_data)
    prediction = round(float(model_prediction), 2)
    return min(prediction, 100)

# Custom CSS for styling
custom_css = """
<style>
body {
    background-color: #f0f6ff;
}
.stApp {
    background: linear-gradient(to right, #e0f7fa, #e8eaf6);
    font-family: 'Segoe UI', sans-serif;
}
h1 {
    color: #2c3e50;
    text-align: center;
}
input, .stNumberInput > div > div {
    background-color: #ffffff !important;
    border: 1px solid #ccc !important;
    padding: 8px;
    border-radius: 10px;
}
.sidebar .sidebar-content {
    background-color: #d1c4e9;
    padding: 20px;
    border-radius: 12px;
}
div.stButton > button {
    background-color: #4caf50;
    color: white;
    font-weight: bold;
    border-radius: 10px;
    padding: 0.75em 1.5em;
}
div.stButton > button:hover {
    background-color: #388e3c;
}
.st-success, .st-warning, .st-error {
    font-size: 1.2rem;
    padding: 10px;
    border-radius: 8px;
}
</style>
"""

# Main Streamlit app
def main():
    st.markdown(custom_css, unsafe_allow_html=True)

    st.title("🎓 Student Performance Predictor")

    # Sidebar greeting
    st.sidebar.title("🎉 Welcome!")
    name = st.sidebar.text_input("Enter Your Name:")
    current_class = st.sidebar.text_input("Enter Your Class:")
    if name and current_class:
        st.sidebar.info(f"Hello {name} from class {current_class}! 👋")

    # Input Section
    st.markdown("### 📊 Enter Your Academic Details")

    col1, col2 = st.columns(2)
    with col1:
        Hours_studied = st.number_input("📚 Hours Studied", min_value=0.0, max_value=10.0, value=0.0)
        previous_score = st.number_input("📈 Previous Score (%)", min_value=0.0, max_value=100.0, value=0.0)
        Extracurricular_activity = st.number_input("🎨 Extracurricular Activities (0-10)", min_value=0.0, max_value=10.0, value=0.0)

    with col2:
        sleep_hours = st.number_input("😴 Sleep Hours", min_value=0.0, max_value=10.0, value=0.0)
        sample_question_papers_solved = st.number_input("📄 Sample Papers Solved", min_value=0.0, max_value=20.0, value=0.0)

    # Prediction button
    if st.button("🔮 Predict My Score"):
        marks = predict_marks(Hours_studied, previous_score, Extracurricular_activity, sleep_hours, sample_question_papers_solved)

        # Display result
        if marks > 90:
            st.balloons()
            st.success(f"🎉 Congrats {name}! You're doing excellently with a predicted score of **{marks}%**! Keep it up! 💪")
        elif marks > 35:
            st.warning(f"😊 Good job {name}, your predicted score is **{marks}%**. There's room for improvement, stay focused! 🎯")
        else:
            st.error(f"⚠️ {name}, your predicted score is **{marks}%**. Let’s work harder and improve your performance! 🚀")

if __name__ == "__main__":
    main()

