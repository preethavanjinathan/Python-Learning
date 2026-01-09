def maximum(a, b):
    def inner():
        return a if a > b else b
    return inner()
print(maximum(10, 35))
