def change(s):
    print(id(s))
    s = s.upper()
    print(id(s))

name = "python"
change(name)
print(name)
