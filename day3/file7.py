x = 50
y = [10,20,30,40]


def writeFile(filename, data):
    with open(filename, 'a') as filetxt:
        try:
            for v in map(str, data):
                filetxt.write(v)
        except:
            print('exception raised')

writeFile('deneme.txt',y)