import streamlit as st

def chatbot_app():
    # Tamil Nadu logo URL
    tamilnadu_icon_url = "https://raw.githubusercontent.com/Ration123/trail/main/TamilNadu_Logo.svg.png"

    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

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

    # CSS styles
    st.markdown(
        """
        <style>
        .fixed-helpbot {
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 9999;
            display: flex;
            align-items: center;
            gap: 8px;
            background-color: #0084ff;
            border-radius: 30px;
            padding: 8px 16px;
            color: white;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            user-select: none;
        }
        .fixed-helpbot img {
            height: 24px;
            width: 24px;
        }
        .chat-box-container {
            position: fixed;
            bottom: 70px;
            right: 20px;
            width: 320px;
            max-height: 400px;
            background: #f9f9f9;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
            border-radius: 10px;
            padding: 10px;
            overflow-y: auto;
            font-family: Arial, sans-serif;
            z-index: 9999;
            display: flex;
            flex-direction: column;
        }
        .chat-header {
            background-color: #0084ff;
            color: white;
            padding: 8px 12px;
            border-radius: 8px 8px 0 0;
            font-weight: bold;
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
        """,
        unsafe_allow_html=True,
    )

    # HELP BOT button fixed bottom right
    # We use st.button with a unique key and toggle state
    if st.button(
        f'<img src="{tamilnadu_icon_url}" style="height:24px;width:24px;margin-right:8px;">HELP BOT',
        key="unique_helpbot_button",
        help="Click to open/close chat",
        args=None,
        kwargs=None,
        on_click=None,
        disabled=False,
        type="secondary",
    ):
        st.session_state.chat_open = not st.session_state.chat_open

    # Show chat box if open
    if st.session_state.chat_open:
        chat_container = st.container()
        with chat_container:
            st.markdown('<div class="chat-box-container">', unsafe_allow_html=True)
            st.markdown('<div class="chat-header">Help Bot</div>', unsafe_allow_html=True)

            # Show chat messages
            for sender, message in st.session_state.chat_history:
                cls = "chat-message-user" if sender == "user" else "chat-message-bot"
                st.markdown(f'<div class="{cls}">{message}</div>', unsafe_allow_html=True)

            # Input text box and button in a form for better state control
            with st.form(key="chat_form", clear_on_submit=True):
                user_input = st.text_input("Your question:", placeholder="Ask me anything...", key="chat_input")
                submitted = st.form_submit_button("Send")
                if submitted and user_input.strip():
                    st.session_state.chat_history.append(("user", user_input))
                    response = get_bot_response(user_input)
                    st.session_state.chat_history.append(("bot", response))
                    # No need to call st.experimental_rerun(), form submit reruns automatically

            st.markdown("</div>", unsafe_allow_html=True)


chatbot_app()
