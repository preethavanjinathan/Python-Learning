class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        print("Current Balance:", self.__balance)

atm = ATM(2000)
atm.deposit(500)
atm.withdraw(1000)
atm.check_balance()
