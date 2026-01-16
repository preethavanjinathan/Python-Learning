nums = [10, 20, 30, 40, 50]
element = 40
index = -1
for i in range (len(nums)):
    if nums[i] == element:
        index = i
        break

print("Index:", index)