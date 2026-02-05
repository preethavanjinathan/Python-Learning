class Maths:
    def add(self, a, b):
        return a + b

class AdvancedMaths(Maths):
    pass

obj = AdvancedMaths()
print(obj.add(10, 20))
