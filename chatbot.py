import google.generativeai as genai
import streamlit as st
import time

# 🔑 API KEY (BEST PRACTICE: use secrets in deployment)
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# ⚡ Fast model (low cost + high speed)
model = genai.GenerativeModel("gemini-1.5-flash")


def get_response(user_input):
    """
    Safe Gemini response with retry + error handling
    """

    for attempt in range(3):
        try:
            response = model.generate_content(user_input)

            if response and response.text:
                return response.text

        except Exception as e:
            print(f"Attempt {attempt+1} failed:", e)
            time.sleep(2)

    return "⚠️ AI is busy or quota exceeded. Please try again later."
