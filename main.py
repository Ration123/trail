import streamlit as st
from streamlit_option_menu import option_menu
from utils import set_background, show_title_image, get_translator,set_responsive_style
import app1
import app2
import app3
import app4
import app6
import app7
import app8
# === Setup ===
set_background()
set_responsive_style()
# Only ONE language toggle checkbox here
lang_toggle = st.sidebar.checkbox("Switch to Tamil", key="lang_toggle_checkbox")
t = get_translator(lang_toggle)

# === Sidebar Option Menu ===
with st.sidebar:
    selected_option = option_menu(
        menu_title="🛒 Tamil Nadu Ration Shop",
       options = [
    "🏠 Home",
    "📊 Stock Availability",
    "🔐 User Login",
    "🔑 Admin Login",
    "📬 Grievance",
    "🌐 Language",
    "📝 New Registration",     # <-- 7th
    "📞 Contact"               # <-- 8th
],
        icons = [
    "house-door", 
    "bar-chart-line", 
    "lock", 
    "key",               # Icon for Admin Login
    "envelope", 
    "globe",
    "person-plus",       # Icon for New Registration
    "telephone"
],
        menu_icon="gear-fill",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "5!important", "background-color": "#1f4e79"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {"color": "white", "font-size": "18px", "--hover-color": "#FFA500"},
            "nav-link-selected": {"background-color": "#FFA500"},
        }
    )

# === Main Area Routing ===
if selected_option == "🏠 Home":
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
    app7.chatbot_app()

elif selected_option == "📊 Stock Availability":
    app1.app(lang_toggle)

elif selected_option == "🔐 User Login":
    app2.app(lang_toggle)
elif selected_option == "🔑 Admin Login":
    app6.app(lang_toggle) 

elif selected_option == "📬 Grievance":
    app3.app(lang_toggle)

elif selected_option == "🌐 Language":
    app4.app(lang_toggle)
elif selected_option == "📝 New Registration":
    app8.app(lang_toggle)

elif selected_option == "📞 Contact":
    # Contact page content
    st.markdown(f"<h2 style='color:black; font-weight:900;'>{t('Contact Us')}</h2>", unsafe_allow_html=True)
    
    # Add clickable links for the phone number and email
    contact_number = "9344810244"
    email = "keerthivasangopal2004@gmail.com"
    
    st.markdown(f"""
        <p style='color:black; font-weight:900; font-size:18px;'>
            {t('📞 Contact us at:')} <a href='tel:{contact_number}' style='color:#1f4e79;'>{contact_number}</a>
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
        <p style='color:black; font-weight:900; font-size:18px;'>
            {t('📧 Email:')} <a href='mailto:{email}' style='color:#1f4e79;'>{email}</a>
        </p>
    """, unsafe_allow_html=True)




