import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # FIX: sqrt(n) is enough
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")  # FIX
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def power(base, exp):
    return base ** exp

print(is_prime(17))
print(factorial(5))
print(fibonacci(8))