def count_kwargs(**kwargs):
    return len(kwargs)
result = count_kwargs(a=10, b=20, c=30)
print(result)