
def gcd2(a, b):
    while b!=0:
        a, b = b, a % b
    return a


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


print(gcd(12,7))
print(gcd(10,5))

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]

result = list(filter(lambda x:x in b, a))
print(result)

squares = map(lambda x: x**2, range(10))
answer = list(filter(lambda x: 5 < x < 50, squares))
print(answer)
