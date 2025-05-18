import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
from utils import set_background, get_translator

# Initialize Firebase once
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

# Admin credentials (hardcoded)
ADMIN_USERNAME = "ADMIN"
ADMIN_PASSWORD = "0000"

def show_admin_dashboard(t):
    st.header("Admin Dashboard")

    ref = db.reference('/')
    all_data = ref.get()

    if not all_data:
        st.info("No data found.")
        return

    for user_id, user_data in all_data.items():
        with st.expander(f"User ID: {user_id}", expanded=False):
            st.markdown("### User Details")
            st.write(f"**Username:** {user_data.get('Username', '-')}")
            st.write(f"**Shop:** {user_data.get('Shop', '-')}")
            st.write(f"**Product:** {user_data.get('product', '-')}")
            st.write(f"**Quantity (g):** {user_data.get('quantity', 0)}")
            st.write(f"**Transaction ID:** {user_data.get('transaction_id', '-')}")
            st.write(f"**Bill Placed:** {'✅ Yes' if user_data.get('Bill', False) else '❌ No'}")


def app(lang_toggle):
    set_background()
    t = get_translator(lang_toggle)

    st.title(t("admin_login_title"))

    username = st.text_input(t("Adminname"))
    password = st.text_input(t("password"), type="password")
    login_btn = st.button(t("login_button"))

    if login_btn:
        if username == "ADMIN" and password == "0000":
            st.success(t("success"))
            show_admin_dashboard(t)
        else:
            st.error(t("error"))
