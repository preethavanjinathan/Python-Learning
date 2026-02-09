class Bank:
    def interest(self):
        print("Bank interest")

class SavingsAccount(Bank):
    def interest(self):
        print("Savings account interest")

s = SavingsAccount()
s.interest()
