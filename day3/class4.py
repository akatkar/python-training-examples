from random import randint

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f'[{self.x},{self.y}]'

    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2)**(1/2)

a = Point(0,1)
b = Point(0,5)

print(a.distance(b))


# generate 1000 Points
allPoints = [Point(randint(-500,500), randint(-500,500)) for _ in range(100)]
print(len(allPoints))

print(allPoints)

origin = Point(0, 0)
dict = {origin.distance(p) : p for p in allPoints}
print(dict[min(dict)])

minDist = 1000
nearestPoint = origin
for p in allPoints:
    dist = origin.distance(p)
    if dist < minDist :
        minDist = dist
        nearestPoint = p

print(nearestPoint)
