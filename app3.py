import streamlit as st
from utils import set_background, show_title_image, get_translator

def app():
    # Setup
    st.set_page_config(page_title="Grievance", layout="wide")
    set_background()
    lang_toggle = st.sidebar.checkbox("Switch to Tamil")
    t = get_translator(lang_toggle)

    # Display the title image and header
    show_title_image()
    st.header(t("Submit Complaint or Feedback"))

    # Input fields for grievance submission
    full_name = st.text_input(t("Full Name"))
    contact_info = st.text_input(t("Contact Email / Phone"))
    message = st.text_area(t("Your Message"))

    # Submit button logic
    if st.button(t("Submit")):
        st.success(t("Thank you! We received your feedback."))
if __name__ == "__main__":
    app()
