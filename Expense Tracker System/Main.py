# main.py

from User import User
from datetime import datetime


def print_welcome():
    print("=" * 50)
    print("💸 Welcome to the Expense Tracker System 💸".center(50))
    print("=" * 50)


def print_menu():
    print("\n🔸 What would you like to do?")
    print("1️⃣  Add Expense")
    print("2️⃣  View Total Expenses")
    print("3️⃣  Generate Expense Report")
    print("4️⃣  Generate User Financial Report")
    print("5️⃣  Exit")


def get_valid_float(prompt: str):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❗Invalid input! Please enter a valid number.")


def get_valid_date():
    while True:
        date = input("📅 Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("❗Invalid date format! Please try again using YYYY-MM-DD.")


def main():
    print_welcome()
    name = input("👤 Enter your name: ")
    income = get_valid_float("💰 Enter your income: ")
    user = User(name, income)

    while True:
        print_menu()
        choice = input("➡️ Select an option (1-5): ")

        if choice == '1':
            print("\n--- 📝 Add a New Expense ---")
            category = input("📂 Enter category: ")
            amount = get_valid_float("💵 Enter amount: ")
            date = get_valid_date()
            user.add_expense(category, amount, date)

        elif choice == '2':
            print("\n--- 📊 View Total Expenses ---")
            month = input("📅 Enter month (MM): ")
            year = input("📅 Enter year (YYYY): ")
            try:
                month = int(month)
                year = int(year)
                total = user.tracker.total_expenses(month, year)
                print(f"✅ Total expenses for {month:02}/{year}: ${total:.2f}")
            except ValueError:
                print("❗Invalid input for month/year. Please try again.")

        elif choice == '3':
            print("\n--- 📑 Generating Expense Report ---")
            user.generate_report()

        elif choice == '4':
            print("\n--- 🧾 Generating User Financial Report ---")
            user.generate_user_report()

        elif choice == '5':
            print("\n👋 Exiting the Expense Tracker. Goodbye!")
            break

        else:
            print("❗Invalid choice. Please select a valid option (1-5).")


if __name__ == "__main__":
    main()
