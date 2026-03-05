class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))

    if age < 18:
        raise AgeError("Age must be 18 or above")

    print("Eligible to vote")

except AgeError as e:
    print("Error:", e)







