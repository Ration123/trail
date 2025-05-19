import streamlit as st
from utils import set_background, get_translator

def app(lang_toggle):
    set_background()
    t = get_translator(lang_toggle)

    st.title(t("📝 New Ration Shop Registration"))

    st.markdown(t("""
        If you are a new user and want to register for ration shop services, 
        please fill the form below:
    """))

    st.markdown("""
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSek8ehEkLq3d8dt95Mz_CaOSBcnWYXxoDLpNAL-qpuV3cQXuA/viewform?embedded=true" 
                width="100%" height="1400" frameborder="0" marginheight="0" marginwidth="0">
                Loading…
        </iframe>
    """, unsafe_allow_html=True)
