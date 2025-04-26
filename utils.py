import streamlit as st
from deep_translator import GoogleTranslator
import bcrypt

# Dummy users and admins (hashed passwords)
users = {"user1": bcrypt.hashpw("pass123".encode('utf-8'), bcrypt.gensalt()),
         "user2": bcrypt.hashpw("pass456".encode('utf-8'), bcrypt.gensalt())}
admins = {"admin1": bcrypt.hashpw("admin123".encode('utf-8'), bcrypt.gensalt())}

def calculate_price(quantity):
    return (quantity / 100) * 10

# Background setup
def set_background():
    st.markdown("""
        <style>
        html, body, .stApp {
            background-image: url("https://raw.githubusercontent.com/Ration123/trail/main/beautiful-view-green-fields-sunrise-captured-canggu-bali.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: scroll;
            background-position: center center;
            height: 100%;
            width: 100%;
        }
        .block-container {
            background-color: rgba(255, 255, 255, 0.10);
            padding: 2rem;
            border-radius: 20px;
            backdrop-filter: blur(4px);
            margin-top: 40px;
        }
        .stMarkdown, .stTextInput, .stTextArea, .stSelectbox, .stRadio, .stButton {
            color: black !important;
            font-weight: 900 !important;
        }
        input, textarea {
            background-color: rgba(255, 255, 255, 0.85) !important;
            color: black !important;
            font-weight: 900 !important;
        }
        footer, header, .viewerBadge_container__1QSob, .st-emotion-cache-1v0mbdj {
            display: none !important;
        }
        .stApp {
            padding-top: 50px;
        }
        </style>
    """, unsafe_allow_html=True)

def show_title_image():
    st.image("https://raw.githubusercontent.com/Ration123/RATION/main/title", use_container_width=True)

def get_translator(lang):
    translator = GoogleTranslator(source='en', target='ta') if lang else None

    def t(text):
        if lang:
            try:
                return translator.translate(text)
            except Exception as e:
                st.error(f"Translation failed: {e}")
                return text
        else:
            return text

    return t
