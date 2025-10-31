
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp import MCPToolkit
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

async def run_emi_agent():
    params = StdioServerParameters(command="python", args=["mcp_server_emi.py"])
    async with stdio_client(params) as (r, w):
        async with ClientSession(r, w) as session:
            await session.initialize()
            toolkit = MCPToolkit(session=session)
            await toolkit.initialize()
            tools = toolkit.get_tools()
            print("Tools:", [t.name for t in tools])

            llm = ChatOpenAI(model="gpt-5", temperature=0)
            agent = create_react_agent(llm, tools)
            result = await agent.ainvoke({
                "messages":[("user","Calculate EMI for ₹5 L loan @ 10% for 3 years and share message of the day.")]
            })
            print("Agent Response:", result["messages"][-1].content)

asyncio.run(run_emi_agent())
