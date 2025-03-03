<img width="1280" alt="Screenshot 2025-03-02 at 7 53 17 PM" src="https://github.com/user-attachments/assets/8abf293f-034e-4423-a860-3e69c2f35e84" />
<img width="1280" alt="Screenshot 2025-03-02 at 8 05 26 PM" src="https://github.com/user-attachments/assets/2c69a54f-7def-4838-b815-caf212e6e7aa" />
<img width="1280" alt="Screenshot 2025-03-02 at 8 05 21 PM" src="https://github.com/user-attachments/assets/07181831-de94-490d-8990-d29f8f14dc9b" />
<img width="1280" alt="Screenshot 2025-03-02 at 8 05 15 PM" src="https://github.com/user-attachments/assets/e9aa0082-1cfc-4ca5-8b21-57ea86f4813d" />
<img width="1280" alt="Screenshot 2025-03-02 at 7 53 51 PM" src="https://github.com/user-attachments/assets/305fd45c-b301-4c74-9862-c85d3ebd5722" />
<img width="1280" alt="Screenshot 2025-03-02 at 7 53 41 PM" src="https://github.com/user-attachments/assets/0a85f6cf-e171-4cd4-a01b-eccc7b57562d" />
<img width="1280" alt="Screenshot 2025-03-02 at 7 53 33 PM" src="https://github.com/user-attachments/assets/e5852311-fd21-4848-81fa-10190413b98e" />
<img width="1280" alt="Screenshot 2025-03-02 at 7 53 25 PM" src="https://github.com/user-attachments/assets/c40464a7-be06-422d-ba7b-6c482eb9edad" />
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
