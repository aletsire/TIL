# Recursion
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))

# For
def fib_for(n):
    if n<2:
        return n
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a+b
        return b
print(fib_for(5))

# While
def fib_while(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a+b
print(fib_while(5))