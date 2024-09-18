import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()
st.set_page_config(
    page_title="NDHbot",
    page_icon="icon/robots.png", 
)
st.markdown(
    """
    <style>
    .title {
        font-size: 60px;
        color: #6699FF; 
        font-family:'Times New Roman';
        text-align: center;
    }
    </style>
    <h1 class="title">🤖MR.Hau AI</h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    .welcome-message {
        font-size: 17px;
        color: #6699FF;
        font-family: 'Times New Roman';
        text-align: center;
        font-style: italic;
    }
    </style>
    <div class="welcome-message">Mang lại niềm vui cho mọi nhà</div>
    """,
    unsafe_allow_html=True
)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
gen_ai.configure(api_key=GOOGLE_API_KEY)
model=gen_ai.GenerativeModel("gemini-pro")
def translate(user):
    if user ==" model":
        return "bot"
    else:
        return "user"
 
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

for message in st.session_state.chat_session.history:
    with st.chat_message(translate(message.role),avatar="icon/chatbot.png"):
        st.markdown(message.parts[0].text)

promt = st.chat_input("Nói đi")
if promt:
    st.chat_message("user",avatar="icon/mask.png").markdown(promt)
    gemini_response = st.session_state.chat_session.send_message(promt)
    with st.chat_message("bot",avatar="icon/chatbot.png"):
        st.markdown(gemini_response.text)
