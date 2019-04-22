
def fibo(n):
    a, b = 0, 1
    while a < n:
        yield a
        a,b = b, a+b


for i in fibo(30):
    print(i)

def fiboN(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a,b = b, a+b

for i in fiboN(50):
    print(i)
