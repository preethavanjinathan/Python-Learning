def bill(amount, tax=5, discount=0):
    tax_amount = (amount * tax) / 100
    final_amount = (amount + tax_amount - discount)
    return final_amount
print(bill(1000))
print(bill(1000, 10, 100))