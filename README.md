
class BudgetPlanner:
    def __init__(self):
        self.monthly_income = 0
        self.monthly_expenses = {}

    def add_monthly_income(self, amount):
        self.monthly_income += amount

    def add_monthly_expense(self, category, amount):
        if category in self.monthly_expenses:
            self.monthly_expenses[category] += amount
        else:
            self.monthly_expenses[category] = amount

    def calculate_savings(self):
        total_expenses = sum(self.monthly_expenses.values())
        savings = self.monthly_income - total_expenses
        return savings

    def get_monthly_income(self):
        return self.monthly_income

    def get_monthly_expenses(self):
        return self.monthly_expenses

    def get_savings(self):
        return self.calculate_savings()

    def get_total_expenses(self):
        return sum(self.monthly_expenses.values())

    def get_remaining_income(self):
        return self.monthly_income - self.get_total_expenses()

    def get_expense_percentage(self, category):
        total_expenses = sum(self.monthly_expenses.values())
        if total_expenses == 0:
            return 0

       return (self.monthly_expenses[category] / total_expenses) * 100

    def get_expense_categories(self):
        return list(self.monthly_expenses.keys())

    def reset(self):
        self.monthly_income = 0
        self.monthly_expenses = {}

    if __name__ == '__main__':
        planner = BudgetPlanner()

        while True:

          print("\nBudget Planner Menu:")
          print("1. Add Monthly Income")
          print("2. Add Monthly Expense")
          print("3. Calculate Savings")
          print("4. Get Monthly Income")
          print("5. Get Monthly Expenses")
          print("6. Get Savings")
          print("7. Get Total Expenses")
          print("8. Get Remaining Income")
          print("9. Get Expense Percentage")
          print("10. View Expense Categories")
          print("11. Reset")

          choice = input("Enter your choice (1-11): ")

          if choice == '1':
              amount = float(input("Enter monthly income: "))
              planner.add_monthly_income(amount)
