import streamlit as st
from streamlit_option_menu import option_menu
from utils import set_background, show_title_image, get_translator
import app1
import app2
import app3
import app4
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
with st.sidebar:
    selected_option = option_menu(
        menu_title="ISA MIT Student Chapter",
        options=[ 
            "Stock Availability",
            "Login / Signup",
            "Grievance",
            "Language",
            "Contact"
        ],
        icons=[
            "bar-chart-line", "lock", "envelope", "globe",
        ],
        menu_icon="gear-fill",
        default_index=0,
        styles={
            "container": {"padding": "5!important", "background-color": "#1f4e79"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "18px", "--hover-color": "#FFA500"},
            "nav-link-selected": {"background-color": "#FFA500"},
        }
    )

# === Redirect to other apps ===
elif menu == "📊 Stock Availability":
    app1.app()

elif menu == "🔐 Login / Signup":
    app2.app()

elif menu == "📬 Grievance":
    app3.app()

elif menu == "🌐 Language":
    app4.app()

