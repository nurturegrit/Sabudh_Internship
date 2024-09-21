# Generator function for Fibonacci sequence
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# First 10 numbers in the Fibonacci sequence
for number in fibonacci_generator(10):
    print(number, end=" ")