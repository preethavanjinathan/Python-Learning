def calculator(a, b):
    def add(): return a + b
    def sub(): return a - b
    def mul(): return a * b
    def div(): return a / b

    print("Add:", add())
    print("Sub:", sub())
    print("Mul:", mul())
    print("Div:", div())

calculator(10, 2)