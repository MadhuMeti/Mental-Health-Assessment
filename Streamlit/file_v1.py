import streamlit as st
import pickle

# Load the saved SVC model
with open("a_svc_model.pkl", "rb") as f:
    svc_model = pickle.load(f)

# Define questions and their options
questions = {
    "I was aware of dryness of my mouth.": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time", "Applied to me very much or most of the time"],
    "I experienced breathing difficulty (e.g. excessively rapid breathing, breathlessness in the absence of physical exertion).": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time", "Applied to me very much or most of the time"],
    "I experienced trembling (e.g. in the hands).": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time", "Applied to me very much or most of the time"],
    "I was worried about situations in which I might panic and make a fool of myself.": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time", "Applied to me very much or most of the time"],
    "I felt I was close to panic.": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time", "Applied to me very much or most of the time"],
    "I was aware of the action of my heart in the absence of physical exertion (e.g. sense of heart rate increase, heart missing a beat).": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time", "Applied to me very much or most of the time"],
    "I felt scared without any good reason.": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time", "Applied to me very much or most of the time"]
}

# Define a mapping of gender to numeric values
gender_to_numeric = {"Female": 0, "Male": 1}

# Build the Streamlit app
st.title("Mental Health Prediction")
st.write("A step towards mental wellness.")

# Get age from user
age = st.number_input("Enter your age:", min_value=16, max_value=25, step=1)

# Get gender from user
gender = st.radio("Select your gender:", ("Male", "Female"))

# Convert gender to numeric value
gender_numeric = gender_to_numeric[gender]

# Get user input for the questionnaire
user_input = []
for question, options in questions.items():
    selected_option = st.selectbox(f"{question}:", options)
    numeric_value = options.index(selected_option)
    user_input.append(numeric_value)

# Append age and gender to the user input
user_input = [age, gender_numeric] + user_input

# Make prediction using the loaded model
prediction = svc_model.predict([user_input])[0]

# Display the prediction results
if st.button("Make Prediction"):
    st.write(f"Score: {prediction}")
