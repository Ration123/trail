import streamlit as st

def chatbot_app():
    # Tamil Nadu logo icon URL
    tamilnadu_icon_url = "https://raw.githubusercontent.com/Ration123/trail/main/TamilNadu_Logo.svg.png"
    mic_icon_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Microphone_icon.svg/2048px-Microphone_icon.svg.png"  # Replace with your preferred mic icon

    # Initialize session state
    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Bot logic
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
            return "Sorry, I didn't understand that. Please ask something else."

    # --- Custom CSS ---
    st.markdown(f"""
        <style>
        .help-bot-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 10px;
        }}
        .mic-icon {{
            width: 40px;
            height: 40px;
            margin-top: 5px;
            cursor: pointer;
        }}
        .help-label {{
            font-size: 12px;
            color: #444;
            text-align: center;
        }}
        .chat-box {{
            position: fixed;
            top: 120px;
            left: 20px;
            width: 320px;
            max-height: 400px;
            background: #f9f9f9;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            border-radius: 10px;
            padding: 10px;
            overflow-y: auto;
            font-family: Arial, sans-serif;
            z-index: 9998;
            display: flex;
            flex-direction: column;
        }}
        .chat-message-user {{
            background-color: #0084ff;
            color: white;
            padding: 8px 12px;
            border-radius: 12px;
            margin: 6px 0;
            align-self: flex-end;
            max-width: 80%;
            word-wrap: break-word;
        }}
        .chat-message-bot {{
            background-color: #e5e5ea;
            color: black;
            padding: 8px 12px;
            border-radius: 12px;
            margin: 6px 0;
            align-self: flex-start;
            max-width: 80%;
            word-wrap: break-word;
        }}
        </style>
    """, unsafe_allow_html=True)

    # --- Top Row Layout ---

    # Toggle button (hidden)
    chat_toggle = st.button(" ", key="toggle", help="Toggle Chatbot")
    if chat_toggle:
        st.session_state.chat_open = not st.session_state.chat_open

    # Chat Window
    if st.session_state.chat_open:
        st.markdown('<div class="chat-box">', unsafe_allow_html=True)

        # Chat history
        for chat in st.session_state.chat_history:
            role_class = "chat-message-user" if chat["sender"] == "user" else "chat-message-bot"
            st.markdown(f'<div class="{role_class}">{chat["message"]}</div>', unsafe_allow_html=True)

        # Dropdown for questions (no floating input at bottom)
        question = st.selectbox("Quick Help", ["", "How to check stock?", "How to login as user?", "How to place order?", "How to submit grievance?"], key="chat_select")
        if question and question.strip() != "":
            st.session_state.chat_history.append({"sender": "user", "message": question})
            reply = get_bot_response(question)
            st.session_state.chat_history.append({"sender": "bot", "message": reply})
            st.experimental_rerun()

        st.markdown('</div>', unsafe_allow_html=True)
