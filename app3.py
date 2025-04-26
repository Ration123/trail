import streamlit as st
from utils import set_background, show_title_image, get_translator

def app():
    # Setup
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
        # Check if all required fields are filled
        if full_name and contact_info and message:
            # Here you can save the feedback data to a file or a database
            # For example, saving to Google Sheets, Firebase, or a text file
            
            # For demonstration, we just print the submitted data
            # In actual implementation, you'd store this in a database or file
            st.success(t("Thank you! We received your feedback."))
            st.write(f"Name: {full_name}")
            st.write(f"Contact Info: {contact_info}")
            st.write(f"Message: {message}")
        else:
            st.error(t("Please fill out all fields before submitting."))

if __name__ == "__main__":
    app()
