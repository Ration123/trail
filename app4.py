import streamlit as st
from utils import set_background, show_title_image, get_translator

def app():
    # Setup
   
    set_background()
    lang_toggle = st.sidebar.checkbox("Switch to Tamil")
    t = get_translator(lang_toggle)

    # Display the title image and header
    show_title_image()
    st.header(t("Language Switcher"))
    st.write(t("Use the checkbox in the sidebar to toggle between Tamil and English."))

if __name__ == "__main__":
    app()
