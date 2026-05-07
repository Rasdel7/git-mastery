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
    return s == s[::-1]  # BUG: case sensitive, "Racecar" fails

def word_count(s):
    words = s.split(" ")  # BUG: breaks on multiple spaces
    return len(words)

def capitalize_words(s):
    return s.title()

print(is_palindrome("Racecar"))   # Returns False — wrong
print(word_count("hello  world")) # Returns 3 — wrong