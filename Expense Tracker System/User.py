
from ExpenseTracker import ExpenseTracker

class User:
    def __init__(self, name: str, income: float):
        self.name = name
        self.income = income
        self.tracker = ExpenseTracker()

    def add_expense(self, category: str, amount: float, date: str):
        self.tracker.add_expense(self.get_user_id(), category, amount, date)

    def get_user_id(self) -> int:
        cursor = self.tracker.conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE name = ?", (self.name,))
        result = cursor.fetchone()
        if result:
            return result[0]
        else:
            self.tracker.conn.execute("INSERT INTO users (name, income) VALUES (?, ?)", (self.name, self.income))
            return self.get_user_id()

    def generate_report(self):
        self.tracker.generate_report()

    def generate_user_report(self):
        self.tracker.generate_user_report(self.get_user_id())
