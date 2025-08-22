from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

async def main():
    client = MultiServerMCPClient({
        "maths": {
            "command": "python",
            "args": ["mathserver.py"],
            "transport": "stdio",
        }
    })


    llm = ChatGroq(model="qwen/qwen3-32b")
    tools = await client.get_tools()

    # ✅ Use positional args for latest langgraph
    agent = create_react_agent(llm, tools)

    response = await agent.ainvoke(
        {"messages":[{"role": "user", "content": "what is (3+5)*12"}]})
    print("Response:", response["messages"][-1].content)


asyncio.run(main())



