import streamlit as st
from utils import get_translator, calculate_price

def app(lang_toggle):
    t = get_translator(lang_toggle)

    st.header(t("Rice Order Portal"))
    st.write(t("Please enter your desired quantity."))

    quantity = st.number_input(t("Enter quantity of rice (in grams)"), min_value=0, step=100)

    if quantity > 0:
        price = calculate_price(quantity)
        st.info(f"💸 {t('Total Amount')}: ₹{price:.2f}")

        # Show UPI payment info
        st.subheader(t("Pay via GPay"))
        st.image("static/gpay_qr.png", caption=t("Scan to Pay"), width=250)  # adjust path and width
        st.write(f"📌 {t('UPI ID')}: UPI@gov")

    if st.button(t("Place Order")):
        st.success(t("Your order has been placed successfully!"))
