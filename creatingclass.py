class Person:
    def __init__(self, name):
        self.__name = name

    def display_name(self):
        print("Name:", self.__name)

p = Person("Preetha")
p.display_name()