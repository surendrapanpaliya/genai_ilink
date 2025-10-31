
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_client():
    params = StdioServerParameters(command="python", args=["mcp_server.py"])
    async with stdio_client(params) as (r, w):
        async with ClientSession(r, w) as session:
            await session.initialize()
            tools = await session.list_tools()
            print("Available tools:", [t[0] for t in tools])
            result = await session.call_tool("add", {"a": 10, "b": 20})
            print("Result:", result.structuredContent.get("result"))

asyncio.run(test_client())
