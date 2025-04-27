import streamlit as st
from utils import set_background, show_title_image, get_translator, users, admins, calculate_price
import bcrypt
import app5
def app(lang_toggle):
    set_background()
    t = get_translator(lang_toggle)  # Get translator based on language toggle

    # Display the title image and header
    show_title_image()
    st.header(t("Login Portal"))

    # Select role (User/Admin)
    role = st.radio(t("Login as:"), [t("User"), t("Admin")])

    # Inputs for username and password
    username = st.text_input(t("Username"))
    password = st.text_input(t("Password"), type="password")

    # When login button is clicked
    if st.button(t("Login")):
        # Check if the credentials match for the chosen role (User/Admin)
        if role == t("User") and username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]):
            st.success(f"{t('Welcome')} {username}!")  # Welcome message
            app5.app(lang_toggle)
        elif role == t("Admin") and username in admins and bcrypt.checkpw(password.encode('utf-8'), admins[username]):
            st.success(f"{t('Welcome Admin')} {username}!")
        else:
            st.error(t("Invalid username or password"))

