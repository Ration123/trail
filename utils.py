import streamlit as st

# Dummy users and admins
users = {"user1": "pass123", "user2": "pass456"}
admins = {"admin1": "admin123"}

def calculate_price(quantity):
    return (quantity / 100) * 10

def set_background():
    st.markdown("""
        <style>
        html, body, .stApp {
            background-image: url("https://raw.githubusercontent.com/Ration123/RATION/main/GRAIN.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: scroll;
            background-position: center 200px;
            height: 100%;
            width: 100%;
        }
        .block-container {
            background-color: rgba(255, 255, 255, 0.10);
            padding: 2rem;
            border-radius: 20px;
            backdrop-filter: blur(4px);
            margin-top: 40px;
        }
        .stMarkdown, .stTextInput, .stTextArea, .stSelectbox, .stRadio, .stButton {
            color: black !important;
            font-weight: 900 !important;
        }
        input, textarea {
            background-color: rgba(255, 255, 255, 0.85) !important;
            color: black !important;
            font-weight: 900 !important;
        }
        footer, header, .viewerBadge_container__1QSob, .st-emotion-cache-1v0mbdj {
            display: none !important;
        }
        .stApp {
            padding-top: 50px;
        }
        </style>
    """, unsafe_allow_html=True)

def show_title_image():
    st.image("https://raw.githubusercontent.com/Ration123/RATION/main/title", use_container_width=True)

def get_translator(lang):
    def t(text):
        translations = {
            "Home": "முகப்பு",
            "Welcome to Tamil Nadu Ration Shop Portal": "தமிழ்நாடு ரேஷன் கடை போர்டல் வரவேற்கிறது!",
            "- Track shop stock": "- கடை பொருள் இருப்பை பின்தொடர்",
            "- Submit complaints": "- புகார் அளிக்க",
            "- Place orders & track status": "- ஆர்டரை இட & நிலையை பின்தொடர",
            "Real-Time Stock": "நிகழ்நேர பொருள் நிலை",
            "Select Shop": "கடையைத் தேர்ந்தெடுக்கவும்",
            "Current Stock Levels": "தற்போதைய இருப்பு நிலை",
            "Login as:": "உள்நுழைவு பயனராக:",
            "User": "பயனர்",
            "Admin": "நிர்வாகி",
            "Username": "பயனர் பெயர்",
            "Password": "கடவுச்சொல்",
            "Login": "உள்நுழை",
            "Welcome": "வரவேற்கின்றோம்",
            "Card Type: APL": "அட்டை வகை: APL",
            "🧾 Order Status: Received this month ✔️": "🧾 ஆர்டர் நிலை: இந்த மாதம் பெற்றது ✔️",
            "🧾 Order Status: Not received this month ": "🧾 ஆர்டர் நிலை: இந்த மாதம் பெறப்படவில்லை ",
            "💸 Pay via GPay: UPI@gov": "💸 GPay வழியாக செலுத்த: UPI@gov",
            "Place Order": "ஆர்டர் இடு",
            "Login Portal": "உள்நுழைவு போர்டல்",
            "Submit Complaint or Feedback": "புகார் அல்லது கருத்தை சமர்ப்பிக்கவும்",
            "Full Name": "முழுப் பெயர்",
            "Contact Email / Phone": "தொடர்பு மின்னஞ்சல் / தொலைபேசி",
            "Your Message": "உங்கள் செய்தி",
            "Thank you! We received your feedback.": "நன்றி! உங்கள் கருத்தை பெற்றோம்.",
            "Language Switcher": "மொழி மாற்று",
            "Use the checkbox in the sidebar to toggle between Tamil and English.": "தமிழ் மற்றும் ஆங்கிலத்தை மாற்ற பக்கப்பட்டி பெட்டியைப் பயன்படுத்தவும்.",
            "Enter quantity of rice (in grams)": "அரிசி அளவை உள்ளிடவும் (கிராம்களில்)",
            "Total Amount": "மொத்த தொகை"
            
        }
        return translations.get(text, text) if lang else text
    return t
