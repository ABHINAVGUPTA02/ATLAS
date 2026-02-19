import os
from dotenv import load_dotenv
from utils.weather_info import WeatherForecastTool
from typing import List
from langchain.tools import tool


class WeatherInfoTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
        self.weather_service = WeatherForecastTool(self.api_key)
        self.weather_tool_list = self._setup_tool()

    def _setup_tool(self) -> List[tool]:
        """Set up weather information tools."""
        @tool
        def get_current_weather(city:str):
            """
            Get current weather information for a specified city.

            Args:
                city (str): The name of the city to get the weather information for.

            Returns:
                str: A message containing the current weather information for the specified city.
            """
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data:
                temp = weather_data.get("main", {}).get("temp", 'N/A')
                desc = weather_data.get("weather", [{}])[0].get("description", 'N/A')
                return f"The current temperature in {city}: {temp}°C with {desc}."
            return f"Could not retrieve weather data for {city}."

        @tool
        def get_weather_forecast(city: str):
            """
            Get weather forecast information for a specified city.

            Args:
                city (str): The name of the city to get the weather forecast for.

            Returns:
                str: A message containing the weather forecast information for the specified city.
            """
            forecast_data = self.weather_service.get_weather_forecast(city)
            if forecast_data and "list" in forecast_data:
                forecast_summary = []
                for i in range(len(forecast_data['list'])):  # Get first 5 forecasts
                    item = forecast_data['list'][i]
                    date = item['dt_txt'].split(' ')[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    forecast_summary.append(f"{date}: {temp} degree celcius , {desc}")
                return f"Weather forecast for {city}:\n" + "\n".join(forecast_summary)
            return f"Could not fetch forecast for {city}"

        return [get_current_weather,get_weather_forecast]