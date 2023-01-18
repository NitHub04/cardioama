# Import from standard library
import logging
import re

# Import from 3rd party libraries
import streamlit as st
import streamlit.components.v1 as components

# Import modules
import oai

#OpenAI key
openai.api_key = "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"

# Configure logger
logging.basicConfig(format="\n%(asctime)s\n%(message)s", level=logging.INFO, force=True)



response = openai.Completion.create(
    engine="text-davinci-002",
    prompt='[QUESTION]',
    temperature=0.5
)

answer = response["choices"][0]["text"]
st.write(answer)

"""
# Define functions
def generate_text(topic: str, mood: str = "", style: str = ""):
    """Generate Tweet text."""
    if st.session_state.n_requests >= 5:
        st.session_state.text_error = "Too many requests. Please wait a few seconds before generating another Tweet."
        logging.info(f"Session request limit reached: {st.session_state.n_requests}")
        st.session_state.n_requests = 1
        return

    st.session_state.tweet = ""
    st.session_state.image = ""
    st.session_state.text_error = ""

    if not topic:
        st.session_state.text_error = "Please enter a topic"
        return

    with text_spinner_placeholder:
        with st.spinner("Please wait while your Tweet is being generated..."):
            mood_prompt = f"{mood} " if mood else ""
            if style:
                twitter = twe.Tweets(account=style)
                tweets = twitter.fetch_tweets()
                tweets_prompt = "\n\n".join(tweets)
                prompt = (
                    f"Write a {mood_prompt}Tweet about {topic} in less than 120 characters "
                    f"and in the style of the following Tweets:\n\n{tweets_prompt}\n\n"
                )
            else:
                prompt = f"Write a {mood_prompt}Tweet about {topic} in less than 120 characters:\n\n"

            openai = oai.Openai()
            flagged = openai.moderate(prompt)
            mood_output = f", Mood: {mood}" if mood else ""
            style_output = f", Style: {style}" if style else ""
            if flagged:
                st.session_state.text_error = "Input flagged as inappropriate."
                logging.info(f"Topic: {topic}{mood_output}{style_output}\n")
                return

            else:
                st.session_state.text_error = ""
                st.session_state.n_requests += 1
                st.session_state.tweet = (
                    openai.complete(prompt).strip().replace('"', "")
                )
                logging.info(
                    f"Topic: {topic}{mood_output}{style_output}\n"
                    f"Tweet: {st.session_state.tweet}"
                )
                
""" 
