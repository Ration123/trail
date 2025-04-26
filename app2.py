import streamlit as st
from utils import set_background, show_title_image, get_translator, users, admins, calculate_price

def app():
    # Setup
    set_background()  # Setting the background image

    # Language toggle
    lang_toggle = st.sidebar.checkbox("Switch to Tamil")
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
        if (role == t("User") and users.get(username) == password) or (role == t("Admin") and admins.get(username) == password):
            st.success(f"{t('Welcome')} {username}!")  # Welcome message
            
            # If the user role is selected
            if role == t("User"):
                st.subheader(t("Card Type: APL"))
                st.write(t("🧾 Order Status: Not received this month"))
                
                # Order form for the user
                with st.form("order_form", clear_on_submit=True):  # Added clear_on_submit=True to clear fields
                    quantity = st.number_input(t("Enter quantity of rice (in grams)"), min_value=0, step=100, key="quantity")
                    price = calculate_price(quantity)  # Calculate price based on quantity
                    st.write(f"💸 {t('Pay via GPay: UPI@gov')}")
                    st.write(f"{t('Total Amount')}: ₹{price:.2f}")
                    
                    # Submit order button
                    submitted = st.form_submit_button(t("Place Order"))
                    if submitted:
                        st.success(f"{t('Your order has been placed successfully!')}")
                        # Optionally, display an order summary or reset form for a new order

        else:
            st.error(t("Invalid username or password"))

if __name__ == "__main__":
    app()
