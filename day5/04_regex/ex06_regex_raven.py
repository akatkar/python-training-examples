import re

import re

def main():
    with open('raven.txt') as fh:
        for line in fh:
            s = re.sub('(Len|Neverm)ore', '###', line)
            print(s, end='')

if __name__ == "__main__":
    main()
