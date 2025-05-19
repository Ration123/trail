import streamlit as st

def app(lang_toggle):
    st.set_page_config(page_title="New Ration Shop Registration", page_icon="📝")

    st.title("📝 New Ration Shop Registration")
    st.markdown("""
        Welcome to the Ration Shop Registration Page.  
        Please fill out the form below to apply for a new ration shop registration.  
        Ensure all details are correct before submitting.
    """)

    # Replace this URL with your actual Google Form link
    google_form_url = "https://docs.google.com/forms/d/e/1FAIpQLSdXXXXXXXXXXXXXXX/viewform?embedded=true"

    # Embed the form using iframe
    st.components.v1.html(
        f"""
        <iframe src="{google_form_url}" width="100%" height="900" frameborder="0" marginheight="0" marginwidth="0">
        Loading…
        </iframe>
        """,
        height=950,
    )


