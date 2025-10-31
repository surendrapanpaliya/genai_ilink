import math
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("LoanEMIServer")

@mcp.tool()
def calculate_emi(principal: float, rate: float, tenure_years: float) -> float:
    """Calculate monthly EMI."""
    r = rate / (12 * 100)
    n = tenure_years * 12
    emi = principal * r * ((1 + r)**n) / ((1 + r)**n - 1)
    return round(emi, 2)

@mcp.tool()
def message_of_the_day() -> str:
    return "Dream big — finance smartly 💡"

if __name__ == "__main__":
    mcp.run()
