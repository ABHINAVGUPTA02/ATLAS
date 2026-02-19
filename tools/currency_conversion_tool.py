import os
from dotenv import load_dotenv
from typing import List
import tools
from langchain.tools import tool   
from utils.currency_converter import CurrencyConverter

class CurrencyConverterTool:
    def __init__(self,):
        load_dotenv()
        self.api_key = os.environ.get("EXCHANGE_RATE_API_KEY")
        self.currency_service = CurrencyConverter(self.api_key)
        self.currency_converter_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        @tool
        def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
            return self.currency_service.convert(amount, from_currency, to_currency)

        return [convert_currency]
