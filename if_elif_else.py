units = int(input("Enter units consumed: "))
if units <= 100:
    rate = 5
elif units <= 200:
    rate = 7
else:
    rate = 10
bill = units * rate
print(f"Units consumed: {units}")
print(f"Rate: {rate} per unit")
print(f"Total Bill: {bill}")
