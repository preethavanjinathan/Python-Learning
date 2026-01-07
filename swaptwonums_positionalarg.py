def swap(a, b):
    print("Before swapping;")
    print("a =", a, "b =", b)
    a, b = b, a
    print("After swapping:")
    print("a =", a, "b =", b)
swap(10, 5)