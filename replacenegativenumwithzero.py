arr = [2, -5, 7, -1, 3]
for i in range(len(arr)):
    if arr[i] < 0:
        arr[i] = 0
print(arr)