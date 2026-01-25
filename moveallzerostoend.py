arr = [0, 1, 0, 3, 12]
index = 0
for i in arr:
    if i != 0:
        arr[index] = i
        index += 1
for i in range(index, len(arr)):
    arr[i] = 0
print(arr)