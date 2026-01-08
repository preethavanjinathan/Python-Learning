def find_key(key, **kwargs):
    return kwargs.get(key, "Key not found")
value = find_key("age", name="Preetha", age=19, city="Trichy")
print(value)