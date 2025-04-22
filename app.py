from flask import Flask, render_template, request, redirect, flash, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory storage for transactions
transactions = []

@app.route('/')
def index():
    selected_month = request.args.get('month')
    now = datetime.now()
    month_filter = selected_month if selected_month else now.strftime("%Y-%m")

    filtered = [
        tx for tx in transactions
        if tx['date'].strftime('%Y-%m') == month_filter
    ]

    income = sum(float(tx['amount']) for tx in filtered if tx['transaction_type'] == "Income")
    expense = sum(float(tx['amount']) for tx in filtered if tx['transaction_type'] == "Expense")
    balance = income - expense

    expense_by_category = {}
    for tx in filtered:
        if tx['transaction_type'] == "Expense":
            category = tx['category']
            expense_by_category[category] = expense_by_category.get(category, 0) + float(tx['amount'])

    return render_template(
        'index.html',
        transactions=filtered,
        total_income=income,
        total_expense=expense,
        balance=balance,
        selected_month=month_filter,
        expense_by_category=expense_by_category
    )

@app.route('/add', methods=['POST'])
def add_transaction():
    tx_type = request.form.get('transaction_type')
    amount = request.form.get('amount')
    category = request.form.get('category', '')
    if category == "Other":
        category = request.form.get("custom_category", "Other")
    if tx_type == "Income":
        category = ''

    transactions.append({
        "transaction_type": tx_type,
        "amount": amount,
        "category": category,
        "date": datetime.now()
    })

    flash("Transaction added!")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
