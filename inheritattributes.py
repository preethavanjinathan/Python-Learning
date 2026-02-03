class Vehicle:
    def __init__(self, type):
        self.type = type

class Car(Vehicle):
    pass

c = Car("Four Wheeler")
print(c.type)
