def writeFile(filename, data):
    filetxt = open(filename, 'a')
    for v in data:
        filetxt.write(v)
    filetxt.close()

def readFile(filename):
    filetxt = open(filename, 'r')
    result = filetxt.readlines()
    filetxt.close()
    return result

lines = readFile('deneme.txt')
print(lines)

modList = lines[:2]
modList.append("line 3\n")
for i in lines[2:]:
    modList.append(i)

print(modList)
writeFile("deneme2.txt",modList)