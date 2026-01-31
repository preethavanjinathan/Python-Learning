class Employee:
    def __init__(self):
        self.name = input("Enter name: ")
        self.salary = int(input("Enter salary: "))

    def display(self):
        print(self.name, self.salary)

e = Employee()
e.display()
