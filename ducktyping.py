class Car:
    def move(self):
        print("Car is moving")

class Bike:
    def move(self):
        print("Bike is moving")

def start(vehicle):
    vehicle.move()

start(Car())
start(Bike())