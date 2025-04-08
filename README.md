Budget Planner App - used to help track expenses and savings.
Very self explanatory. Answer the questions with the correct amounts based on your personal situation. 
The purpose and value of this app is to help people with their finances and budget planning is an important part of that.
Tech used = Tkinter, python, visual code, and chat gpt to figure out how to fix the errors that occurred throughout the process so far. 

Code so far:

import tkinter as tk
from tkinter import messagebox, font, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime

class BudgetPlanner:
    def __init__(self):
        self.budgets_by_month = {}

    def get_month_data(self, month):
        if month not in self.budgets_by_month:
            self.budgets_by_month[month] = {
                'income': 0,
                'expenses': {},
                'limits': {}
            }
        return self.budgets_by_month[month]

    def add_income(self, month, amount):
        self.get_month_data(month)['income'] += amount

    def set_limit(self, month, category, limit):
        self.get_month_data(month)['limits'][category] = limit

    def add_expense(self, month, category, amount):
        data = self.get_month_data(month)
        data['expenses'][category] = data['expenses'].get(category, 0) + amount

        if category in data['limits'] and data['expenses'][category] > data['limits'][category]:
            return f"⚠️ Over budget for {category}!"
        return None

    def calculate_savings(self, month):
        data = self.get_month_data(month)
        return data['income'] - sum(data['expenses'].values())

    def reset_month(self, month):
        if month in self.budgets_by_month:
            del self.budgets_by_month[month]

    def save_summary(self, month):
        data = self.get_month_data(month)
        with open(f"budget_summary_{month}.txt", "w") as file:
            file.write(f"Month: {month}\n")
            file.write(f"Income: ${data['income']:.2f}\n")
            file.write("Expenses:\n")
            for cat, amt in data['expenses'].items():
                line = f"  {cat}: ${amt:.2f}"
                if cat in data['limits']:
                    line += f" (Limit: ${data['limits'][cat]:.2f})"
                file.write(line + "\n")
            file.write(f"Savings: ${self.calculate_savings(month):.2f}\n")

    def save_all_summaries(self):
        with open("budget_summary_all.txt", "w") as file:
            for month in self.budgets_by_month:
                data = self.get_month_data(month)
                file.write(f"Month: {month}\n")
                file.write(f"Income: ${data['income']:.2f}\n")
                file.write("Expenses:\n")
                for cat, amt in data['expenses'].items():
                    line = f"  {cat}: ${amt:.2f}"
                    if cat in data['limits']:
                        line += f" (Limit: ${data['limits'][cat]:.2f})"
                    file.write(line + "\n")
                file.write(f"Savings: ${self.calculate_savings(month):.2f}\n\n")

class BudgetApp:
    def __init__(self, root):
        self.budget = BudgetPlanner()
        self.categories = ["Groceries", "Rent", "Utilities", "Transportation", "Entertainment", "Savings", "Other"]

        root.title("Budget Planner")
        root.geometry("550x720")
        root.configure(bg="#f0f4f7")

        self.month_var = tk.StringVar(value=datetime.now().strftime("%B"))
        self.category_var = tk.StringVar()

        font_header = font.Font(size=12, weight="bold")

        tk.Label(root, text="Select Month:", bg="#f0f4f7", font=font_header).pack(pady=5)
        ttk.Combobox(root, textvariable=self.month_var, values=self.get_months(), state="readonly").pack()

        tk.Label(root, text="Enter Monthly Income:", bg="#f0f4f7", font=font_header).pack(pady=5)
        self.income_entry = tk.Entry(root)
        self.income_entry.pack(pady=5)
        tk.Button(root, text="Add Income", command=self.add_income).pack()

        tk.Label(root, text="Choose Expense Category:", bg="#f0f4f7", font=font_header).pack(pady=5)
        self.category_dropdown = ttk.Combobox(root, textvariable=self.category_var, values=self.categories, state="readonly")
        self.category_dropdown.bind("<<ComboboxSelected>>", self.toggle_custom_category_entry)
        self.category_dropdown.pack()

        self.custom_category_entry = tk.Entry(root)
        self.custom_category_entry.pack(pady=5)
        self.custom_category_entry.pack_forget()

        tk.Label(root, text="Enter Expense Amount:", bg="#f0f4f7", font=font_header).pack(pady=5)
        self.expense_amount_entry = tk.Entry(root)
        self.expense_amount_entry.pack(pady=5)

        tk.Label(root, text="(Optional) Set Limit for Category:", bg="#f0f4f7").pack()
        self.limit_entry = tk.Entry(root)
        self.limit_entry.pack(pady=5)

        tk.Button(root, text="Add Expense", command=self.add_expense).pack(pady=5)

        self.expense_listbox = tk.Listbox(root, width=50)
        self.expense_listbox.pack(pady=5)

        self.result_label = tk.Label(root, text="", fg="blue", bg="#f0f4f7")
        self.result_label.pack()

        tk.Button(root, text="Show Summary", command=self.show_summary).pack(pady=5)
        tk.Button(root, text="Show Bar Chart", command=self.show_bar_chart).pack(pady=5)

        tk.Button(root, text="Save This Month", command=self.save_this_month).pack(pady=5)
        tk.Button(root, text="Save All Months", command=self.save_all_months).pack(pady=5)
        tk.Button(root, text="Reset This Month", command=self.reset_month).pack(pady=5)

    def get_months(self):
        return [datetime(1900, m, 1).strftime('%B') for m in range(1, 13)]

    def toggle_custom_category_entry(self, event):
        if self.category_var.get() == "Other":
            self.custom_category_entry.pack()
        else:
            self.custom_category_entry.pack_forget()

    def get_current_category(self):
        return self.custom_category_entry.get() if self.category_var.get() == "Other" else self.category_var.get()

    def add_income(self):
        try:
            income = float(self.income_entry.get())
            self.budget.add_income(self.month_var.get(), income)
            self.income_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Income added!")
        except ValueError:
            messagebox.showerror("Error", "Enter a valid income amount.")

    def add_expense(self):
        month = self.month_var.get()
        category = self.get_current_category()
        try:
            amount = float(self.expense_amount_entry.get())
            limit = self.limit_entry.get()
            if limit:
                self.budget.set_limit(month, category, float(limit))
            warning = self.budget.add_expense(month, category, amount)
            self.expense_amount_entry.delete(0, tk.END)
            self.limit_entry.delete(0, tk.END)
            self.custom_category_entry.delete(0, tk.END)
            self.update_expense_list()
            if warning:
                messagebox.showwarning("Budget Alert", warning)
            else:
                messagebox.showinfo("Success", f"Expense added to {category}.")
        except ValueError:
            messagebox.showerror("Error", "Enter valid expense amount.")

    def update_expense_list(self):
        self.expense_listbox.delete(0, tk.END)
        month = self.month_var.get()
        data = self.budget.get_month_data(month)
        for cat, amt in data['expenses'].items():
            line = f"{cat}: ${amt:.2f}"
            if cat in data['limits']:
                line += f" (Limit: ${data['limits'][cat]:.2f})"
            self.expense_listbox.insert(tk.END, line)

    def show_summary(self):
        month = self.month_var.get()
        savings = self.budget.calculate_savings(month)
        data = self.budget.get_month_data(month)
        summary = f"Total Income: ${data['income']:.2f}\n" \
                  f"Total Expenses: ${sum(data['expenses'].values()):.2f}\n" \
                  f"Savings: ${savings:.2f}"
        self.result_label.config(text=summary)
        self.update_expense_list()

    def show_bar_chart(self):
        month = self.month_var.get()
        data = self.budget.get_month_data(month)
        if not data['expenses']:
            messagebox.showinfo("No Data", "No expenses to display.")
            return

        fig, ax = plt.subplots(figsize=(5, 4))
        categories = list(data['expenses'].keys())
        amounts = list(data['expenses'].values())

        ax.bar(categories, amounts, color="teal")
        ax.set_title(f"Expenses for {month}")
        ax.set_ylabel("Amount ($)")
        ax.set_xticks(range(len(categories)))
        ax.set_xticklabels(categories, rotation=45, ha='right')

        window = tk.Toplevel()
        window.title("Expense Bar Chart")
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def save_this_month(self):
        self.budget.save_summary(self.month_var.get())
        messagebox.showinfo("Saved", f"Summary for {self.month_var.get()} saved!")

    def save_all_months(self):
        self.budget.save_all_summaries()
        messagebox.showinfo("Saved", "All summaries saved to 'budget_summary_all.txt'.")

    def reset_month(self):
        self.budget.reset_month(self.month_var.get())
        self.expense_listbox.delete(0, tk.END)
        self.result_label.config(text="")
        messagebox.showinfo("Reset", f"Data for {self.month_var.get()} has been reset.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()

