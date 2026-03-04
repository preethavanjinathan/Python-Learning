try:
    num = int(input("Enter number: "))
    result = 100 / num
    print("Result:", result)

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("Cannot divide by zero!")