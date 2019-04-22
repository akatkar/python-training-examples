ex=[item**2 for item in range(1,10,2)]

print(ex)

example = [item for item in range(1, 10, 2)]
print(example)

given = [1,2,3,4,5,6]


def divide(lst, n):
    return [lst[i*n:(i+1)*n] for i in range(len(lst)//n)]

x = [given[i*3:(i+1)*3] for i in range(len(given)//3)]
print(x)

for a in x:
    for b in a:
        print(b, end=' ')
    print()

