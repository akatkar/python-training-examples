import re


def main():
    with open('raven.txt') as fh:
        pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
        newPoem = []
        for line in fh:
            if re.search(pattern, line):
                newPoem.append(pattern.sub(lambda m:'*'*len(m.group(0)), line))
            else: newPoem.append(line)

        # newPoem = [i if re.search(pattern, line) pattern.sub(lambda m: '*' * len(m.group(0)), line)  else line for line in fh ]

        for line in newPoem:
            print(line, end='')

if __name__ == "__main__":
    main()
