def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def is_palindrome(s):
    s = s.lower().strip()  # FIX: normalize before comparing
    return s == s[::-1]

def word_count(s):
    words = s.split()  # FIX: split() without args handles multiple spaces
    return len(words)

def capitalize_words(s):
    return s.title()

print(is_palindrome("Racecar"))   # Now True
print(word_count("hello  world")) # Now 2