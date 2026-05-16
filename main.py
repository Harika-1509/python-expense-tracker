import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime


class ExpenseTracker:

    def __init__(self):

        self.file_name = "expenses.csv"

    def add_expense(self):

        try:

            category = input("Enter category: ")

            amount = float(input("Enter amount: "))

            description = input("Enter description: ")

            date = datetime.now().strftime("%Y-%m-%d")

            with open(self.file_name, "a", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    date,
                    category,
                    amount,
                    description
                ])

            print("Expense added successfully!")

        except ValueError:

            print("Invalid amount entered.")

        except Exception as e:

            print("Error:", e)

    def view_expenses(self):

        try:

            df = pd.read_csv(self.file_name)

            print("\n===== ALL EXPENSES =====")

            print(df)

        except Exception as e:

            print("Error:", e)

    def analyze_expenses(self):

        try:

            df = pd.read_csv(self.file_name)

            print("\n===== EXPENSE ANALYSIS =====")

            total = df["Amount"].sum()

            average = df["Amount"].mean()

            maximum = df["Amount"].max()

            print("Total Spending:", total)

            print("Average Spending:", average)

            print("Highest Expense:", maximum)

            print("\nCategory Wise Spending:")

            print(df.groupby("Category")["Amount"].sum())

        except Exception as e:

            print("Error:", e)

    def show_graph(self):

        try:

            df = pd.read_csv(self.file_name)

            category_data = df.groupby("Category")["Amount"].sum()

            plt.figure(figsize=(8,5))

            category_data.plot(kind="bar")

            plt.title("Category Wise Expenses")

            plt.xlabel("Category")

            plt.ylabel("Amount")

            plt.grid(True)

            plt.show()

        except Exception as e:

            print("Error:", e)


tracker = ExpenseTracker()

while True:

    print("\n===== EXPENSE TRACKER =====")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Analyze Expenses")
    print("4. Show Expense Graph")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        tracker.add_expense()

    elif choice == "2":

        tracker.view_expenses()

    elif choice == "3":

        tracker.analyze_expenses()

    elif choice == "4":

        tracker.show_graph()

    elif choice == "5":

        print("Exiting program...")

        break

    else:

        print("Invalid choice.")