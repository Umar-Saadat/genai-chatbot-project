from google import genai

# Add your API key
client = genai.Client(api_key="YOUR API KEY")

model = "gemini-2.5-flash"

def get_response(user_input):
    response = client.models.generate_content(
        model=model,
        contents=user_input
    )
    return response.text