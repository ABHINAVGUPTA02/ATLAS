import os
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv
from utils.place_info_search import GooglePlaceSearchTool, TavilySearchTool

class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("GPLACES_API_KEY")
        self.google_places_search = GooglePlaceSearchTool(api_key=self.api_key)
        self.tavily_search = TavilySearchTool(api_key=self.api_key)
        self.place_search_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        @tool
        def search_attractions(place: str) -> List:
            try:
                attraction_result = self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions in {place} as suggested by google: {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the attractions of {place}: {tavily_result}"

        @tool
        def search_restaurants(place: str) -> List:
            try:
                restaurant_result = self.google_places_search.google_search_restaurants(place)
                if restaurant_result:
                    return f"Following are the restaurants in {place} as suggested by google: {restaurant_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_restaurants(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the restaurants of {place}: {tavily_result}"
            
        @tool
        def search_activities(place: str) -> List:
            try:
                activity_result = self.google_places_search.google_search_activity(place)
                if activity_result:
                    return f"Following are the activities in {place} as suggested by google: {activity_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the activities of {place}: {tavily_result}" 
            
        @tool
        def search_transportation(place: str) -> List:
            try:
                transportation_result = self.google_places_search.google_search_transportation(place)
                if transportation_result:
                    return f"Following are the transportation options in {place} as suggested by google: {transportation_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the transportation options of {place}: {tavily_result}"

        return [search_attractions, search_restaurants, search_activities, search_transportation]