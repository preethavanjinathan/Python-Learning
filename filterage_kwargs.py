def filter_age(**kwargs):
    result = {}
    for name, age in kwargs.items():
        if isinstance(age, int) and age > 18:
            result[name] = age
    return result
print(filter_age(Preetha=20, Anu=17))
