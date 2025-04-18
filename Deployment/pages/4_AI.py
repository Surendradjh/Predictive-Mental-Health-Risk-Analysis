import streamlit as st 
import pandas as pd
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from main import df 
# Page config
st.set_page_config(page_title="AI Mental Health Suggester", layout="centered")
# Dark mode UI styling
st.markdown("""
<style>
.stApp {
    background-color: #1e1e2f;
    color: #f5f6fa;
    font-family: 'Segoe UI', sans-serif;
}
h1, h2, h3, h4, h5, h6 {
    color: #00adb5;
}
label, .stTextInput label {
    color: #f5f6fa !important;
}
.stTextInput>div>input {
    background-color: #2c2f3e;
    color: #f5f6fa;
    border: 1px solid #444;
    border-radius: 8px;
}
.stButton>button {
    background-color: #00adb5;
    color: black;
    padding: 0.5em 1.5em;
    font-weight: bold;
    border-radius: 10px;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #008891;
    color: white;
}
</style>
""", unsafe_allow_html=True)
# Title
st.markdown("<h2 style='text-align: center;'>💬 AI Mental Health Suggester</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Ask personalized questions to get suggestions based on your daily activities.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)
# Input
question = st.text_input("**Get answers with AI**", placeholder="Ex:- What is the status about my health?")
if st.button("Get Answer") and question.strip() != "":
    prompt_template = ChatPromptTemplate(messages=[
        ("system", "You are an AI assistant focused on improving mental health by providing tailored suggestions based on the user's details. "
               "Suggest simple and effective daily activities that align with the user's lifestyle. "
               "When the user asks about health-related topics, explain the health condition based on the details provided. "
               "If the question is unclear or irrelevant, ask the user to enter a proper question. "
               "Based on the user details you have to return the suggestions"
               "Provide suggestions with a brief two-line explanation."),
        ("human", "Here's my daily activity details: {activity_details} and my question: {question}")
    ])
    api_key = "AIzaSyC9j5KaPVcanw9nvPAfKfORBqsCzBjx37I"
    genai_model = ChatGoogleGenerativeAI(api_key=api_key, model="gemini-2.0-flash")
    output_parser = StrOutputParser()
    chain = prompt_template | genai_model | output_parser
    # Get personalized suggestion
    tips = chain.invoke({
        "activity_details": str(df),
        "question": question
    })
    st.markdown("---")
    st.markdown("### 🧠 AI Response:")
    st.write(tips)
