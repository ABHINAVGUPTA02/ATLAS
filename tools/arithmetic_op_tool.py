import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper

load_dotenv()

@tool
def multiply(a: int, b: int) -> int:
    """
    Multiply two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The product of the two integers.
    """
    return a * b

@tool
def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers.
    """
    return a + b

@tool
def currency_converter(from_curr: str, to_curr: str, value: float)  -> float:
    """
    Convert currency from one type to another using exchange rates.

    Args:
        from_curr (str): The currency code to convert from (e.g., 'USD').
        to_curr (str): The currency code to convert to (e.g., 'EUR').
        value (float): The amount of money to convert.

    Returns:
        float: The converted amount in the target currency.
    """
    os.environ["ALPHAVANTAGE_API_KEY"] = os.getenv('ALPHAVANTAGE_API_KEY')
    alpha_vantage = AlphaVantageAPIWrapper()
    response = alpha_vantage._get_exchange_rate(from_currency=from_curr, to_currency=to_curr)
    exchange_rate = response['Realtime Currency Exchange Rate']['5. Exchange Rate']
    return value * float(exchange_rate)