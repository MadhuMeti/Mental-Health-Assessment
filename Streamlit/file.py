import streamlit as st
import pickle

# Load the saved SVC models for each questionnaire page
with open("a_svc_model.pkl", "rb") as f:
    svc_model_anxiety = pickle.load(f)

with open("d_svc_model.pkl", "rb") as f:
    svc_model_depression = pickle.load(f)

# Define questions for each questionnaire page
questions_anxiety = {
    "I was aware of dryness of my mouth": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I experienced breathing difficulty (e.g. excessively rapid breathing, breathlessness in the absence of physical exertion)": ["Did not apply to me at all", "Option 2", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I experienced trembling (e.g. in the hands)": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I was worried about situations in which I might panic and make a fool of myself": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt I was close to panic": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I was aware of the action of my heart in the absence of physical exertion (e.g. sense of heart rate increase, heart missing a beat)": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt scared without any good reason": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"]
}

questions_depression = {
    "I couldn’t seem to experience any positive feeling at all": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I found it difficult to work up the initiative to do things": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt that I had nothing to look forward to": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt down-hearted and blue": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I was unable to become enthusiastic about anything": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt I wasn’t worth much as a person": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I felt that life was meaningless": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"]
}

# Define a mapping of gender to numeric values
gender_to_numeric = {"Female": 0, "Male": 1}

# Function to calculate prediction
def calculate_prediction(age, gender, user_input, model):
    user_input = [age, gender] + user_input
    prediction = model.predict([user_input])[0]
    return prediction

# Home page
def home_page():
    st.title("Mental Health Prediction")
    st.image("images.jpeg", caption="Image Source: Unsplash", use_column_width=True)
    st.write("""
        Welcome to our Mental Health Prediction tool! This tool is designed to help you assess your anxiety and depression levels.
        Click on the buttons below to start predicting!
    """)
    st.markdown("---")
    st.write("## Get Started")
    st.write("Choose one of the following options to predict your mental health:")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Predict Anxiety"):
            st.experimental_set_query_params(page="Anxiety Prediction")
    with col2:
        if st.button("Predict Depression"):
            st.experimental_set_query_params(page="Depression Prediction")

# Questionnaire page 1 (Anxiety)
def questionnaire_page_anxiety():
    st.title("Anxiety Level Prediction")
    st.write("Please answer the questions below.")

    # Get age from user
    age = st.number_input("Enter your age:", min_value=16, max_value=25, step=1)

    # Get gender from user
    gender = st.radio("Select your gender:", ("Male", "Female"))
    gender_numeric = gender_to_numeric[gender]

    # Get user input for the questionnaire
    user_input = []
    for question, options in questions_anxiety.items():
        selected_option = st.selectbox(f"{question}:", options)
        numeric_value = options.index(selected_option)
        user_input.append(numeric_value)

    # Make prediction using the loaded model for anxiety
    if st.button("Make Prediction for Anxiety"):
        prediction = calculate_prediction(age, gender_numeric, user_input, svc_model_anxiety)
        st.success(f"Your anxiety score is: {prediction}")

# Questionnaire page 2 (Depression)
def questionnaire_page_depression():
    st.title("Depression Level Prediction")
    st.write("Please answer the questions below.")

    # Get age from user
    age = st.number_input("Enter your age:", min_value=16, max_value=25, step=1)

    # Get gender from user
    gender = st.radio("Select your gender:", ("Male", "Female"))
    gender_numeric = gender_to_numeric[gender]

    # Get user input for the questionnaire
    user_input = []
    for question, options in questions_depression.items():
        selected_option = st.selectbox(f"{question}:", options)
        numeric_value = options.index(selected_option)
        user_input.append(numeric_value)

    # Make prediction using the loaded model for depression
    if st.button("Make Prediction for Depression"):
        prediction = calculate_prediction(age, gender_numeric, user_input, svc_model_depression)
        st.success(f"Your depression score is: {prediction}")

# Main function
def main():
    st.sidebar.title("Navigation")
    page = st.experimental_get_query_params().get("page", "Home")

    if page == "Home":
        home_page()
    elif page == "Anxiety Prediction":
        questionnaire_page_anxiety()
    elif page == "Depression Prediction":
        questionnaire_page_depression()

# Execute the main function
if __name__ == "__main__":
    main()
