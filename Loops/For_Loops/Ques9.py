# banking system program
# 1. create a class called BankAccount with attributes like account_number, account_holder_name
# 2. create methods for deposit, withdraw, and display_balance
class BankAccount:
    def __init__(self, account_number, account_holder_name):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Account Holder: {self.account_holder_name}, Balance: {self.balance}")
# Example usage
account = BankAccount("123456789", "John Doe")  
account.deposit(1000)
account.withdraw(200)
account.display_balance()

