def calculator(a, b, operation="sub"):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    else:
        return "Invalid operation"
print(calculator(20, 10))