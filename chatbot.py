import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def get_response(user_input):
    response = model.generate_content(user_input)
    return response.text
