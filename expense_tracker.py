import json
import os

FILE_NAME = "expenses.json"

# Load expenses from file
def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

# Save expenses to file
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

# Add expense
def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))
        category = input("Enter category: ")

        expense = {
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        save_expenses(expenses)

        print("✅ Expense added successfully!")

    except ValueError:
        print("❌ Please enter a valid amount.")

# View expenses
def view_expenses():
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n===== Expense List =====")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ₹{expense['amount']} - {expense['category']}")

# Total expenses
def total_expenses():
    total = sum(expense["amount"] for expense in expenses)
    print(f"\n💰 Total Expenses: ₹{total}")

# Delete expense
def delete_expense():
    view_expenses()

    if not expenses:
        return

    try:
        index = int(input("\nEnter expense number to delete: ")) - 1

        if 0 <= index < len(expenses):
            removed = expenses.pop(index)
            save_expenses(expenses)
            print(f"✅ Deleted: ₹{removed['amount']} - {removed['category']}")
        else:
            print("❌ Invalid expense number.")

    except ValueError:
        print("❌ Enter a valid number.")

# Main
expenses = load_expenses()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        print("👋 Thank you for using Expense Tracker!")
        break

    else:
        print("❌ Invalid option.")
