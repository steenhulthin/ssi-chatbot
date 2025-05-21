import streamlit as st
import chatbot

st.title("Website Q&A Chatbot")

user_input = st.text_input("Ask a question about the website")

if user_input:
    answer = chatbot.qa.run(user_input)
    st.write(answer)