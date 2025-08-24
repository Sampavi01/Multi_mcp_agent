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
import asyncio

load_dotenv()

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

    # Example 1: Math
    print("\n--- Invoking Agent for Math Question ---")
    math_input = {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    async for chunk in agent.astream(math_input):
        print("--- Next Step ---")
        pprint.pprint(chunk)
        print("\n")

    # Example 2: Weather
    print("\n--- Invoking Agent for Weather Question ---")
    weather_input = {"messages": [{"role": "user", "content": "what is the weather in San Francisco?"}]}
    async for chunk in agent.astream(weather_input):
        print("--- Next Step ---")
        pprint.pprint(chunk)
        print("\n")

    # Example 3: Dictionary
    print("\n--- Invoking Agent for Dictionary Question ---")
    dict_input = {"messages": [{"role": "user", "content": "define artificial intelligence"}]}
    async for chunk in agent.astream(dict_input):
        print("--- Next Step ---")
        pprint.pprint(chunk)
        print("\n")

    # Example 4: Research
    print("\n--- Invoking Agent for Research Question ---")
    research_input = {"messages": [{"role": "user", "content": "summarize top 3 papers on deep reinforcement learning"}]}
    async for chunk in agent.astream(research_input):
        print("--- Next Step ---")
        pprint.pprint(chunk)
        print("\n")


if __name__ == "__main__":
    asyncio.run(main())
