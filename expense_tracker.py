from expense import Expense


def main():
    print("Running Expense Tracker!")

    # get user input for expense
    expense = get_user_expense()
    print(expense)

    # write their expense to a file
    save_expense_to_file()

    # read file and summarize expenses
    summarize_expenses()


def get_user_expense():
    print("Getting User Expense")
    expense_date = input("Enter the date (YYYY-MM-DD): ")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))
    expense_categories = [
        "Food",
        "Home",
        "Transport",
        "Healthcare",
        "Clothing",
        "Entertainment",
        "Savings",
        "Miscellaneous",
    ]

    while True:
        print(f"Select a category:")
        for i, category_name in enumerate(expense_categories):
            print(f"{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category: {value_range}")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                date=expense_date,
                name=expense_name,
                category=selected_category,
                amount=expense_amount,
            )
            return new_expense
        else:
            print("Invalid category. Please try again!")


def save_expense_to_file():
    print("Saving User Expense")


def summarize_expenses():
    print("Summarizing User Expenses")


if __name__ == "__main__":
    main()
