import streamlit as st
from utils import set_background, show_title_image, get_translator, users, admins, calculate_price
import bcrypt

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
            
            # Order form for the user
            st.subheader(t("Card Type: APL"))
            st.write(t("🧾 Order Status: Not received this month"))
                
            # Order form for the user
            with st.form("order_form", clear_on_submit=False):
                quantity = st.number_input(t("Enter quantity of rice (in grams)"), min_value=0, step=100, key="quantity")
                price = calculate_price(quantity)  # Calculate price based on quantity
                st.write(f"💸 {t('Pay via GPay: UPI@gov')}")
                st.write(f"{t('Total Amount')}: ₹{price:.2f}")
                    
                # Submit order button
                submitted = st.form_submit_button(t("Place Order"))
                if submitted:
                    st.success(f"{t('Your order has been placed successfully!')}")
        elif role == t("Admin") and username in admins and bcrypt.checkpw(password.encode('utf-8'), admins[username]):
            st.success(f"{t('Welcome Admin')} {username}!")
        else:
            st.error(t("Invalid username or password"))

if __name__ == "__main__":
    app()
