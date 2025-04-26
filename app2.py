import streamlit as st
from utils import set_background, show_title_image, get_translator, users, admins, calculate_price

# Setup
st.set_page_config(page_title="Login/Signup", layout="wide")
set_background()
lang_toggle = st.sidebar.checkbox("Switch to Tamil")
t = get_translator(lang_toggle)

show_title_image()
st.header(t("Login Portal"))

role = st.radio(t("Login as:"), [t("User"), t("Admin")])
username = st.text_input(t("Username"))
password = st.text_input(t("Password"), type="password")

if st.button(t("Login")):
    if (role == t("User") and users.get(username) == password) or (role == t("Admin") and admins.get(username) == password):
        st.success(f"{t('Welcome')} {username}!")
        if role == t("User"):
            st.subheader(t("Card Type: APL"))
            st.write(t("🧾 Order Status: Not received this month "))
            with st.form("order_form", clear_on_submit=False):
                quantity = st.number_input(t("Enter quantity of rice (in grams)"), min_value=0, step=100, key="quantity")
                price = calculate_price(quantity)
                st.write(f"💸 {t('Pay via GPay: UPI@gov')}")
                st.write(f"{t('Total Amount')}: ₹{price:.2f}")
                submitted = st.form_submit_button(t("Place Order"))
    else:
        st.error("Invalid username or password")
