a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator(+, -, *, /): ")
match op:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        print("Result:", a / b if b != 0 else "Cannot divide by zero")
    case _:
        print("Invalid operator")
