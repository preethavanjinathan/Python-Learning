class Vehicle:
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

c = Car()
b = Bike()
c.start()
b.start()
