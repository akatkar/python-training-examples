import re

data = """
Mustafa Kemal was born in <<1881>>
He has read <<3997>> books during his life
There is noting here
"""

def main():
    print(data)
    pattern = re.compile("<<[\d]*>>")
    mo = pattern.search(data)
    print(mo.span())

    lst = pattern.findall(data)
    print(lst)
    for matched in pattern.finditer(data):
        print(matched.group())

if __name__ == '__main__':
    main()