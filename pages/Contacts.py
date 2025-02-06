import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")

with st.form(key="email_form"):
    user_email = st.text_input("audrius13toto@gmail.com")
    option = st.selectbox(
        'What topic do you want to discuss?',
        df["topic"])
    raw_message = st.text_area("Text")
    message = f"""\
subject: New email from {user_email}

from: {user_email}
topic: {option}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent succesfully")