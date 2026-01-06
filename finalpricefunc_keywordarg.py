def final_price(price, discount=0):
    return price - discount
amount = final_price(price=1000, discount=300)
print("Final price:", amount)
