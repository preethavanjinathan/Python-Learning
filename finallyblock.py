try:
    f = open("sample.txt")
    print("File not found!")

except FileNotFoundError:
    print("File not found!")

finally:
    print("Execution completed.")
    