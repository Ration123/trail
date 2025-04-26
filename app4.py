import streamlit as st
from utils import set_background, show_title_image, get_translator

def app(lang_toggle):
    set_background()
    t = get_translator(lang_toggle)
    # Display the title image and header
    show_title_image()
    st.header(t("Language Switcher"))
    st.write(t("Use the checkbox in the sidebar to toggle between Tamil and English."))

    if lang_toggle:
        st.write(t("You have switched to Tamil."))
    else:
        st.write(t("You have switched to English."))

