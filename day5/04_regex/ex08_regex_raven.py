import re

import re

def replaceWith(matched):
    return '*'*len(matched.group(0))

def main():
    with open('raven.txt') as fh:
        pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
        for line in fh:
            if re.search(pattern, line):
                print(pattern.sub(replaceWith, line),end='')

if __name__ == "__main__":
    main()
