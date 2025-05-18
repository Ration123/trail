import streamlit as st
def chatbot_app():
# Load your Tamil Nadu icon image
 tamilnadu_icon = "/mnt/data/58015941-1cce-47c5-ba49-75c9156123e8.png"

# Initialize chat UI state
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

# Custom CSS for fixed icon and chat box
 st.markdown(
    """
    <style>
    .chat-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        cursor: pointer;
        z-index: 9999;
    }
    .chat-box {
        position: fixed;
        bottom: 90px;
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
    """, unsafe_allow_html=True
)

# Display the Tamil Nadu icon button to open/close chat
 if st.button("", key="chat_toggle", help="Open Chatbot", args=None):
    st.session_state.chat_open = not st.session_state.chat_open

st.markdown(
    f"""
    <img src="{tamilnadu_icon}" 
    class="chat-button" alt="Chat Bot" 
    onclick="document.querySelector('button[kind=primary]').click()"
    style="background-size: cover;">
    """,
    unsafe_allow_html=True,
)


# Show chat box only if toggled
 if st.session_state.chat_open:
    with st.container():
        st.markdown('<div class="chat-box">', unsafe_allow_html=True)

        # Show chat history messages
        for chat in st.session_state.chat_history:
            if chat["sender"] == "user":
                st.markdown(f'<div class="chat-message-user">{chat["message"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-message-bot">{chat["message"]}</div>', unsafe_allow_html=True)

        # Input for user message
        user_input = st.text_input("Ask something...", key="chat_input", label_visibility="collapsed")

        if user_input:
            st.session_state.chat_history.append({"sender": "user", "message": user_input})
            reply = get_bot_response(user_input)
            st.session_state.chat_history.append({"sender": "bot", "message": reply})
            # Clear input by rerun
            

        st.markdown('</div>', unsafe_allow_html=True)
