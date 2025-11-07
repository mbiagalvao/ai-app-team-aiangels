import streamlit as st
import sys
import os

from src.ai_client import AIClient

# Page config
st.set_page_config(
    page_title="AI Course - Week 1 Demo",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 My First AI App")
st.write("Welcome to your first AI-powered web application!")

# Initialize AI client
try:
    if 'ai_client' not in st.session_state:
        st.session_state.ai_client = AIClient()
    
    # Chat interface
    st.subheader("💬 Chat with AI")
    
    user_input = st.text_input("Ask the AI anything:")
    
    if st.button("Send") and user_input:
        with st.spinner("AI is thinking..."):
            response = st.session_state.ai_client.chat(user_input)
        
        st.success("AI Response:")
        st.write(response)
    
    # Team info
    st.sidebar.header("📋 Team Information")
    st.sidebar.write("**Team Name:** [Your team name]")
    st.sidebar.write("**Members:** [List your team members]")
    st.sidebar.write("**App Idea:** [Your chosen app idea]")
    
    st.sidebar.header("🎯 Week 1 Goals")
    st.sidebar.checkbox("✅ Python installed", value=True)
    st.sidebar.checkbox("✅ Virtual environment set up", value=True)
    st.sidebar.checkbox("✅ Google AI Studio configured", value=True)
    st.sidebar.checkbox("✅ GitHub repository created", value=True)
    st.sidebar.checkbox("✅ First AI API call successful", value=True)
    st.sidebar.checkbox("✅ Streamlit app running", value=True)

except Exception as e:
    st.error(f"Error initializing AI client: {e}")
    st.info("Make sure your .env file contains GOOGLE_API_KEY")