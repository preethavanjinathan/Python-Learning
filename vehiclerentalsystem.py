from abc import ABC, abstractmethod

class Vehicle(ABC):

    def rent_cost(self, days):
        pass

class Car(Vehicle):

    def rent_cost(self, days):
        return days * 1500

class Bike(Vehicle):

    def rent_cost(self, days):
        return days * 500


c = Car()
b = Bike()

print("Car Rent:", c.rent_cost(3))
print("Bike Rent:", b.rent_cost(3))