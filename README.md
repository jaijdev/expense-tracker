# Expense Tracker CLI

A simple command-line expense tracker built in Python.

This project allows users to add, update, delete, and summarize expenses directly from the terminal.

---

## Project URL

https://roadmap.sh/projects/expense-tracker

---

## Features

- Add expenses
- Update expenses
- Delete expenses
- View all expenses
- View total expense summary
- View monthly expense summary
- Persistent storage using JSON

---

## Tech Stack

- Python 3
- argparse (CLI argument parsing)
- JSON (data storage)
- tabulate (table formatting)

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/jaijdev/expense-tracker.git
cd expense-tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install tabulate
```

---

## Usage

### Add an expense

```bash
python main.py add --description "Lunch" --amount 20
```

### List all expenses

```bash
python main.py list
```

### Update an expense

```bash
python main.py update --id 1 --description "Dinner"
```

Update amount:

```bash
python main.py update --id 1 --amount 35
```

### Delete an expense

```bash
python main.py delete --id 1
```

### View total summary

```bash
python main.py summary
```

### View monthly summary

```bash
python main.py summary --month 2
```

---

## Project Structure

```
expense-tracker/
│
├── main.py
├── expenses.json
└── README.md
```

---

## How It Works

- Expenses are stored in `expenses.json`.
- Each expense has:
  - ID
  - Date
  - Description
  - Amount
- The CLI uses `argparse` to parse commands.
- Data is loaded from and saved to a JSON file for persistence.

---

## Author

Jai Joshi