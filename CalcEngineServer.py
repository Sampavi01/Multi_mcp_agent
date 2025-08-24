from mcp.server.fastmcp import FastMCP
import aiohttp
import os

mcp = FastMCP("AdvancedMath")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def percentage_of(part: float, whole: float) -> float:
    """Calculate what percentage 'part' is of 'whole'"""
    if whole == 0:
        return 0
    return (part / whole) * 100

@mcp.tool()
async def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """
    Convert currency using ExchangeRate API
    Free endpoint: https://api.exchangerate.host
    """
    url = f"https://api.exchangerate.host/convert?from={from_currency.upper()}&to={to_currency.upper()}&amount={amount}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return f"Failed to fetch conversion. Status code: {resp.status}"
            data = await resp.json()
            result = data.get("result")
            if result is None:
                return "Conversion failed."
            return f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
