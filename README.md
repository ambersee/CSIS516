Budget Planner App - used to help track expenses and savings.
Very self explanatory. Answer the questions with the correct amounts based on your personal situation. 
The purpose and value of this app is to help people with their finances and budget planning is an important part of that.
Tech used = Tkinter, python, visual code, and chat gpt to figure out how to fix the errors that occurred throughout the process so far. 

Code so far:

import tkinter as tk
from tkinter import messagebox

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
        return self.monthly_income - total_expenses

class BudgetApp:
    def __init__(self, root):
        self.budget = BudgetPlanner()

        root.title("Budget Planner")
        root.geometry("400x400")

        # Income Section
        self.income_label = tk.Label(root, text="Enter Monthly Income:")
        self.income_label.pack()
        self.income_entry = tk.Entry(root)
        self.income_entry.pack()
        self.add_income_btn = tk.Button(root, text="Add Income", command=self.add_income)
        self.add_income_btn.pack()

        # Expenses Section
        self.expense_label = tk.Label(root, text="Enter Expense Category and Amount:")
        self.expense_label.pack()

        self.expense_category_entry = tk.Entry(root)
        self.expense_category_entry.insert(0, "Category")
        self.expense_category_entry.bind("<FocusIn>", self.clear_placeholder_category)
        self.expense_category_entry.bind("<FocusOut>", self.restore_placeholder_category)
        self.expense_category_entry.pack()

        self.expense_amount_entry = tk.Entry(root)
        self.expense_amount_entry.insert(0, "Amount")
        self.expense_amount_entry.bind("<FocusIn>", self.clear_placeholder_amount)
        self.expense_amount_entry.bind("<FocusOut>", self.restore_placeholder_amount)
        self.expense_amount_entry.pack()

        self.add_expense_btn = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_expense_btn.pack()

        # Show Summary Button
        self.summary_btn = tk.Button(root, text="Show Summary", command=self.show_summary)
        self.summary_btn.pack()

        # Summary Output
        self.result_label = tk.Label(root, text="", fg="blue")
        self.result_label.pack()

    # Placeholder Functions
    def clear_placeholder_category(self, event):
        if self.expense_category_entry.get() == "Category":
            self.expense_category_entry.delete(0, tk.END)
            self.expense_category_entry.config(fg="black")

    def restore_placeholder_category(self, event):
        if not self.expense_category_entry.get():
            self.expense_category_entry.insert(0, "Category")
            self.expense_category_entry.config(fg="gray")

    def clear_placeholder_amount(self, event):
        if self.expense_amount_entry.get() == "Amount":
            self.expense_amount_entry.delete(0, tk.END)
            self.expense_amount_entry.config(fg="black")

    def restore_placeholder_amount(self, event):
        if not self.expense_amount_entry.get():
            self.expense_amount_entry.insert(0, "Amount")
            self.expense_amount_entry.config(fg="gray")

    # Functions to Add Income and Expenses
    def add_income(self):
        try:
            income = float(self.income_entry.get())
            self.budget.add_monthly_income(income)
            self.income_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Income added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def add_expense(self):
        category = self.expense_category_entry.get()
        try:
            amount = float(self.expense_amount_entry.get())
            self.budget.add_monthly_expense(category, amount)
            self.expense_category_entry.delete(0, tk.END)
            self.expense_amount_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Expense added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid amount.")

    def show_summary(self):
        savings = self.budget.calculate_savings()
        summary_text = f"Total Income: ${self.budget.monthly_income}\n" \
                       f"Total Expenses: ${sum(self.budget.monthly_expenses.values())}\n" \
                       f"Savings: ${savings}"
        self.result_label.config(text=summary_text)

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()
