from functions import (
    show_menu,
    add_expense,
    show_expenses,
    total_expenses,
    remove_expense,
)

expenses = []


while True:
    show_menu()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print()
        print("Please enter a valid number.")
        print()
        continue

    if choice == 1:
        add_expense(expenses)

    elif choice == 2:
        remove_expense(expenses)

    elif choice == 3:
        print("Your expenses:")
        show_expenses(expenses)

    elif choice == 4:
        total_expenses(expenses)

    elif choice == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")
