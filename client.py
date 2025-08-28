import os
import sys
import asyncio
from dotenv import load_dotenv
import streamlit as st

# --- OpenSSL fix for Windows ---
if sys.platform == "win32":
    dll_path = os.path.join(sys.prefix, "DLLs")
    if os.path.exists(dll_path):
        os.add_dll_directory(dll_path)
# -------------------------------

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

load_dotenv()

# --- Initialize MCP client and agent ---
async def init_agent():
    client = MultiServerMCPClient(
        {
            "math": {"command": "python", "args": ["CalcEngineServer.py"], "transport": "stdio"},
            "weather": {"command": "python", "args": ["Weather.py"], "transport": "stdio"},
            "dictionary": {"command": "python", "args": ["dictionary.py"], "transport": "stdio"},
            "research": {"command": "python", "args": ["research_summarizer.py"], "transport": "stdio"},
        }
    )
    tools = await client.get_tools()
    model = ChatGroq(model="llama3-70b-8192")
    agent = create_react_agent(model, tools)
    return agent

# --- Async function to get AI answer ---
async def get_answer(agent, user_input):
    query = {"messages": [{"role": "user", "content": user_input}]}
    final_answer = ""
    async for chunk in agent.astream(query):
        if "agent" in chunk and chunk["agent"]["messages"]:
            msg = chunk["agent"]["messages"][-1]  # AIMessage object
            if hasattr(msg, "content") and msg.content.strip():
                final_answer = msg.content
    return final_answer

# --- Streamlit UI ---
st.set_page_config(page_title="MCP Chat", page_icon="🤖", layout="centered")
st.markdown(
    """
    <style>
    body { background-color: #000000; color: #ffffff; }
    .stTextInput>div>div>input { background-color: #222222; color: #ffffff; }
    .chat-box { max-height: 500px; overflow-y: auto; padding: 10px; border-radius: 10px; }
    .user-msg { background-color: #111111; color: #00ff00; padding: 10px; border-radius: 10px; margin-bottom: 5px; }
    .ai-msg { background-color: #222222; color: #00ffff; padding: 10px; border-radius: 10px; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True
)

st.title("🌟 MCP Multi-Agent Chat ")

# Initialize agent
if "agent_obj" not in st.session_state:
    st.session_state.agent_obj = asyncio.run(init_agent())

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- Continuous chatbot input ---
user_input = st.chat_input("Enter your query...")

if user_input:
    # Append user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Get AI answer
    with st.spinner("🤖 Thinking..."):
        answer = asyncio.run(get_answer(st.session_state.agent_obj, user_input))
    st.session_state.chat_history.append({"role": "ai", "content": answer})
    st.rerun()

# Display chat history
if st.session_state.chat_history:
    st.markdown("### 💬 Chat History")
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"<div class='user-msg'>👤 You: {msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='ai-msg'>🤖 AI: {msg['content']}</div>", unsafe_allow_html=True)
    
    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []
        st.rerun()
else:
    st.info("💡 Start a conversation by typing a message below!")
