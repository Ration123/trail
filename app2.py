import streamlit as st
from utils import set_background, show_title_image, get_translator, users, admins, calculate_price
import bcrypt
import app5

def app(lang_toggle):
    set_background()
    t = get_translator(lang_toggle)

    show_title_image()
    st.header(t("Login Portal"))

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.username = None

    if not st.session_state.logged_in:
        # Login form
        role = st.radio(t("Login as:"), [t("User"), t("Admin")])
        username = st.text_input(t("Username"))
        password = st.text_input(t("Password"), type="password")

        if st.button(t("Login")):
            if role == t("User") and username in users and bcrypt.checkpw(password.encode('utf-8'), users[username]):
                st.session_state.logged_in = True
                st.session_state.role = "User"
                st.session_state.username = username
            elif role == t("Admin") and username in admins and bcrypt.checkpw(password.encode('utf-8'), admins[username]):
                st.session_state.logged_in = True
                st.session_state.role = "Admin"
                st.session_state.username = username
            else:
                st.error(t("Invalid username or password"))
    else:
        if st.session_state.role == "User":
            app5.app(lang_toggle)
        elif st.session_state.role == "Admin":
            st.success(f"{t('Welcome Admin')} {st.session_state.username}!")
            # (admin panel you can show here later)
