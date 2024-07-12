import streamlit as st
import pickle

page_bg="""
<style>
[data-testid='stAppViewContainer']{
background-image: url("https://img.freepik.com/free-photo/still-life-sustainability-concept-arrangement_23-2148996992.jpg?w=2000&t=st=1712302813~exp=1712303413~hmac=877d5b945f8fe728271de92c5f2a7d850374a34607862f96753c7da0aea25a60");
background-size:cover;
}
</style>
"""

# Load the saved SVC models for each questionnaire page
with open("a_svc_model.pkl", "rb") as f:
    svc_model_anxiety = pickle.load(f)

with open("d_svc_model.pkl", "rb") as f:
    svc_model_depression = pickle.load(f)

# Define questions for each questionnaire page
questions_anxiety = {
    "I was aware of dryness of my mouth": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
    "I experienced breathing difficulty (e.g. excessively rapid breathing, breathlessness in the absence of physical exertion)": ["Did not apply to me at all", "Applied to me to some degree, or some of the time", "Applied to me to a considerable degree or a good part of time","Applied to me very much or most of the time"],
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
    st.write("A step towards mental wellness.")
    st.write("Illuminate Your Path to Wellness. Let our questionnaire be your guiding light, illuminating the way towards mental clarity and inner harmony. Incorporating mental health assessments into platforms for young people is essential, as it allows for early detection of issues, encourages self-care practices, and facilitates access to support systems, enabling them to navigate life's ups and downs with resilience and well-being.")

# Questionnaire page 1 (Anxiety)
def questionnaire_page_anxiety():
    st.title("Anxiety Level Prediction")
    st.write("Please answer the questions below.")

    # Get age from user
    a_age = st.number_input("Enter your age:", min_value=16, max_value=25, step=1)

    # Get gender from user
    gender = st.radio("Select your gender:", ("Male", "Female"))
    a_gender_numeric = gender_to_numeric[gender]

    # Get user input for the questionnaire
    user_input = []
    for question, options in questions_anxiety.items():
        selected_option = st.selectbox(f"{question}:", options)
        numeric_value = options.index(selected_option)
        user_input.append(numeric_value)

    # Make prediction using the loaded model for anxiety
    if st.button("Make Prediction for Anxiety"):
        a_prediction = calculate_prediction(a_age, a_gender_numeric, user_input, svc_model_anxiety)
        st.write(f"Your Anxiety Score: {a_prediction}")
        st.subheader("Recommendations:")
        if a_prediction in range(0,8):
            st.write("* You are normal!")
            st.write("* Continue with your practices.")
        elif a_prediction in range(8,10):
            st.write("* Get enough sleep.")
            st.write("* Maintain a healthy diet. Include dark chocolate and green tea.")
            st.write("* Try to be physically active.")
        elif a_prediction in range(10,15):
            st.write("* Avoid alcohol and recreational drugs.")
            st.write("* Avoid smoking.")
            st.write("* Try out relaxation techniques like meditation and yoga.")
            st.write("* Limit caffeine intake.")
        elif a_prediction in range(15,20):
            st.write("* Try out pet caring.")
            st.write("* Talk to someone you trust.")
            st.write("* Keep a diary.")
            st.write("* Maintain a healthy diet.")
            st.write("* Limit caffeine intake.")
            st.write("* Avoid smoking.")
        elif a_prediction > 19:
            st.write("* Seek immediate professional help.")
            st.write("* Try out therapy and counseling.")

# Questionnaire page 2 (Depression)
def questionnaire_page_depression():
    st.title("Depression Level Prediction")
    st.write("Please answer the questions below.")

    # Get age from user
    d_age = st.number_input("Enter your age:", min_value=16, max_value=25, step=1)

    # Get gender from user
    gender = st.radio("Select your gender:", ("Male", "Female"))
    d_gender_numeric = gender_to_numeric[gender]

    # Get user input for the questionnaire
    user_input = []
    for question, options in questions_depression.items():
        selected_option = st.selectbox(f"{question}:", options)
        numeric_value = options.index(selected_option)
        user_input.append(numeric_value)

    # Make prediction using the loaded model for depression
    if st.button("Make Prediction for Depression"):
        d_prediction = calculate_prediction(d_age, d_gender_numeric, user_input, svc_model_depression)
        st.write(f"Your Depression Score: {d_prediction}")
        st.subheader("Recommendations:")
        if d_prediction in range(0, 10):
            st.write("* Practice self-care.")
            st.write("* Maintain social connections.")
            st.write("* Engage in volunteer activities.")
        elif d_prediction in range(10, 14):
            st.write("* Seek social support.")
            st.write("* Practice relaxation techniques like yoga and meditation.")
            st.write("* Monitor progress.")
            st.write("* Engage in enjoyable activities.")
        elif d_prediction in range(14, 21):
            st.write("* Try out therapy.")
            st.write("* Limit sources of stress.")
            st.write("* Monitor progress.")
        elif d_prediction in range(20, 28):
            st.write("* Seek professional help.")
            st.write("* Try out therapy and counseling.")
            st.write("* Prioritize safety.")
            st.write("* Practice meditation.")
        elif d_prediction > 27:
            st.write("* Seek immediate professional help.")
            st.write("* Avoid isolation.")
            st.write("* Try out therapy and counseling.")

# Main function
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to:", ["Home", "Anxiety Prediction", "Depression Prediction"])

    if page == "Home":
        home_page()
    elif page == "Anxiety Prediction":
        questionnaire_page_anxiety()
    elif page == "Depression Prediction":
        questionnaire_page_depression()

st.markdown(page_bg, unsafe_allow_html=True)

# Execute the main function
if __name__ == "__main__":
    main()

