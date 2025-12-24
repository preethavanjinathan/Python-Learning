n = int(input())
values = input().split()
total = 0
for i in range(n):
    total = total + int(values[i])
average = total / n
print(average)
