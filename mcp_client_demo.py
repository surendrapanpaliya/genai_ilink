
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(command="python", args=["mcp_server.py"])

    async with stdio_client(params) as (r, w):
        async with ClientSession(r, w) as session:
            await session.initialize()
            tools = await session.list_tools()
            tool_names = [t[0] for t in tools]
            print("Available tools:", tool_names)

            result = await session.call_tool("add", {"a": 7, "b": 8})
            print("add(7,8) =", result.structuredContent.get("result"))

            motd = await session.call_tool("message_of_the_day", {})
            print("message_of_the_day() =", motd.structuredContent.get("result"))

asyncio.run(main())
