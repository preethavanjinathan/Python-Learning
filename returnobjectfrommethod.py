class Number:
    def __init__(self, value):
        self.value = value

    def double(self):
        return Number(self.value * 2)

n1 = Number(5)
n2 = n1.double()
print(n2.value)
