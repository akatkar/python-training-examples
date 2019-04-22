import re

SEARCH_PATTERN = 'aa[bc]*dd'
pattern = re.compile(SEARCH_PATTERN)

while True:
    enter = input('Enter a line (q to Quit) : ')
    if enter.lower() == 'q':
        break
    if pattern.search(enter):
        print(f'{enter} matched for {SEARCH_PATTERN}')
    else:
        print('NO MATCH !')


