import streamlit as st
import pandas as pd
from send_email import sending

topics = pd.read_csv('topics.csv')
choice = topics['topic']
st.header("Contact Me")
with st.form(key="user_form"):
    user_addr = st.text_input("Your email address",placeholder="user@example.com")
    user_topic = st.selectbox("Choice topic",choice)
    user_message = st.text_area("Your message",placeholder="Nothing")
    message = f"""\
Subject: New email from {user_addr}

From: {user_addr}
Topic: {user_topic}
{user_message}
"""
    user_clicked = st.form_submit_button("Send")
    if user_clicked:
        sending(message)
        st.info("Your email was sent successfully!")