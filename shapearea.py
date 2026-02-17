class Circle:
    def area(self):
        r = 3
        print("Circle:", 3.14 * r * r)

class Rectangle:
    def area(self):
        l, b = 4, 5
        print("Rectangle:", l * b)

class Triangle:
    def area(self):
        b, h = 6, 2
        print("Triangle:", 0.5 * b * h)

shapes = [Circle(), Rectangle(), Triangle()]

for s in shapes:
    s.area()
