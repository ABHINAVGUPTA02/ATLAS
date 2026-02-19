import os
from dotenv import load_dotenv
from typing import List
from langchain.tools import tool   
from utils.currency_converter import CurrencyConverter

class CurrencyConverterTool:
    def __init__(self):
        load_dotenv()
        self.api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
        self.currency_service = CurrencyConverter(self.api_key)
        self.currency_converter_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        @tool
        def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
            """
            Convert an amount from one currency to another using real-time exchange rates.
            
            Args:
                amount (float): The amount of money to convert.
                from_currency (str): The source currency code (e.g., 'USD', 'EUR', 'INR').
                to_currency (str): The target currency code (e.g., 'USD', 'EUR', 'INR').
            
            Returns:
                float: The converted amount in the target currency.
            """
            return self.currency_service.convert(amount, from_currency, to_currency)

        return [convert_currency]