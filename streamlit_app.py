import sys
import streamlit as st
import datetime
import requests

BASE_URL = "http://localhost:8000"

st.set_page_config()

st.title()

# initialize chat history message
if "messages" not in st.session_state:
    st.session_state.messages = []


st.header()

with st.form():
    user_input = ""
    submit_button = ""

if submit_button and user_input.strip():
    pass