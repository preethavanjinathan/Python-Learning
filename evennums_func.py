def even_nums(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens
print(even_nums([1, 2, 3, 4, 5, 6]))