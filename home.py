import streamlit as st

st.set_page_config(page_title="Nutritional Chatbot", page_icon="🏠", layout="wide")

st.title("🥗 Welcome to the Nutritional Chatbot!")
st.write("Get instant answers to your nutrition-related questions.")

# Button to navigate to the chatbot
st.write("Click below to start chatting:")
st.markdown("[👉 Start Chatting 💬](http://localhost:8501)", unsafe_allow_html=True)
