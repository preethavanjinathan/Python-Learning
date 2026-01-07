def multiply_all(*args):
    product = 1
    for num in args:
        product *= num
    return product
print(multiply_all(2,3,4))