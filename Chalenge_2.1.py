class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited ₹{amount}.
          New balance: ₹{self.__account_balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew ${amount}. New balance: ₹{self.__account_balance}"
        else:
            return "Invalid withdrawal amount or insufficient balance."

    def display_balance(self):
        return f"Account balance for {self.__account_holder_name}: ₹{self.__account_balance}"

# Input from the user to create a BankAccount instance
account_number = input("Enter account number: ")
account_holder_name = input("Enter account holder name: ")
initial_balance = float(input("Enter initial balance: "))

account = BankAccount(account_number, account_holder_name, initial_balance)

# Testing deposit and withdrawal
print(account.display_balance())

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        deposit_amount = float(input("Enter the deposit amount: "))
        print(account.deposit(deposit_amount))
    elif choice == "2":
        withdrawal_amount = float(input("Enter the withdrawal amount: "))
        print(account.withdraw(withdrawal_amount))
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

print("Thank you for using our banking service!")



