"""A simple command-line personal expense tracker."""

expenses = []
total_expenses = 0.0


def add_expense():
    global total_expenses

    name = input("Enter the expense name: ").strip()

    if not name:
        print("The expense name cannot be empty.")
        return

    try:
        amount = float(input("Enter the expense amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if amount <= 0:
        print("The amount must be greater than zero.")
        return

    expense = {"name": name, "amount": amount}
    expenses.append(expense)
    total_expenses += amount

    print("Expense added successfully!")


def list_expenses():
    if not expenses:
        print("No expenses have been added yet.")
        return

    print("\n--- YOUR EXPENSES ---")

    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense['name']}: "
            f"{expense['amount']:.2f} TL"
        )


def show_total():
    print(f"Total expenses: {total_expenses:.2f} TL")


def main():
    print("Welcome to the Personal Expense Tracker!")

    while True:
        print("\n--- EXPENSE TRACKER MENU ---")
        print("1. Add an expense")
        print("2. List expenses")
        print("3. Show total expenses")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            print("Thanks for using the Personal Expense Tracker!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
