import streamlit as st
from langchain_groq import ChatGroq

st.title("🦜🔗 Quickstart App")

groq_api_key = st.sidebar.text_input("Groq API Key", type="password")
# groq_api_key = "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"

def generate_response(input_text):
    model = ChatGroq(model_name="llama3-8b-8192", 
                     temperature=0.7, 
                     api_key=groq_api_key)
    st.info(model.invoke(input_text))


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not groq_api_key.startswith("gsk_"):
        st.warning("Please enter your Groq API key!", icon="⚠")
    if submitted and groq_api_key.startswith("gsk_"):
        generate_response(text)