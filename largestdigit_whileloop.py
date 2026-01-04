num = int(input("Enter number: "))
largest = 0
while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num //= 10
print("Largest digit =", largest)
