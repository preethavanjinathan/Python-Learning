def student_data(*args, **kwargs):
    print("Subjects:")
    for subject in args:
        print("-", subject)
    print("\nStudent Details:")
    for key, value in kwargs.items():
        print(key, ":", value)
student_data("Maths", "Physics", "Chemistry",
             name="Preetha", roll_no=31, marks=95)
