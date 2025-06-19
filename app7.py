import streamlit as st

def chatbot_app():
    questions = [
        "Select a question...",
        "How to check stock availability?",
        "How to login as user?",
        "How to login as admin?",
        "How to place an order?",
        "How to submit a grievance?",
        "How to switch language?",
        "How to contact support?",
    ]

    def get_bot_response(msg):
        msg = msg.lower()
        if "stock" in msg:
            return "You can check stock availability in the 'Stock Availability' section."
        elif "login" in msg and "user" in msg:
            return "User Login lets you access your personal ration account."
        elif "login" in msg and "admin" in msg:
            return "Admin Login is for authorized personnel to manage the portal."
        elif "order" in msg:
            return "Place orders after logging in as a user."
        elif "grievance" in msg or "complaint" in msg:
            return "Submit complaints in the 'Grievance' section."
        elif "language" in msg:
            return "Switch language using the toggle in the sidebar."
        elif "contact" in msg:
            return "Contact details are under the 'Contact' section."
        else:
            return "Sorry, I didn't understand that. Please select another question."

    # State tracking
    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Floating styled Streamlit button (no HTML form)
    st.markdown("""
        <style>
            div.stButton > button#helpbot-btn {
                position: fixed;
                bottom: 20px;
                right: 20px;
                z-index: 1000;
                background-color: #dc3545;
                color: white;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 16px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.3);
            }
        </style>
    """, unsafe_allow_html=True)

    if st.button("HELP BOT", key="helpbot-btn"):
        st.session_state.chat_open = not st.session_state.chat_open

    # Chat interface
    if st.session_state.chat_open:
        st.markdown("### 🤖 Help Bot")
        selected_question = st.selectbox("Choose your question:", options=questions, index=0, key="chat_q")
        if selected_question != questions[0]:
            st.session_state.chat_history.append(("user", selected_question))
            st.session_state.chat_history.append(("bot", get_bot_response(selected_question)))

        st.markdown('<div style="max-height: 300px; overflow-y: auto;">', unsafe_allow_html=True)
        for sender, msg in st.session_state.chat_history:
            color = "#0084ff" if sender == "user" else "#e5e5ea"
            text_color = "white" if sender == "user" else "black"
            st.markdown(
                f'<div style="background-color:{color}; color:{text_color}; padding:8px; border-radius:12px; max-width:80%; margin:6px 0;">{msg}</div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
