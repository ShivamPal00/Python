class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.__balance}")
        else:
            print("Insufficient funds.")

# Creating a BankAccount object
account = BankAccount("123456789", 1000)

# Accessing account details using public methods
print("Account Number:", account.get_account_number())
print("Balance:", account.get_balance())

# Trying to access private attributes directly (not recommended)
# print("Account Number:", account.__account_number)  # This will throw an AttributeError

# Depositing and withdrawing funds
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)  # This will result in "Insufficient funds." message
