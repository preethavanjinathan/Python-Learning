def modify(lst):
    lst.append(10)
a = [1, 2]
b = a.copy()
modify(b)
print(a, b)
