from utils.expense_calculator import Calculator
from typing import List
from langchain.tools import tool

class ExpenseCalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.expense_calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        @tool
        def estimate_total_hotel_cost(price_per_night: float, total_days: int) -> float:
            """
            Calculate the total hotel cost based on price per night and number of days.
            
            Args:
                price_per_night (float): The cost of the hotel room per night.
                total_days (int): The total number of nights staying at the hotel.
            
            Returns:
                float: The total hotel cost for the entire stay.
            """
            return self.calculator.multiply(price_per_night, total_days)

        @tool
        def calculate_total_expenses(*expenses: float) -> float:
            """
            Calculate the sum of all travel expenses.
            
            Args:
                *expenses (float): Variable number of expense amounts to sum up (e.g., hotel, food, transport, activities).
            
            Returns:
                float: The total sum of all provided expenses.
            """
            return self.calculator.calculate_total(*expenses)
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, total_days: int) -> float:
            """
            Calculate the daily budget by dividing total cost by number of days.
            
            Args:
                total_cost (float): The total budget or cost for the trip.
                total_days (int): The total number of days for the trip.
            
            Returns:
                float: The daily budget amount.
            """
            return self.calculator.calculate_daily_budget(total_cost, total_days)

        return [estimate_total_hotel_cost, calculate_total_expenses, calculate_daily_expense_budget]