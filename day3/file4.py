
x = 50
y = [10,20,30,40]


def writeFile(filename, data):
    filetxt = open(filename, 'a')
    for v in map(int, data):
        filetxt.write(v)
    filetxt.close()

writeFile('deneme.txt',y)