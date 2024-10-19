# expenseTracker.py

import sqlite3
from datetime import datetime
from Expense import Expense


class ExpenseTracker:
    def __init__(self, db_name="expenses.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_expenses_table()
        self.create_user_table()

    def create_expenses_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                date TEXT NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
            )''')

    def create_user_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                income REAL NOT NULL
            )''')

    def add_expense(self, user_id: int, category: str, amount: float, date: str):
        try:
            expense = Expense(category, amount, date)
            with self.conn:
                self.conn.execute("INSERT INTO expenses (user_id, category, amount, date) VALUES (?, ?, ?, ?)",
                                  (user_id, expense.category, expense.amount, expense.date))
            print(f"Expense added: {expense.category}, {expense.amount}, {expense.date}")
        except ValueError as e:
            print(f"Error: {e}")

    def total_expenses(self, month: int, year: int) -> float:
        cursor = self.conn.cursor()
        cursor.execute('''SELECT SUM(amount) FROM expenses 
                          WHERE strftime('%m', date) = ? AND strftime('%Y', date) = ?''',
                       (f"{month:02d}", str(year)))
        total = cursor.fetchone()[0]
        return total if total else 0.0

    def categorize_expenses(self):
        cursor = self.conn.cursor()
        cursor.execute('''SELECT category, SUM(amount) FROM expenses GROUP BY category''')
        return cursor.fetchall()

    def generate_report(self):
        categories = self.categorize_expenses()
        print("\nExpense Report:")
        for category, total in categories:
            print(f"{category}: ${total:.2f}")

    def generate_user_report(self, user_id: int):
        cursor = self.conn.cursor()

        # Get user's income
        cursor.execute("SELECT income FROM users WHERE user_id = ?", (user_id,))
        income = cursor.fetchone()[0]

        # Get total expenses for the user
        cursor.execute("SELECT SUM(amount) FROM expenses WHERE user_id = ?", (user_id,))
        total_expenses = cursor.fetchone()[0]

        print(f"\nUser Report:")
        print(f"User Income: ${income:.2f}")
        print(f"Total Expenses: ${total_expenses if total_expenses else 0.0:.2f}")
        print(f"Remaining Income: ${income - (total_expenses if total_expenses else 0):.2f}")
