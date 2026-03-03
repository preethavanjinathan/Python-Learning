from abc import ABC, abstractmethod

class Shape(ABC):

    def area(self):
        pass

class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

s = Square(5)
print("Area:", s.area())