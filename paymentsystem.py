from abc import ABC, abstractmethod

class Payment(ABC):

    def pay(self, amount):
        pass

class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")

class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")

class CashPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} in Cash")


payments = [CreditCardPayment(),
            UPIPayment(),
            CashPayment()
]

for p in payments:
    p.pay(1000)