def string_values(**kwargs):
    strings = []
    for value in kwargs.values():
        if isinstance(value, str):
            strings.append(value)
    return strings
print(string_values(name = "Preetha", sub = "Python", age = 19))