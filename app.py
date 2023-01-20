import openai
import streamlit as st

openai.api_key = st.secrets["api_secret"]

"""
# Welcome to St Barts Cardiology Chatbot!
Ask any questions below:

Note:
This app uses OpenAI's GPT-3 to generate answers and is for research purposes only.
This is not medical advice.
"""

chatbot_input = st.text_input('Ask a question?','What is an angiogram?')

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=chatbot_input,
    temperature=0.1,
    max_tokens=4000
)

answer = 'BartsChatbot:'+response["choices"][0]["text"]
# st.button(label="Submit", help='press to ask your question', on_click=answer)

st.write(answer)
print(answer)

"""
Please email your feedback to bartshealth.bartsaf@nhs.net
"""
