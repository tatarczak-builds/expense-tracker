def show_menu():
    print()
    print("=========== Menu ===========")
    print()
    print("1. Add expense")
    print("2. Remove an expense")
    print("3. Show expenses")
    print("4. Show total expenses")
    print("5. Exit")
    print()


def add_expense(expenses):
    while True:
        print()
        name = input("Enter expense name: ")

        while True:
            try:
                amount = float(input("Enter expense amount: "))
                expenses.append((name, amount))
                break
            except ValueError:
                print("Please enter a proper amount.")

        save_expenses(expenses)

        print(f"Expense '{name}' of amount {amount:.2f} added.")
        print()

        while True:
            another = input("Add another expense? (y/n): ").strip().lower()

            if another in ("y", "yes"):
                break

            elif another in ("n", "no"):
                return

            else:
                print("Please enter y or n")


def remove_expense(expenses):
    while True:
        if not expenses:
            print("No expenses to remove.")
            return

        print("=== Remove expense ===")
        print()

        show_expenses(expenses)

        print()

        try:
            chosen_index = int(
                input("Enter the number of the expense to remove: ")) - 1
            print()
        except ValueError:
            print("Please enter a valid number.")
            continue

        if 0 <= chosen_index < len(expenses):
            removed_expense = expenses.pop(chosen_index)

            print()
            print(
                f"Removed expense: {removed_expense[0]} - {removed_expense[1]:.2f}")
            print()

            save_expenses(expenses)

        else:
            print("Invalid index. No expense removed.")
            continue

        while True:
            another = input("Remove another expense? (y/n): ").strip().lower()

            if another in ("y", "yes"):
                break

            elif another in ("n", "no"):
                return

            else:
                print("Please enter y or n")


def show_expenses(expenses):
    if not expenses:
        print()
        print("No expenses found.")
        print()
        return

    for index, (name, amount) in enumerate(expenses, start=1):
        print(f"{index}. {name} - {amount:.2f}")


def total_expenses(expenses):
    total = sum(amount for _, amount in expenses)
    print()
    print(f"Total expenses: {total:.2f}")


def save_expenses(expenses):
    with open("expenses.txt", "w") as file:
        for name, amount in expenses:
            file.write(f"{name}-{amount}\n")


def load_expenses():
    expenses = []

    try:
        with open("expenses.txt", "r") as file:
            content = file.read()
            lines = content.split("\n")

            for line in lines:
                # may also be if not line: continue
                if line == '':
                    continue

                name, amount = line.rsplit("-", 1)
                amount = float(amount)
                expenses.append((name, amount))
    except FileNotFoundError:
        pass

    return expenses
