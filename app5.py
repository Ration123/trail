import streamlit as st
from utils import set_background, show_title_image, get_translator

# Setup
st.set_page_config(page_title="Language Settings", layout="wide")
set_background()
lang_toggle = st.sidebar.checkbox("Switch to Tamil")
t = get_translator(lang_toggle)

show_title_image()
st.header(t("Language Switcher"))
st.write(t("Use the checkbox in the sidebar to toggle between Tamil and English."))
