def max_value_kw(**kwargs):
    numbers = []
    for value in kwargs.values():
        if isinstance(value, (int, float)):
            numbers.append(value)
            return max(numbers) if numbers else None
print(max_value_kw(a=10, b=20, c=9))
