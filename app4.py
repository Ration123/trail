import streamlit as st
from utils import set_background, show_title_image, get_translator

# Setup
st.set_page_config(page_title="Grievance", layout="wide")
set_background()
lang_toggle = st.sidebar.checkbox("Switch to Tamil")
t = get_translator(lang_toggle)

show_title_image()
st.header(t("Submit Complaint or Feedback"))

st.text_input(t("Full Name"))
st.text_input(t("Contact Email / Phone"))
st.text_area(t("Your Message"))
if st.button(t("Submit")):
    st.success(t("Thank you! We received your feedback."))
