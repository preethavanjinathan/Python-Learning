from abc import ABC, abstractmethod

class Employee(ABC):

    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):

    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):

    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


f = FullTimeEmployee(60000)
p = PartTimeEmployee(30, 600)

print("Full Time Salary:", f.calculate_salary())
print("Part Time Salary:", p.calculate_salary())