from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        print("Circle area calculated")

class Rectangle(Shape):
    def area(self):
        print("Rectangle area calculated")

shapes = [Circle(), Rectangle()]

for s in shapes:
    s.area()