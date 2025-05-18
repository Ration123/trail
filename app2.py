import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from utils import set_background, show_title_image, get_translator, users, admins, calculate_price

# Initialize Firebase only once
if not firebase_admin._apps:
    cred = credentials.Certificate({
        "type": st.secrets.FIREBASE.type,
        "project_id": st.secrets.FIREBASE.project_id,
        "private_key_id": st.secrets.FIREBASE.private_key_id,
        "private_key": st.secrets.FIREBASE.private_key.replace("\\n", "\n"),
        "client_email": st.secrets.FIREBASE.client_email,
        "client_id": st.secrets.FIREBASE.client_id,
        "auth_uri": st.secrets.FIREBASE.auth_uri,
        "token_uri": st.secrets.FIREBASE.token_uri,
        "auth_provider_x509_cert_url": st.secrets.FIREBASE.auth_provider_x509_cert_url,
        "client_x509_cert_url": st.secrets.FIREBASE.client_x509_cert_url
    })
    firebase_admin.initialize_app(cred, {
        'databaseURL': st.secrets.FIREBASE.databaseURL
    })

# Utility: Get UID from Firebase by username & password
def get_user_uid(username, password):
    ref = db.reference("/")
    data = ref.get()
    for uid, user in (data or {}).items():
        if user.get("Username") == username and str(user.get("password")) == str(password):
            return uid
    return None

# Main app function
def app(lang_toggle):
    set_background()
    t = get_translator(lang_toggle)
    st.title(t("Ration Ordering Portal"))

    # Session initialization
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.uid = ""
        st.session_state.username = ""
        st.session_state.user_data = {}
        st.session_state.is_admin = False

    # Login form
    if not st.session_state.logged_in:
        username = st.text_input(t("Username"))
        password = st.text_input(t("Password"), type="password")
        if st.button(t("Login")):
            # Admin login check
            if username == "ADMIN" and password == "0000":
                st.session_state.logged_in = True
                st.session_state.username = "ADMIN"
                st.session_state.is_admin = True
                st.success(f"{t('Welcome')}, ADMIN!")
            else:
                uid = get_user_uid(username, password)
                if uid:
                    user_ref = db.reference(f"/{uid}")
                    user_data = user_ref.get()
                    st.session_state.logged_in = True
                    st.session_state.uid = uid
                    st.session_state.username = username
                    st.session_state.user_data = user_data
                    st.session_state.is_admin = False
                    st.success(f"{t('Welcome')}, {username}!")
                    st.info(f"{t('Your Shop Number')}: {user_data.get('Shop')}")
                else:
                    st.error(t("Invalid username or password."))
        return  # Stop here until login successful

    # After login
    
    # Admin dashboard: Show all user details
    if st.session_state.is_admin:
        st.header("🔐 Admin Dashboard - All Users Data")
        all_users = db.reference("/").get()
        if all_users:
            for uid, user in all_users.items():
                st.subheader(f"User ID: {uid}")
                st.write(f"**Username:** {user.get('Username')}")
                st.write(f"**Shop Number:** {user.get('Shop')}")
                st.write(f"**Bill Placed:** {user.get('Bill')}")
                st.write(f"**Product:** {user.get('product')}")
                st.write(f"**Quantity:** {user.get('quantity')} g")
                st.write(f"**Transaction ID:** {user.get('transaction_id')}")
                st.markdown("---")
        else:
            st.write("No user data found.")
        return  # Stop further UI for admin

    # User dashboard / order portal
    user_data = st.session_state.user_data
    user_ref = db.reference(f"/{st.session_state.uid}")

    if user_data.get("Bill"):
        st.success("✅ " + t("Order already placed!"))
        st.write(f"**{t('Product')}**: {user_data.get('product')}")
        st.write(f"**{t('Quantity')}**: {user_data.get('quantity')}g")
        st.write(f"**{t('Transaction ID')}**: {user_data.get('transaction_id')}")
    else:
        st.subheader("🛒 " + t("Place Your Order"))
        product = st.selectbox(t("Select Product"), [t("Rice")])
        quantity = st.number_input(t("Enter quantity in grams"), min_value=100, step=100, key="quantity_input")
        price = (quantity // 100) * 10
        st.write(f"💰 {t('Total Price')}: ₹{price}")

        st.markdown("### 📲 " + t("Scan & Pay"))
        st.image(
            f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=upi://pay?pa=keerthivasang2004@oksbi&pn=RationStore&am={price}",
            caption=t("Scan with any UPI app")
        )

        transaction_id = st.text_input(t("Enter UPI Transaction ID"), key="txn_input")

        if st.button(t("Place Order")):
            if not transaction_id.strip():
                st.error("⚠️ " + t("Please enter a valid UPI Transaction ID."))
            else:
                user_ref.update({
                    "product": product,
                    "quantity": quantity,
                    "Bill": True,
                    "transaction_id": transaction_id
                })
                st.success("✅ " + t("Order placed successfully!"))
                st.session_state.user_data = user_ref.get()
