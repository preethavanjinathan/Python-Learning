def validate(password):
    def inner():
        if len(password) >= 8:
            return "Strong password"
        else:
            return "Weak password"
    return inner()
print(validate("python123"))