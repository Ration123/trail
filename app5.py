import streamlit as st
import qrcode
from io import BytesIO
from utils import get_translator, calculate_price

def app(lang_toggle):
    t = get_translator(lang_toggle)

    st.header(t("Rice Order Portal"))
    st.write(t("Please enter your desired quantity."))

    quantity = st.number_input(t("Enter quantity of rice (in grams)"), min_value=0, step=100)

    if quantity > 0:
        price = calculate_price(quantity)
        st.info(f"💸 {t('Total Amount')}: ₹{price:.2f}")

        # --- Generate UPI Payment QR ---
        upi_id = "myupiid@gov"   # Your UPI ID
        name = "Order"
        currency = "INR"

        upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={price}&cu={currency}"

        # Generate QR code image
        qr = qrcode.make(upi_link)
        buffered = BytesIO()
        qr.save(buffered, format="PNG")

        st.subheader("🧾 " + t("Scan to Pay"))
        st.image(buffered.getvalue(), width=250)  # Show QR code

        st.write(f"📌 {t('UPI ID')}: `{upi_id}`")
        st.markdown(f"[{t('Or Click to Pay')}]({upi_link})")

        # --- Place Order Button ---
        if st.button(t("Place Order")):
            st.success(t("Order placed successfully!"))

            # --- Ask for payment confirmation ---
            payment_done = st.radio(t("Have you completed the payment?"), (t("Yes"), t("No")))

            if payment_done == t("Yes"):
                st.success(t("Thank you for your payment! Your order is confirmed. ✅"))
            elif payment_done == t("No"):
                st.warning(t("Please complete the payment to confirm your order. 🔴"))
