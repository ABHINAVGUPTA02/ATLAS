from utils.expense_calculator import Calculator
from typing import List
from langchain.tools import tool

class ExpenseCalculatorTool:
    def __init__(self):
        self.calculator = Calculator()
        self.expense_calculator_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        @tool
        def estimate_total_hotel_cost(price_per_night: str, total_days: float) -> float:
            return self.calculator.multiply(price_per_night, total_days)

        @tool
        def calculate_total_expenses(*expenses: float) -> float:
            return self.calculator.calculate_total(*expenses)
        
        @tool
        def calculate_daily_expense_budget(total_cost: float, total_days: int) -> float:
            return self.calculator.calculate_daily_budget(total_cost, total_days)

        return [estimate_total_hotel_cost, calculate_total_expenses, calculate_daily_expense_budget]
