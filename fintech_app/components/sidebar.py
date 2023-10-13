import streamlit as st
import os
from dotenv import load_dotenv

from fintech_app.components.faq import faq


def set_open_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key
    os.environ["OPENAI_API_KEY"] = api_key
    st.session_state["OPENAI_API_CONFIGURED"] = True
    print('OPENAI API key is Configured Successfully!')


def sidebar():
    load_dotenv()
    with st.sidebar:

        try:
            api_key = os.getenv("OPENAI_API_KEY")
            os.environ["OPENAI_API_KEY"] = api_key
            st.session_state["OPENAI_API_CONFIGURED"] = True
        except:
            st.markdown(
                "## Please configure an OpenAI key \n"
                "From [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"
            )
        st.title(':orange[About the Chatbot]')
        st.markdown("This chatbot is built to assist the below practitioners to develop AI software:")
        st.markdown("- Fintech Subject Matter Experts")
        st.markdown("- Data Scientists\n")
        st.markdown("- Data Engineers\n")
        st.markdown("- Machine Learning Engineers\n")
        st.markdown("- Machine Learning DevOps\n")
        st.markdown("---")
        st.markdown("This Chatbot was developed as part of the MBA research project")
        st.markdown(":orange[By Peter T Nkomo (2023)]")
        st.markdown("---")

        faq()
