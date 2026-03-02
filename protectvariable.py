class Employee:
    def __init__(self, salary):
        self._salary = salary

class Manager(Employee):
    def show_salary(self):
        print("Salary:", self._salary)

m = Manager(50000)
m.show_salary()
