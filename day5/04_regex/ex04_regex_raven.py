import re

def main():
    with open('raven.txt') as fh:
        pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
        for line in fh:
            if pattern.search(line):
                print(line, end='')

if __name__ == "__main__":
    main()
