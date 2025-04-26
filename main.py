import streamlit as st
from utils import set_background, show_title_image, get_translator

# === Setup ===
st.set_page_config(page_title="Tamil Nadu Ration Shop", layout="wide")
set_background()

st.sidebar.title("🛒 Tamil Nadu Ration Shop")
lang_toggle = st.sidebar.checkbox("Switch to Tamil")
t = get_translator(lang_toggle)

menu = st.sidebar.radio("📂 Menu", [
    "🏠 Home", "📊 Stock Availability", "🔐 Login / Signup", "📬 Grievance", "🌐 Language"])

# === Home Page ===
if menu == "🏠 Home":
    show_title_image()
    st.markdown(f"<h1 style='color:black; font-weight:900;'>{t('Welcome to Tamil Nadu Ration Shop Portal')}</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:black; font-weight:900; font-size:18px;'>{t('This portal allows citizens to:')}</p>", unsafe_allow_html=True)
    st.markdown(f"""
    <ul style='color: black; font-weight: 900; font-size: 16px; list-style-type: disc; margin-left: 20px;'>
        <li>{t('- Track shop stock')}</li>
        <li>{t('- Submit complaints')}</li>
        <li>{t('- Place orders & track status')}</li>
    </ul>
    """, unsafe_allow_html=True)

# === Redirect to other apps ===
elif menu == "📊 Stock Availability":
    st.switch_page("app1.py")

elif menu == "🔐 Login / Signup":
    st.switch_page("app3.py")

elif menu == "📬 Grievance":
    st.switch_page("app4.py")

elif menu == "🌐 Language":
    st.switch_page("app5.py")

