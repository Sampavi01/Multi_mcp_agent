import os
import sys
import pprint  # pretty-print

# --- Start of the OpenSSL fix (Windows only) ---
if sys.platform == "win32":
    dll_path = os.path.join(sys.prefix, "DLLs")
    if os.path.exists(dll_path):
        os.add_dll_directory(dll_path)
# --- End of the OpenSSL fix ---

from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import asyncio

async def main():
    # Define all 4 servers (all use stdio for consistency)
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["CalcEngineServer.py"],
                "transport": "stdio",
            },
            "weather": {
                "command": "python",
                "args": ["Weather.py"],
                "transport": "stdio",
            },
            "dictionary": {
                "command": "python",
                "args": ["dictionary.py"],
                "transport": "stdio",
            },
            "research": {
                "command": "python",
                "args": ["research_summarizer.py"],
                "transport": "stdio",
            },
        }
    )

    tools = await client.get_tools()
    model = ChatGroq(model="llama3-70b-8192")
    agent = create_react_agent(model, tools)

    print("Type 'exit' to quit.")
    while True:
        user_input = input("\nEnter your query: ").strip()
        if user_input.lower() == "exit":
            break

        query = {"messages": [{"role": "user", "content": user_input}]}
        async for chunk in agent.astream(query):
            # If agent returned a message
            if "agent" in chunk and "messages" in chunk["agent"]:
                for msg in chunk["agent"]["messages"]:
                    print(msg.content)
            # If a tool returned a message
            elif "tools" in chunk and "messages" in chunk["tools"]:
                for msg in chunk["tools"]["messages"]:
                    print(msg.content)


if __name__ == "__main__":
    asyncio.run(main())
