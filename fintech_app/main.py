"""Python file to serve as the frontend"""
import sys
import os
import time

sys.path.append(os.path.abspath('.'))

import streamlit as st
from fintech_app.components.sidebar import sidebar
from fintech_app.constants.dataScienceConstants import data_science_web_urls
from fintech_app.constants.dataScienceConstants import finance_gpt_urls
from fintech_app.constants.dataScienceConstants import others_urls
from fintech_app.constants.machineLearningConstants import machine_learning_web_urls
from fintech_app.constants.applicationConstants import template
from embedchain.config import LlmConfig


def ingest_training_data():
    web_urls = data_science_web_urls + machine_learning_web_urls + finance_gpt_urls + others_urls
    with st.spinner('Loading data ....please wait'):
        for url in web_urls:
            url_ = url
            fintech_chat_bot.add(url_)

    st.session_state["IS_BOT_READY"] = True


def response_embedchain(query):
    """Logic for loading the chain you want to use should go here."""
    llm_config = LlmConfig(template=template, system_prompt="")
    response = fintech_chat_bot.query(query, config=llm_config)
    return response


def add_data_form(r):
    st.session_state[f"url_{r}"] = [st.session_state.get(f"value_{r}")]
    print(st.session_state.get(f"{r}"))


def toggle_closed():
    st.session_state["expander_state"] = False


if __name__ == "__main__":

    st.set_page_config(
        page_title="💂‍♂️: Virtual Assistant",
        page_icon="💂‍♂️",
        layout="wide",
        initial_sidebar_state="expanded", )
    st.header(":orange[💬 AI Software Development Virtual Assistant for Practitioners in FinTechs]")

    sidebar()

    if "expander_state" not in st.session_state:
        st.session_state["expander_state"] = True

    if not st.session_state.get("OPENAI_API_CONFIGURED"):
        st.error("Please configure your API Keys!")

    if st.session_state.get("OPENAI_API_CONFIGURED"):
        st.markdown(":green[Chatbot Started and Ready:]")
        from embedchain import App as ecApp

        fintech_chat_bot = ecApp()
        fintech_chat_bot.online = True
        # ingesting data
        if not st.session_state.get("IS_BOT_READY"):
            with st.spinner('Waiting for data ingestion to complete'):
                ingest_training_data()
            st.success('Data Ingestion Done!')

        if st.session_state.get("IS_BOT_READY"):

            if "messages" not in st.session_state:
                st.session_state["messages"] = [
                    {"role": "assistant", "content": "How can I help you? Please enter your question below."}]

            # Display chat messages from history on app rerun
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if user_input := st.chat_input("Enter your question?"):
                # Add user message to chat history
                st.session_state.messages.append({"role": "user", "content": user_input})
                # Display user message in chat message container
                with st.chat_message("user"):
                    st.markdown(user_input)
                # Display assistant response in chat message container
                with st.chat_message("assistant"):
                    message_placeholder = st.empty()
                    full_response = ""

                    with st.spinner('Chatbot is thinking of the answer...please wait'):
                        assistant_response = response_embedchain(user_input)
                    # Simulate stream of response with milliseconds delay
                    for chunk in assistant_response.split():
                        full_response += chunk + " "
                        time.sleep(0.05)
                        # Add a blinking cursor to simulate typing
                        message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
