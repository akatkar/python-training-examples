
def squares(n):
    for i in range(n):
        yield i**2

for i in squares(10):
    print(i)

print(list(squares(10)))

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True


def primes(n):
    for i in range(n):
        if isPrime(i):
            yield i

for i in primes(100):
    print(i)