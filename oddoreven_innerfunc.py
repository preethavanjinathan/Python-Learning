def check_number(n):
    def inner():
        return "Even" if n % 2 == 0 else "Odd"
    return inner()
print(check_number(7))
