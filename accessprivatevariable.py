class Car:
    def __init__(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

c = Car(80)
print(c.get_speed())
