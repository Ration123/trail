import streamlit as st

def app(lang_toggle):
    st.title("📝 New Ration Shop Registration")

    st.markdown("""
        If you are a new user and want to register for ration shop services, 
        please fill the form below:
    """)

    st.markdown("""
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSek8ehEkLq3d8dt95Mz_CaOSBcnWYXxoDLpNAL-qpuV3cQXuA/viewform?embedded=true" 
                width="100%" height="1200" frameborder="0" marginheight="0" marginwidth="0">
                Loading…
        </iframe>
    """, unsafe_allow_html=True)
