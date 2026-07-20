def show_menu():
    print("=========== Menu ===========")
    print()
    print("1. Add expense")
    print("2. Remove an expense")
    print("3. Show expenses")
    print("4. Show total expenses")
    print("5. Exit")


def add_expense(expenses):
    while True:

        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        expenses.append((name, amount))
        print(f"Expense '{name}' of amount {amount} added.")
        print()

        another = input("Add another expense? (y/n): ").strip().lower()

        if another not in ("y", "yes"):
            break


def show_expenses(expenses):
    for index, (name, amount) in enumerate(expenses):
        print(f"{index + 1}. {name} - {amount}")


def total_expenses(expenses):
    total = sum(amount for _, amount in expenses)
    print(f"Total expenses: {total}")


def remove_expense(expenses):
    print("which expense would you like to remove?")
    show_expenses(expenses)
    chosen_index = int(
        input("Enter the number of the expense to remove: ")) - 1
    if 0 <= chosen_index < len(expenses):
        removed_expense = expenses.pop(chosen_index)
        print(f"Removed expense: {removed_expense[0]} - {removed_expense[1]}")
    else:
        print("Invalid index. No expense removed.")
