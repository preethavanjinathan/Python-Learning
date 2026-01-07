def count_strings(*args):
    count = 0
    for value in args:
        if type(value) == str:
            count += 1
    return count
print(count_strings("Preetha", 19, "Python", 5.5))
