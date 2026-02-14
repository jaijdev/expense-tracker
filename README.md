Expense Tracker CLI

A simple command-line expense tracker built in Python.

**Project URL:**
https://roadmap.sh/projects/expense-tracker

**Features**

- Add expenses
- Update expenses
- Delete expenses
- View all expenses
- View total summary
- View monthly summary

Setup

Clone the repository:

git clone https://github.com/jaijdev/expense-tracker.git
cd expense-tracker


Create virtual environment:

python -m venv venv
source venv/bin/activate


Install dependencies:

pip install tabulate

Usage

Add expense:

python main.py add --description "Lunch" --amount 20


List expenses:

python main.py list


Update expense:

python main.py update --id 1 --description "Dinner"


Delete expense:

python main.py delete --id 1


View total summary:

python main.py summary


View monthly summary:

python main.py summary --month 2
