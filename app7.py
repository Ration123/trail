import streamlit as st

def chatbot_app():
    tamilnadu_icon_url = "https://raw.githubusercontent.com/Ration123/trail/main/TamilNadu_Logo.svg.png"
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

    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "reset_selectbox" not in st.session_state:
        st.session_state.reset_selectbox = False

    # Fixed-position button style and logic
    st.markdown(f"""
        <style>
        .helpbot-container {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 1000;
        }}
        .helpbot-button {{
            background-color: #1e1e2f;
            color: white;
            padding: 10px 18px;
            border: none;
            border-radius: 12px;
            font-weight: 600;
            display: flex;
            align-items: center;
            cursor: pointer;
        }}
        .helpbot-button img {{
            height: 24px;
            margin-right: 8px;
        }}
        </style>
        <div class="helpbot-container">
            <button class="helpbot-button" onclick="window.location.reload();">
                <img src="{tamilnadu_icon_url}" alt="Logo"> HELP BOT
            </button>
        </div>
    """, unsafe_allow_html=True)

    # Logic toggle on rerun (workaround: click resets page and toggles state)
    if st.button("Toggle Help Bot", key="toggle_helpbot"):
        st.session_state.chat_open = not st.session_state.chat_open

    if st.session_state.chat_open:
        selected_question = st.selectbox("Choose your question:", options=questions, index=0, key="chat_question_select")
        if selected_question != questions[0]:
            st.session_state.chat_history.append(("user", selected_question))
            bot_reply = get_bot_response(selected_question)
            st.session_state.chat_history.append(("bot", bot_reply))
            st.session_state.reset_selectbox = True
            

        st.markdown('<div style="max-height: 300px; overflow-y: auto;">', unsafe_allow_html=True)
        for sender, msg in st.session_state.chat_history:
            color = "#0084ff" if sender == "user" else "#e5e5ea"
            align = "right" if sender == "user" else "left"
            text_color = "white" if sender == "user" else "black"
            st.markdown(
                f'<div style="background-color:{color}; color:{text_color}; padding:8px; border-radius:12px; max-width:80%; margin:6px 0; word-wrap: break-word;">{msg}</div>',
                unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    chatbot_app()
