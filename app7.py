import streamlit as st

def chatbot_app():
    st.markdown(
        """
        <style>
        .chat-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 300px;
            max-height: 400px;
            background-color: #f1f1f1;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            padding: 10px;
            overflow-y: auto;
            font-family: Arial, sans-serif;
            z-index: 1000;
        }
        .user-msg {
            background-color: #0084ff;
            color: white;
            padding: 8px 12px;
            border-radius: 12px;
            margin: 6px 0;
            max-width: 80%;
            align-self: flex-end;
        }
        .bot-msg {
            background-color: #e5e5ea;
            color: black;
            padding: 8px 12px;
            border-radius: 12px;
            margin: 6px 0;
            max-width: 80%;
            align-self: flex-start;
        }
        .chat-messages {
            display: flex;
            flex-direction: column;
            max-height: 320px;
            overflow-y: auto;
        }
        </style>
        """, unsafe_allow_html=True)

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    def get_bot_response(user_input):
        user_input = user_input.lower()
        if "stock" in user_input:
            return "You can check stock availability in the 'Stock Availability' section."
        elif "login" in user_input and "user" in user_input:
            return "User Login lets you access your personal ration account."
        elif "login" in user_input and "admin" in user_input:
            return "Admin Login is for authorized personnel to manage the portal."
        elif "order" in user_input:
            return "Place orders after logging in as a user."
        elif "grievance" in user_input or "complaint" in user_input:
            return "Submit complaints in the 'Grievance' section."
        elif "language" in user_input:
            return "Switch language using the toggle in the sidebar."
        elif "contact" in user_input:
            return "Contact details are under the 'Contact' section."
        else:
            return "Sorry, I didn't understand that. Please ask something else."

    # Layout container for the chat
    chat_container = st.container()
    with chat_container:
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)

        # Display chat messages
        for chat in st.session_state.chat_history:
            if chat['sender'] == 'user':
                st.markdown(f'<div class="user-msg">{chat["message"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="bot-msg">{chat["message"]}</div>', unsafe_allow_html=True)

        # Input box for user message
        user_input = st.text_input("You:", key="chat_input", label_visibility="collapsed")

        if user_input:
            st.session_state.chat_history.append({"sender": "user", "message": user_input})
            bot_reply = get_bot_response(user_input)
            st.session_state.chat_history.append({"sender": "bot", "message": bot_reply})

            # Clear input box after submission
            st.experimental_rerun()

        st.markdown('</div>', unsafe_allow_html=True)
