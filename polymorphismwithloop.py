class Dog:
    def sound(self):
        print("Dog barks")

class Cat:
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat()]

for a in animals:
    a.sound()
