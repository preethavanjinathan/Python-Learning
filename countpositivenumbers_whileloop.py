count = 0
while True:
    num = int(input("Enter number: "))
    if num < 0:
        break
    if num > 0:
        count += 1
print("Count of positive numbers =", count)
