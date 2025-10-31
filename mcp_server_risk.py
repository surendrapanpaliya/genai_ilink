
from mcp.server.fastmcp import FastMCP
mcp = FastMCP("RiskServer")

@mcp.tool()
def calculate_risk_score(age: int, income: float, liabilities: float) -> str:
    """Return basic financial risk score."""
    ratio = liabilities / income if income else 1
    score = max(0, 100 - (age*0.2 + ratio*50))
    if score > 75: return "Low Risk"
    elif score > 40: return "Moderate Risk"
    else: return "High Risk"

@mcp.tool()
def message_of_the_day() -> str:
    return "Plan your finances before they plan you 💼"

if __name__ == "__main__":
    mcp.run()
