
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("BankingMCP")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def message_of_the_day() -> str:
    return "Stay curious. Build boldly."

if __name__ == "__main__":
    mcp.run()
