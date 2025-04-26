import streamlit as st
from streamlit_option_menu import option_menu
from utils import set_background, show_title_image, get_translator
import app1
import app2
import app3
import app4

# === Setup ===
set_background()



# === Sidebar Option Menu ===
with st.sidebar:
    selected_option = option_menu(
        menu_title="🛒 Tamil Nadu Ration Shop",
        options=[
            "🏠 Home",
            "📊 Stock Availability",
            "🔐 Login / Signup",
            "📬 Grievance",
            "🌐 Language",
            "📞 Contact"
        ],
        icons=[
            "house-door", 
            "bar-chart-line", 
            "lock", 
            "envelope", 
            "globe",
            "telephone"
        ],
        menu_icon="gear-fill",
        default_index=0,
        orientation="vertical",   # sidebar by default vertical
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

elif selected_option == "📊 Stock Availability":
    app1.app()

elif selected_option == "🔐 Login / Signup":
    app2.app()

elif selected_option == "📬 Grievance":
    app3.app()

elif selected_option == "🌐 Language":
    app4.app()

elif selected_option == "📞 Contact":
    # Contact page content
    st.markdown(f"<h2 style='color:black; font-weight:900;'>{t('Contact Us')}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:black; font-weight:900; font-size:18px;'>{t('📞 Contact us at: 123-456-7890')}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='color:black; font-weight:900; font-size:18px;'>{t('📧 Email: support@example.com')}</p>", unsafe_allow_html=True)
