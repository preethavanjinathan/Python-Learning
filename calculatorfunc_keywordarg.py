def calculate(*, a, b, operation):
    if operation == "add":
        print("Result:", a + b)
    elif operation == "sub":
        print("Result:", a - b)
    elif operation == "mul":
        print("Result:", a * b)
    else:
        print("Invalid operation")
calculate(a=10, b=2, operation="add")
calculate(a=10, b=2, operation="sub")
calculate(a=10, b=2, operation="mul")
