def min_of_three(a, b, c):
    if a <= b and a <= c:
        return a
    if b <= a and b <= c:
        return b
    else:
        return c
print(min_of_three(10, 20, 30))