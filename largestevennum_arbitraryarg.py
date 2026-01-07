def largest_even(*args):
    evens = []
    for num in args:
        if num % 2 == 0:
            evens.append(num)
    return max(evens)
print(largest_even(3, 10, 7, 8, 68, 5))
