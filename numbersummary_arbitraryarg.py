def numbers_summary(*args):
    total_count = len(args)
    total_sum = sum(args)
    maximum = max(args)
    minimum = min(args)
    return total_count, total_sum, maximum, minimum
print(numbers_summary(10, 20, 15, 45, 68))
