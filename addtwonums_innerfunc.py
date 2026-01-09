def add(a, b):
    def inner():
        return a + b
    return inner()
print(add(10, 20))