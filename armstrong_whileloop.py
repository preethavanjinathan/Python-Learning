num = int(input("Enter number: "))
temp = num
sum_arm = 0
digits = len(str(num))
while temp > 0:
    digit = temp % 10
    sum_arm += digit ** digits
    temp //=10
if sum_arm == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")