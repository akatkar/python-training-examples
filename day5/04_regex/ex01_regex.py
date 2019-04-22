import re

data = ['Mustafa Kemal was born in <<1881>>',
'He has read <<3997>> books during his life',
'There is noting here']

def main():
    pattern = re.compile("<<[\d]*>>")
    for line in data:
        mo = pattern.search(line)
        if mo:
            value = mo.group(0)
            print(value)

if __name__ == '__main__': main()

