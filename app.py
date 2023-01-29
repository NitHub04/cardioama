import openai
import streamlit as st
from deta import Deta
from datetime import datetime
import pandas as pd

openai.api_key = st.secrets["api_secret"]
deta = Deta(st.secrets["deta_key"])
db = deta.Base("cardioama_db")

"""
# Welcome to St Barts Cardiology Chatbot!
Ask any questions below:

Note:
This app uses OpenAI's GPT-3 to generate answers and is for research purposes only.
This is not medical advice.
"""

chatbot_input = st.text_input('Ask a question?','What is an angiogram?')

if st.button("Submit"):
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y_%H:%M:%S")
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=chatbot_input,
    temperature=0.1,
    max_tokens=4000)

    answer = 'BartsChatbot:'+response["choices"][0]["text"]
# st.button(label="Submit", help='press to ask your question', on_click=answer)

    st.write(answer)
    print(answer)
    db.put({"a_time_stamp": timestampStr,"b_input": chatbot_input,"c_answer": answer })

"""
Please email your feedback to bartshealth.bartsaf@nhs.net
"""

admin_key = st.text_input('Admin Key','????')

@st.experimental_memo
def convert_def(df):
    return df.to_csv(index=False)

if st.button('Display') and admin_key == "1234":
    db_content = db.fetch().items
    df = pd.DataFrame.from_dict(db_content)
    st.dataframe(df)
    csv = convert_def(df)
    st.download_button("Press to Download",csv,"file.csv","text/csv",key='download-csv')
