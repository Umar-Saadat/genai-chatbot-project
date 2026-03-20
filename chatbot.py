import google.generativeai as genai
import streamlit as st

# 🔐 Get API key from Streamlit secrets
API_KEY = st.secrets["API_KEY"]

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def get_response(user_input):
    response = model.generate_content(user_input)
    return response.text
