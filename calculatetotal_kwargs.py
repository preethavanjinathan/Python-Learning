def calculate_total(*args, discount=0, **kwargs):
    total = sum(args)
    discount_amount = total * discount / 100
    return total - discount_amount

print(calculate_total(100, 200, 300, discount=10))
