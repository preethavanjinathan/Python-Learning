def check_prime(n):
    def inner():
        if n <= 1:
            return "Not Prime"
        for i in range(2, n):
            if n % i == 0:
                return "Not Prime"
        return "Prime"
    return inner()
print(check_prime(17))
print(check_prime(30))
