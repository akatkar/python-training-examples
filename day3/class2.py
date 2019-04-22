
class Rational:
    counter = 0

    def __init__(self,a,b):
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a % b)

        cd = gcd(a,b)
        self.a = a // cd
        self.b = b // cd
        Rational.counter += 1

    def __add__(self, other):
        a = self.a * other.b + other.a * self.b
        b = self.b * other.b
        return Rational(a,b)

    def __sub__(self, other):
        a = self.a * other.b - other.a * self.b
        b = self.b * other.b
        return Rational(a,b)

    def __mul__(self, other):
        a = self.a * other.a
        b = self.b * other.b
        return Rational(a,b)

    def __invert__(self):
        return Rational(self.b, self.a)

    def __truediv__(self, other):
        return self * ~other

    def __floordiv__(self, other):
        return self / other

    def __str__(self):
        return '{}/{}'.format(self.a, self.b)

r1 = Rational(1,2)
print(r1)
r2 = Rational(1,3)
print(r2)

r3 = r1 + r2
print(r3)
r4 = Rational(6,7)
r5 = r3 + r4
print(r5)

r6 = r1 * r2
print(r6)
r7 = r1 / r2
print(r7)

r7 = r1 // r2
print(r7)

r8 = ~r7
print(r8)

r9 = Rational(10,20)
print(r9)

print(r9.counter)