# Pythagorean triples

# Generator with iteration
def pyth2(n):
    for a in range(1,n):
        for b in range(a,n):
            for c in range(b,n):
                if a**2 + b**2 == c**2:
                    yield (a,b,c)


# Generator with comprehension
def pyth_gen(n):
    return ((a,b,c) for a in range(1,n) for b in range(a,n) for c in range(b,n) if a**2 + b**2 == c**2)

# test the generator
print(pyth_gen(50))

for i in pyth_gen(50):
    print(i)