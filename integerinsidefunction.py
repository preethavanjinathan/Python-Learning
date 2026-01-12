def func(x):
    print(id(x))
    x = x + 1
    print(id(x))
a = 10
print(id(a))
func(a)
print(a)