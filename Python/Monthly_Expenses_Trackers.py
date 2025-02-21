class Admin:
    def __init__(self, username, password):  # Fixed constructor
        self.username = username
        self.password = password
        self.customers_data = []  

    def login(self, username, password):
        return self.username == username and self.password == password

    def view_expenses(self):
        if not self.customers_data:
            print("No customer data available.")
        else:
            for customer in self.customers_data:
                total_expenses = sum(exp['amount'] for exp in customer.expenses)
                print(f"Customer: {customer.name}, Total Expenses: {total_expenses}")

    def highest_spending(self):
        if not self.customers_data:
            print("No customer data available.")
        else:
            highest_spender = self.get_highest_spender()
            if highest_spender:
                total_expenses = sum(exp['amount'] for exp in highest_spender.expenses)
                print(f"Highest spender is {highest_spender.name} with total expenses: {total_expenses}")

    def get_highest_spender(self):
        return max(self.customers_data, key=lambda customer: sum(exp['amount'] for exp in customer.expenses), default=None)


class Customer:
    def __init__(self, name):  # Fixed constructor
        self.name = name
        self.expenses = []  

    def add_expense(self):
        amount = float(input("Enter expense amount to add: "))
        description = input("Enter description of the expense: ")
        category = input("Enter category of the expense: ")
        expense = {"amount": amount, "description": description, "category": category}
        self.expenses.append(expense)
        print(f"Added expense: {expense}")

    def remove_expense(self):
        amount = float(input("Enter expense amount to remove: "))
        for exp in self.expenses:
            if exp['amount'] == amount:
                self.expenses.remove(exp)
                print(f"Removed expense: {exp}")
                return
        print(f"Expense {amount} not found.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            for exp in self.expenses:
                print(f"Amount: {exp['amount']}, Description: {exp['description']}, Category: {exp['category']}")

    def update_expense(self):
        old_amount = float(input("Enter the expense amount to update: "))
        for exp in self.expenses:
            if exp['amount'] == old_amount:
                new_amount = float(input(f"Enter new expense amount to replace {old_amount}: "))
                new_description = input(f"Enter new description (previous: {exp['description']}): ")
                new_category = input(f"Enter new category (previous: {exp['category']}): ")
                exp['amount'] = new_amount
                exp['description'] = new_description
                exp['category'] = new_category
                print(f"Updated expense to {exp}")
                return
        print(f"Expense {old_amount} not found.")

    def exit_system(self):
        print("Exiting customer system...")


admin = Admin("abhi", "abhi22")


def create_customer():
    name = input("Enter customer name: ")
    return Customer(name)


def admin_menu():
    while True:
        print("\n--- Admin Menu ---")
        print("1. View all customer expenses")
        print("2. View highest spending customer")
        print("3. Exit admin")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin.view_expenses()
        elif choice == "2":
            admin.highest_spending()
        elif choice == "3":
            print("Exiting admin menu...")
            break
        else:
            print("Invalid choice, try again.")


def customer_menu(customer):
    while True:
        print("\n--- Customer Menu ---")
        print("1. Add an expense")
        print("2. Remove an expense")
        print("3. View expenses")
        print("4. Update an expense")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            customer.add_expense()
        elif choice == "2":
            customer.remove_expense()
        elif choice == "3":
            customer.view_expenses()
        elif choice == "4":
            customer.update_expense()
        elif choice == "5":
            customer.exit_system()
            break
        else:
            print("Invalid choice, try again.")


def start_menu():
    while True:
        print("\n--- Welcome to the Expense Tracker System ---")
        print("1. Admin Side")
        print("2. Customer Side")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")

            if admin.login(admin_username, admin_password):
                print("Admin logged in successfully.")
                admin_menu()
            else:
                print("Admin login failed.")

        elif choice == "2":
            customer = create_customer()
            admin.customers_data.append(customer)  
            customer_menu(customer)

        elif choice == "3":
            print("Exiting the system...")
            break

        else:
            print("Invalid choice, try again.")


start_menu()
