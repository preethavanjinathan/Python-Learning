def sum_positive(*args):
    total = 0
    for num in args:
        if num > 0:
            total += num
    return total
print(sum_positive(-5, 9, -9, 34, 67))