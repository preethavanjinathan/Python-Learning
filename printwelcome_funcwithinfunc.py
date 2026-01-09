def outer():
    def inner():
        print("Welcome")
    inner()
outer()