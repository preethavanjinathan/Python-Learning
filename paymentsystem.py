class Payment:
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class Cash(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Cash")

payments = [CreditCard(), UPI(), Cash()]

for p in payments:
    p.pay(1000)
