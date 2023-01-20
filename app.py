import openai
import streamlit as st

openai.api_key = st.secrets["api_secret"]

"""
# Welcome to your Barts Hospital cardiology chatbot!

Note:
This app is for research purposes only and the answers given can be wrong.
This is not medical advice.
"""

chatbot_input = st.text_input('Ask your question below',\x1B['e.g. what is a pacemaker?...']\x1B)

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=chatbot_input,
    temperature=0.5
)

answer = response["choices"][0]["text"]
st.write(answer)
print(answer)

"""
Please email your feedback to bartshealth.bartsaf@nhs.net
"""
