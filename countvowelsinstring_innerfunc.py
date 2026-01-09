def count_vowels(s):
    def inner():
        count = 0
        for ch in s.lower():
            if ch in "aeiou":
                count += 1
        return count
    return inner()
print(count_vowels("Preetha"))
