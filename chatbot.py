import google.generativeai as genai
import time

# 🔑 Set your API key here
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# ⚡ Use fast + low cost model
model = genai.GenerativeModel("gemini-1.5-flash")


def get_response(user_input):
    """
    Generate response with retry + error handling
    """

    for attempt in range(3):  # retry 3 times
        try:
            response = model.generate_content(user_input)

            # If response is empty
            if not response or not response.text:
                return "⚠️ Empty response from model."

            return response.text

        except Exception as e:
            print(f"Attempt {attempt+1} failed:", e)
            time.sleep(2)  # wait before retry

    return "⚠️ API limit reached or server busy. Please try again later."
