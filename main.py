import argparse
import json
import os
from datetime import datetime
from tabulate import tabulate
from calendar import month_name

DATA_FILE = "expenses.json"


# -----------------------------
# Utility Functions
# -----------------------------

def load_expenses():
    """
    Reads expenses from the JSON file.
    If the file doesn't exist, return an empty list.
    """
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    """
    Saves the updated expense list back into the JSON file.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(expenses, file, indent=4)


# -----------------------------
# Core Functionalities
# -----------------------------

def add_expense(description, amount):
    """
    Adds a new expense to the JSON file.
    Automatically assigns a new ID.
    """
    if amount < 0:
        print("Amount cannot be negative.")
        return

    expenses = load_expenses()

    # Generate next ID
    new_id = max([e["id"] for e in expenses], default=0) + 1

    expense = {
        "id": new_id,
        "date": datetime.today().strftime("%Y-%m-%d"),
        "description": description,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print(f"Expense added successfully (ID: {new_id})")


def list_expenses():
    """
    Displays all expenses in a table format.
    """
    expenses = load_expenses()

    if not expenses:
        print("No expenses found.")
        return

    table = []
    for e in expenses:
        table.append([e["id"], e["date"], e["description"], f"${e['amount']:.2f}"])

    print(tabulate(table, headers=["ID", "Date", "Description", "Amount"]))


def delete_expense(expense_id):
    """
    Deletes an expense by ID.
    """
    expenses = load_expenses()

    updated_expenses = [e for e in expenses if e["id"] != expense_id]

    if len(expenses) == len(updated_expenses):
        print("Expense ID not found.")
        return

    save_expenses(updated_expenses)
    print("Expense deleted successfully")


def summary(month=None):
    expenses = load_expenses()

    if month:
        expenses = [
            e for e in expenses
            if int(e["date"].split("-")[1]) == month
        ]

        total = sum(e["amount"] for e in expenses)
        month_str = month_name[month]
        print(f"Total expenses for {month_str}: ${total}")
    else:
        total = sum(e["amount"] for e in expenses)
        print(f"Total expenses: ${total:.2f}")

def update_expense(expense_id, description=None, amount=None):
    """
    Updates an existing expense by ID.
    """
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            if description:
                expense["description"] = description
            if amount is not None:
                if amount < 0:
                    print("Amount cannot be negative.")
                    return
                expense["amount"] = amount

            save_expenses(expenses)
            print("Expense updated successfully")
            return

    print("Expense ID not found.")

# -----------------------------
# CLI Configuration
# -----------------------------

parser = argparse.ArgumentParser(description="Expense Tracker CLI")
subparsers = parser.add_subparsers(dest="command")

# ADD command
add_parser = subparsers.add_parser("add")
add_parser.add_argument("--description", required=True)
add_parser.add_argument("--amount", type=float, required=True)

# LIST command
subparsers.add_parser("list")

# DELETE command
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("--id", type=int, required=True)

# SUMMARY command
summary_parser = subparsers.add_parser("summary")
summary_parser.add_argument("--month", type=int)

# UPDATE command
update_parser = subparsers.add_parser("update")
update_parser.add_argument("--id", type=int, required=True)
update_parser.add_argument("--description")
update_parser.add_argument("--amount", type=float)

args = parser.parse_args()

# -----------------------------
# Command Handling
# -----------------------------

if args.command == "add":
    add_expense(args.description, args.amount)

elif args.command == "list":
    list_expenses()

elif args.command == "delete":
    delete_expense(args.id)

elif args.command == "summary":
    summary(args.month)

elif args.command == "update":
    update_expense(args.id, args.description, args.amount)

else:
    parser.print_help()

