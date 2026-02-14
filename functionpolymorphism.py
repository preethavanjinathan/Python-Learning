class Student:
    def info(self):
        print("I am a Student")

class Teacher:
    def info(self):
        print("I am a Teacher")

def display(obj):
    obj.info()

display(Student())
display(Teacher())