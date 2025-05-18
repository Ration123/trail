import streamlit as st

def chatbot_app():
    # Tamil Nadu logo icon URL (small image hosted on GitHub)
    tamilnadu_icon_url = "https://raw.githubusercontent.com/Ration123/trail/main/TamilNadu_Logo.svg.png"

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
    st.markdown("""
        <style>
        .chat-button {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-image: url('""" + tamilnadu_icon_url + """');
            background-size: cover;
            background-position: center;
            border: none;
            cursor: pointer;
            z-index: 9999;
        }
        .chat-box {
            position: fixed;
            bottom: 80px;
            right: 20px;
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
        }
        .chat-message-user {
            background-color: #0084ff;
            color: white;
            padding: 8px 12px;
            border-radius: 12px;
            margin: 6px 0;
            align-self: flex-end;
            max-width: 80%;
            word-wrap: break-word;
        }
        .chat-message-bot {
            background-color: #e5e5ea;
            color: black;
            padding: 8px 12px;
            border-radius: 12px;
            margin: 6px 0;
            align-self: flex-start;
            max-width: 80%;
            word-wrap: break-word;
        }
        </style>
    """, unsafe_allow_html=True)

    # Hidden button to toggle chat
    chat_toggle = st.button(" ", key="toggle", help="Toggle Chatbot")
    if chat_toggle:
        st.session_state.chat_open = not st.session_state.chat_open

    # Floating chatbot icon
    st.markdown(f"""
        <div class="chat-button" onclick="document.querySelector('button[kind=primary]').click()"></div>
    """, unsafe_allow_html=True)

    # Show chat UI if open
    if st.session_state.chat_open:
        st.markdown('<div class="chat-box">', unsafe_allow_html=True)

        # Chat history
        for chat in st.session_state.chat_history:
            role_class = "chat-message-user" if chat["sender"] == "user" else "chat-message-bot"
            st.markdown(f'<div class="{role_class}">{chat["message"]}</div>', unsafe_allow_html=True)

        # Chat input
        user_input = st.selectbox("Ask something...", ["", "How to check stock?", "How to login as user?", "How to place order?", "How to submit grievance?"], key="chat_select")
        if user_input and user_input.strip() != "":
            st.session_state.chat_history.append({"sender": "user", "message": user_input})
            reply = get_bot_response(user_input)
            st.session_state.chat_history.append({"sender": "bot", "message": reply})
              # Clear input by rerunning

        st.markdown('</div>', unsafe_allow_html=True)
