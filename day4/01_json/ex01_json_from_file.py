import json

# NOTICE THAT this time we are reading from file directly
with open("sample.json") as sample:
    a = json.load(sample)
print(a)
