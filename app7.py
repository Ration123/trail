import streamlit as st

def chatbot_app():
    # Tamil Nadu logo icon URL
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

    # Custom CSS + JS for draggable chat box + button fixed bottom right
    st.markdown(f"""
    <style>
        /* HELP BOT button fixed bottom right */
        #help-bot-button {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #0084ff;
            color: white;
            border: none;
            border-radius: 30px;
            padding: 8px 16px;
            font-weight: bold;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            z-index: 10000;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            user-select: none;
        }}
        #help-bot-button img {{
            height: 24px;
            width: 24px;
            object-fit: contain;
        }}

        /* Draggable chat box */
        #chat-box {{
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
            user-select: none;
        }}

        /* Header for drag */
        #chat-header {{
            background-color: #0084ff;
            color: white;
            padding: 8px 12px;
            border-radius: 8px 8px 0 0;
            cursor: move;
            font-weight: bold;
        }}

        /* Chat messages */
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

    <button id="help-bot-button" title="Toggle Help Bot" aria-label="Toggle Help Bot">
        <img src="{tamilnadu_icon_url}" alt="TN Logo" />
        HELP BOT
    </button>

    <div id="chat-box" style="display:none;">
        <div id="chat-header">Help Bot</div>
        <div id="chat-content"></div>
        <div id="chat-input-area" style="margin-top:8px;">
            <select id="chat-select" style="width: 100%; padding: 6px; border-radius: 6px; border: 1px solid #ccc;">
                <option value="">Quick Help</option>
                <option value="How to check stock?">How to check stock?</option>
                <option value="How to login as user?">How to login as user?</option>
                <option value="How to place order?">How to place order?</option>
                <option value="How to submit grievance?">How to submit grievance?</option>
            </select>
            <button id="chat-send" style="margin-top:6px; width: 100%; padding: 6px; background:#0084ff; color:white; border:none; border-radius:6px; cursor:pointer;">Ask</button>
        </div>
    </div>

    <script>
        const btn = document.getElementById("help-bot-button");
        const chatBox = document.getElementById("chat-box");
        const chatHeader = document.getElementById("chat-header");
        const chatContent = document.getElementById("chat-content");
        const chatSelect = document.getElementById("chat-select");
        const chatSend = document.getElementById("chat-send");

        // Toggle chat box display
        btn.onclick = () => {{
            if (chatBox.style.display === "none") {{
                chatBox.style.display = "flex";
            }} else {{
                chatBox.style.display = "none";
            }}
        }};

        // Simple bot responses in JS (mirror Python logic)
        function getBotResponse(msg) {{
            msg = msg.toLowerCase();
            if (msg.includes("stock")) {{
                return "You can check stock availability in the 'Stock Availability' section.";
            }} else if (msg.includes("login") && msg.includes("user")) {{
                return "User Login lets you access your personal ration account.";
            }} else if (msg.includes("login") && msg.includes("admin")) {{
                return "Admin Login is for authorized personnel to manage the portal.";
            }} else if (msg.includes("order")) {{
                return "Place orders after logging in as a user.";
            }} else if (msg.includes("grievance") || msg.includes("complaint")) {{
                return "Submit complaints in the 'Grievance' section.";
            }} else if (msg.includes("language")) {{
                return "Switch language using the toggle in the sidebar.";
            }} else if (msg.includes("contact")) {{
                return "Contact details are under the 'Contact' section.";
            }} else {{
                return "Sorry, I didn't understand that. Please ask something else.";
            }}
        }}

        // Add message to chat window
        function addMessage(sender, message) {{
            const div = document.createElement("div");
            div.className = sender === "user" ? "chat-message-user" : "chat-message-bot";
            div.textContent = message;
            chatContent.appendChild(div);
            chatContent.scrollTop = chatContent.scrollHeight;
        }}

        // Send message handler
        chatSend.onclick = () => {{
            const question = chatSelect.value;
            if (!question) return;
            addMessage("user", question);
            const reply = getBotResponse(question);
            setTimeout(() => {{
                addMessage("bot", reply);
            }}, 300);
            chatSelect.value = "";
        }};

        // Drag functionality
        let isDragging = false;
        let offsetX, offsetY;

        chatHeader.addEventListener("mousedown", function(e) {{
            isDragging = true;
            offsetX = e.clientX - chatBox.getBoundingClientRect().left;
            offsetY = e.clientY - chatBox.getBoundingClientRect().top;
            document.body.style.userSelect = "none";
        }});

        document.addEventListener("mouseup", function() {{
            isDragging = false;
            document.body.style.userSelect = "auto";
        }});

        document.addEventListener("mousemove", function(e) {{
            if (!isDragging) return;
            let left = e.clientX - offsetX;
            let top = e.clientY - offsetY;

            // Clamp position within viewport
            left = Math.min(window.innerWidth - chatBox.offsetWidth, Math.max(0, left));
            top = Math.min(window.innerHeight - chatBox.offsetHeight, Math.max(0, top));

            chatBox.style.left = left + "px";
            chatBox.style.top = top + "px";
            chatBox.style.bottom = "auto";
            chatBox.style.right = "auto";
        }});
    </script>
    """, unsafe_allow_html=True)


chatbot_app()
