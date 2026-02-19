import os
import requests
from dotenv import load_dotenv

load_dotenv()

class WeatherForecastTool:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("OPENWEATHERMAP_API_KEY")
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def get_current_weather(self, city: str) -> dict:
        """
        Get current weather for a city.
        
        Args:
            city (str): The name of the city.
        
        Returns:
            dict: Weather data or None if request fails.
        """
        try:
            url = f"{self.base_url}/weather"
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error fetching current weather: {e}")
            return None

    def get_weather_forecast(self, city: str) -> dict:
        """
        Get 5-day weather forecast for a city.
        
        Args:
            city (str): The name of the city.
        
        Returns:
            dict: Forecast data or None if request fails.
        """
        try:
            url = f"{self.base_url}/forecast"
            params = {
                "q": city,
                "appid": self.api_key,
                "units": "metric"
            }
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            return None
        except Exception as e:
            print(f"Error fetching weather forecast: {e}")
            return None