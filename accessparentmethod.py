class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    pass

obj = Child()
obj.show()
