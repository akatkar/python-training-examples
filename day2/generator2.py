def primes(n):
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    for i in range(n):
        if isPrime(i):
            yield i

for i in primes(100):
    print(i, end=",")
print()