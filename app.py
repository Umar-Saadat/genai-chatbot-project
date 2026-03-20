import streamlit as st
import time
from chatbot import get_response

# Title
st.title("🤖 Simple Think Bot")

# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Type a message...")

if user_input:
    
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    #  Bot response with animation
    with st.chat_message("assistant"):
        placeholder = st.empty()
        
        reply = get_response(user_input)

        full_text = ""
        for char in reply:
            full_text += char
            placeholder.markdown(full_text + "⚪")
            time.sleep(0.001)

        placeholder.markdown(full_text)

    # Save bot message
    st.session_state.messages.append({"role": "assistant", "content": reply})