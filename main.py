import json

balance = 0

try:

    with open("transactions.json", "r") as file:

        transactions = json.load(file)

except:

    transactions = []

while True:

    balance = 0

    for transaction in transactions:

        if transaction["type"] == "Income":

            balance += transaction["amount"]

        else:

            balance -= transaction["amount"]

    print("\n--- PERSONAL EXPENSE TRACKER ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    print("4. View Transactions")
    print("5. View Report")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == "1":

        amount = float(input("Enter income amount: "))
        category = input("Enter category: ")
        date = input("Enter date: ")
        description = input("Enter description: ")

        transaction = {
            "type": "Income",
            "amount": amount,
            "category": category,
            "date": date,
            "description": description
        }

        transactions.append(transaction)

        with open("transactions.json", "w") as file:

            json.dump(transactions, file, indent=4)

        print("Income added successfully.")

    elif option == "2":

        amount = float(input("Enter expense amount: "))
        category = input("Enter category: ")
        date = input("Enter date: ")
        description = input("Enter description: ")

        transaction = {
            "type": "Expense",
            "amount": amount,
            "category": category,
            "date": date,
            "description": description
        }

        transactions.append(transaction)

        with open("transactions.json", "w") as file:

            json.dump(transactions, file, indent=4)

        print("Expense added successfully.")

    elif option == "3":

        print("\nCurrent Balance: $", balance)

    elif option == "4":

        print("\n--- TRANSACTION HISTORY ---")

        for transaction in transactions:

            print(
                transaction["date"],
                "-",
                transaction["type"],
                "- $", transaction["amount"],
                "- Category:", transaction["category"],
                "- Description:", transaction["description"]
            )

    elif option == "5":

        total_income = 0
        total_expenses = 0

        categories = {}

        for transaction in transactions:

            if transaction["type"] == "Income":

                total_income += transaction["amount"]

            else:

                total_expenses += transaction["amount"]

                category = transaction["category"]

                if category in categories:

                    categories[category] += transaction["amount"]

                else:

                    categories[category] = transaction["amount"]

        print("\n--- FINANCIAL REPORT ---")

        print("Total Income: $", total_income)
        print("Total Expenses: $", total_expenses)
        print("Current Balance: $", balance)

        print("\n--- EXPENSES BY CATEGORY ---")

        for category in categories:

            print(category, ": $", categories[category])

    elif option == "6":

        print("Exiting program...")
        break

    else:

        print("Invalid option.")