import json

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

with open("dict.json","w" ) as file:
    file.write(json.dumps(dict1))
