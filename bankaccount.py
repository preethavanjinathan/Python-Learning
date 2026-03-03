from abc import ABC, abstractmethod

class BankAccount(ABC):

    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):

    def calculate_interest(self):
        return self.balance * 0.05

class CurrentAccount(BankAccount):

    def calculate_interest(self):
        return 0

s = SavingsAccount(10000)
c = CurrentAccount(10000)

print("Savings Interest:", s.calculate_interest())
print("Current Interest:", s.calculate_interest())





