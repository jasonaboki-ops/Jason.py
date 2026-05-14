# Base class
]

class Account:
    def __init__(self, owner, balance=0, withdraw_limit=1000):
        self.owner = owner
        self.balance = balance
        self.withdraw_limit = withdraw_limit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount} deposited successfully.")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
        else:
            print("insufficient balance.")

    def display_balance(self):
        print(f"Current balance: $ {self.balance}")



# Savings Account inheriting from Account
class SavingsAccount(Account):
    withdraw_limit = 100

    def withdraw(self, amount):
        if amount > self.withdraw_limit:

            print(f"Withdrawal failed! Limit is {self.withdraw_limit}.")
        elif amount > self.balance:
            print("insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")


acc1 = SavingsAccount("Jason",1000)

acc1.display_balance()

acc1.withdraw(50)
acc1.display_balance()

acc1.withdraw(150)
acc1.display_balance()