try:
    lst = [10, 20, 30, 40]
    index = int(input("enter index: "))
    print(lst[index])

except IndexError:
    print("Index out of range!")