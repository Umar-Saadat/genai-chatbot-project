import streamlit as st
import time
from chatbot import get_response

# 🎯 App UI
st.title("🤖 Gemini Chatbot (Stable Version)")

# 🧠 Session memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🟢 Show chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# 💬 Input box
user_input = st.chat_input("Type your message...")

if user_input and user_input.strip():

    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    # 🤖 Bot response
    with st.chat_message("assistant"):
        placeholder = st.empty()

        # ⛔ Prevent spam delay (IMPORTANT for quota protection)
        time.sleep(1)

        reply = get_response(user_input)

        # ✨ typing effect
        full_text = ""
        for char in reply:
            full_text += char
            placeholder.markdown(full_text + "▌")
            time.sleep(0.002)

        placeholder.markdown(full_text)

    # Save bot message
    st.session_state.messages.append({"role": "assistant", "content": reply})
