x = 50
y = [10,20,30,40]


def writeFile(filename, data):
    filetxt = open(filename, 'a')
    try:
        for v in map(str, data):
            filetxt.write(v)
    except:
        print('exception raised')
    finally:
        filetxt.close()
        print('file closed')

writeFile('deneme.txt',y)