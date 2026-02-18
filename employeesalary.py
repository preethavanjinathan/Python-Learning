class Employee:
    def salary(self):
        pass

class FullTime(Employee):
    def salary(self):
        print("Full Time Salary = 30000")

class PartTime(Employee):
    def salary(self):
        print("Part Time Salary = 15000")

class Intern(Employee):
    def salary(self):
        print("Intern Salary = 8000")

employees = [FullTime(), PartTime(), Intern()]

for e in employees:
    e.salary()
