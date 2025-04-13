import streamlit as st
import requests
import uuid

st.set_page_config(layout="wide") 
st.title("Vietnamese Legal RAG Chatbot 🤖🇻🇳")

# Set your Flask API URL here
st.session_state.flask_api_url = "https://2b18-34-55-66-142.ngrok-free.app/chat"  # ← đổi URL này nếu cần

# Generate a random session ID
session_id = str(uuid.uuid4())

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display the chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask a legal question..."):
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the payload
    payload = {
        "message": prompt,
        "context": st.session_state.chat_history,
        "sessionId": session_id,
        "stream": True  # Enable streaming mode
    }

    # Display assistant message
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        streamed_content = ""

        try:
            print("hello")
            response = requests.post(
                st.session_state.flask_api_url,
                json=payload,
                stream=True,
                timeout=60
            )
            print("hi")

            if response.status_code == 200:
                print("hi2")
                for chunk in response.iter_lines(decode_unicode=True):
                    if chunk:
                        streamed_content += chunk
                        response_placeholder.markdown(streamed_content)
                st.session_state.chat_history.append({"role": "assistant", "content": streamed_content})
            else:
                st.error(f"Server error: {response.status_code}")

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
