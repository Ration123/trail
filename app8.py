# app7.py
import streamlit as st

def app(lang_toggle):
    st.title("📝 New Ration Card Registration")
    st.markdown("Please fill out the form below:")

    st.markdown("""
    <iframe src="https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform?embedded=true" 
    width="700" height="800" frameborder="0" marginheight="0" marginwidth="0">
    Loading…
    </iframe>
    """, unsafe_allow_html=True)
