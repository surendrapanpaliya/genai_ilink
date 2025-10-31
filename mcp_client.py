
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    params = StdioServerParameters(command="python", args=["mcp_server.py"])

    async with stdio_client(params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools = await session.list_tools()
            # Each entry is (name, schema_dict)
            tool_names = [t[0] for t in tools]
            print("Available tools:", tool_names)

            # Call a tool
            motd = await session.call_tool("message_of_the_day", {})
            print("message_of_the_day() =", motd.structuredContent.get("result"))

            result = await session.call_tool("add", {"a": 10, "b": 5})
            print("add(10,5) =", result.structuredContent.get("result"))

asyncio.run(main())
