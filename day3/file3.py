
filetxt = open('deneme.txt', 'r')
print(filetxt.read())
filetxt.clo1se()

filetxt = open('deneme.txt', 'r')
a = filetxt.readline(200)
print(a,end='')
print(filetxt.readline(),end='')
print(filetxt.readline(),end='')
print(filetxt.readline(),end='')
filetxt.close()
print()

filetxt = open('deneme.txt', 'r')
print(filetxt.readlines(),end='')
filetxt.close()

