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

    # === Chatbot State Initialization ===
    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # === Floating Button with Toggle (No form/refresh) ===
    st.markdown(f"""
        <style>
            .fixed-help-button {{
                position: fixed;
                bottom: 20px;
                right: 20px;
                z-index: 9999;
            }}
            .fixed-help-button button {{
                background-color: #dc3545;
                color: white;
                padding: 10px 16px;
                border: none;
                border-radius: 10px;
                font-size: 16px;
                font-weight: bold;
                display: flex;
                align-items: center;
                gap: 10px;
                cursor: pointer;
            }}
            .fixed-help-button button:hover {{
                background-color: #c82333;
            }}
            .fixed-help-button img {{
                height: 24px;
            }}
        </style>
        <div class="fixed-help-button">
            <button onclick="document.dispatchEvent(new CustomEvent('toggle-chat'))">
                <img src="{tamilnadu_icon_url}" alt="Logo"> HELP BOT
            </button>
        </div>
        <script>
            const docEvent = new EventSource('/_stcore/events');
            document.addEventListener('toggle-chat', function () {{
                window.parent.postMessage({{ type: 'streamlit:rerunScript' }}, '*');
                localStorage.setItem("chat_open", String(!{str(st.session_state.chat_open).lower()}));
            }});
        </script>
    """, unsafe_allow_html=True)

    # Fallback toggle for now — better to replace with Streamlit-native widget:
    chat_toggle = st.checkbox("Show Help Bot", key="chat_toggle")
    st.session_state.chat_open = chat_toggle

    # === Chat UI ===
    if st.session_state.chat_open:
        st.markdown("### 🤖 Help Bot")
        selected_question = st.selectbox("Choose your question:", options=questions, index=0, key="chat_question_select")
        if selected_question != questions[0]:
            st.session_state.chat_history.append(("user", selected_question))
            bot_reply = get_bot_response(selected_question)
            st.session_state.chat_history.append(("bot", bot_reply))

        st.markdown('<div style="max-height: 300px; overflow-y: auto;">', unsafe_allow_html=True)
        for sender, msg in st.session_state.chat_history:
            color = "#0084ff" if sender == "user" else "#e5e5ea"
            align = "right" if sender == "user" else "left"
            text_color = "white" if sender == "user" else "black"
            st.markdown(
                f'<div style="background-color:{color}; color:{text_color}; padding:8px; border-radius:12px; max-width:80%; margin:6px 0; word-wrap: break-word;">{msg}</div>',
                unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
