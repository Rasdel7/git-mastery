def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):  # BUG: slow, should go to sqrt(n)
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)  # BUG: no negative number check

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
print(factorial(-1))  # Will cause infinite recursion