def salary(basic, hra=20, da=10):
    hra_amount = (basic * hra) / 100
    da_amount = (basic * da) / 100
    total_salary = basic + hra_amount + da_amount
    return total_salary
print(salary(10000))
print(salary(10000, 25, 15))