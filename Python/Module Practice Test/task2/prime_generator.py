# Generator function for prime numbers up to n
def prime_generator(n):
    for num in range(2, n+1):
        prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            yield num

# Prime numbers up to 100
for prime in prime_generator(100):
    print(prime, end=" ")