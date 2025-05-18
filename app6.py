import streamlit as st
import firebase_admin
from firebase_admin import credentials, db

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

def admin_login():
    st.title("Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_btn = st.button("Login")

    if login_btn:
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.success("Logged in successfully as admin!")
            # Call your admin dashboard function here or show admin content
            show_admin_dashboard()
        else:
            st.error("Invalid username or password")

def show_admin_dashboard(t):
    st.header(t["dashboard"])
    ref = db.reference('/')
    all_data = ref.get()

    st.write(t["firebase_data"])
    st.json(all_data)

def app(lang_toggle):
    set_background()
    t = get_translator(lang_toggle)
    admin_login()

    if login_btn:
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            st.success(t["success"])
            show_admin_dashboard(t)
        else:
            st.error(t["error"])
    # Add more admin controls here as needed
