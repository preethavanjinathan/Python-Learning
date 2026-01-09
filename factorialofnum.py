def factorial(n):
    def inner():
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    return inner()
print(factorial(3))
