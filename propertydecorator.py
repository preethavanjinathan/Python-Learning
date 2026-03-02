class Product:
    def __init__(self, price):
        self.__price = price

    def price(self):
        return self.__price

    def price(self, value):
        if value > 0:
            self.__price = value
        else:
            print("Invalid price")

p = Product(1000)
print(p.price)
p.price = 1500
print(p.price)