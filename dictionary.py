
from mcp.server.fastmcp import FastMCP
import aiohttp

mcp = FastMCP("DictionaryTool")

@mcp.tool()
async def get_definition(word: str) -> str:
    """
    Fetch the definition of a word using an online dictionary API.
    """
    async with aiohttp.ClientSession() as session:
        resp = await session.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
        data = await resp.json()
        return data[0]['meanings'][0]['definitions'][0]['definition']

if __name__ == "__main__":
    mcp.run(transport="stdio")