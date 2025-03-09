import streamlit as st
import requests

# Hugging Face API Key
HF_API_KEY = "your-access-key"

# Hugging Face Model URL (Choose an appropriate nutrition-based chatbot model)
MODEL_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"

# Function to query Hugging Face model
def get_nutrition_response(user_input):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": user_input}

    try:
        response = requests.post(MODEL_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and len(data) > 0:
            return data[0].get("generated_text", "Sorry, I couldn't understand that.")
        elif isinstance(data, dict):
            return data.get("generated_text", "Sorry, I couldn't understand that.")
        else:
            return "Sorry, I couldn't understand that."
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Streamlit Page Config
st.set_page_config(page_title="Nutritional Chatbot", page_icon="🥗", layout="wide")

# Sidebar Navigation
st.sidebar.title("Nutritional Chatbot")
page = st.sidebar.radio("Navigation", ["Chat", "About"])

if page == "About":
    st.sidebar.subheader("About this Chatbot")
    st.sidebar.write(
        "This chatbot provides reliable nutrition advice based on AI. "
        "It can answer questions about healthy eating, diet plans, "
        "and nutritional facts."
    )

# Main Page
if page == "Chat":
    st.title("Nutritional Chatbot")
    st.write("Ask any nutrition-related questions and get instant responses.")

    # Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display Previous Messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # User Input
    user_input = st.chat_input("Ask me anything about diet, nutrition, and healthy eating.")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Get chatbot response
        response = get_nutrition_response(user_input)
        st.session_state.messages.append({"role": "assistant", "content": response})

        # Display chatbot response
        with st.chat_message("assistant"):
            st.markdown(response)

# Footer with Credit
st.markdown(
    "<hr><center>Built using Streamlit | © 2025 | Developed by Chandana</center>",
    unsafe_allow_html=True
)
