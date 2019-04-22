def x(a):
    return a ** 3
a = 3
b = x(3)

print(f"{a}^3 = {b}")

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

print(-2, isPrime(-2))
print(10, isPrime(10))

primes = []
for i in range(100):
    if isPrime(i):
        primes.append(i)

print(primes)

def isPalindrome(n):
    s = str(n)
    return s == s[::-1]

print(isPalindrome(1234))
print(isPalindrome(12321))
