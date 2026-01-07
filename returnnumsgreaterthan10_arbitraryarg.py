def greater_than_10(*args):
    result = []
    for num in args:
        if num > 10:
            result.append(num)
    return result
print(greater_than_10(4, 12, 23, 37, 56))