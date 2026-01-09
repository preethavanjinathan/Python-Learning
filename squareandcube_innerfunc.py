def calculate(n):
    def inner():
        print("Square:", n * n)
        print("Cube:", n * n * n)
    inner()
calculate(2)