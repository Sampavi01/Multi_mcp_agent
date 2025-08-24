from mcp.server.fastmcp import FastMCP
import aiohttp
import os
from dotenv import load_dotenv
load_dotenv()
# Get your OpenWeatherMap API key from environment variables for safety
API_KEY = os.getenv("OPENWEATHER_API_KEY")

mcp = FastMCP("WeatherTool")

@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Fetch live weather information for a given location using OpenWeatherMap API.
    """
    if not API_KEY:
        return "Error: OpenWeatherMap API key not set. Please set OPENWEATHER_API_KEY in your environment."

    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return f"Could not fetch weather for {location}. Error code: {resp.status}"
            data = await resp.json()
            
            weather = data['weather'][0]['description'].capitalize()
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']

            return (
                f"Weather in {location}: {weather}, "
                f"Temperature: {temp}°C, Feels like: {feels_like}°C, "
                f"Humidity: {humidity}%"
            )

if __name__ == "__main__":
    mcp.run(transport="stdio")  
