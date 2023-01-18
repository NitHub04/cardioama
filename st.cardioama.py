
# Import from standard library
import logging
import re

# Import from 3rd party libraries
import streamlit as st
import streamlit.components.v1 as components

# Import modules
import oai

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)

#OpenAI key
openai.api_key = "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"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=st.text_input(''),
    temperature=0.5
)

answer = response["choices"][0]["text"]
st.write(answer)
