import re

import re

def main():
    with open('raven.txt') as fh:
        for line in fh:
            match = re.search('(Len|Neverm)ore', line)
            if match:
                print(line.replace(match.group(), '###'),end='')

if __name__ == "__main__":
    main()
