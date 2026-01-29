class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def yearly_salary(self):
        return self.salary * 12

e = Employee("Charles", 80000)
print("Yearly Salary:", e.yearly_salary())
