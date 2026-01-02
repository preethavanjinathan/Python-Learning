temp = int(input("Enter temperature in Celsius: "))
if temp > 35:
    print("Hot")
elif 25 <= temp <= 35:
    print("Warm")
elif 15 <= temp <= 24:
    print("Cool")
else:
    print("Cold")
