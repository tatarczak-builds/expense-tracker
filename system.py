
expenses = []

while True:
    print("=========== Menu ===========")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Exit")
    print("4. Show total expenses")
# int before input to ensure the user enters a valid integer
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        print(f"Expense '{name}' of amount {amount} added.")
        expenses.append((name, amount))
    elif choice == 2:
        print("Showing expenses...")
        for name, amount in expenses:
            print(f"Expense: {name}, Amount: {amount}")
    elif choice == 3:
        print("Exiting...")
        break
    elif choice == 4:
        total = sum(amount for _, amount in expenses)
        print(f"Total expenses: {total}")

    else:
        print("Invalid choice. Please try again.")
