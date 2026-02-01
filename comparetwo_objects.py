class Person:
    def __init__(self, age):
        self.age = age

p1 = Person(21)
p2 = Person(19)

if p1.age > p2.age:
    print("p1 is older")
else:
    print("p2 is older")
