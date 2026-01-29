class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

acc = BankAccount(5000)
acc.deposit(1500)
acc.withdraw(500)
print("Balance:", acc.balance)
