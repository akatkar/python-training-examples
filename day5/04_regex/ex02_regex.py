import re

# def replaceWith(matched):
#     s1 = matched.group(0)
#     return '*'*len(s1)
#

def main():
    pattern = '(\d+)'
    data = 'there are 2024 birds in 217788888888 trees'
    result, count = re.subn(pattern, lambda m:'*'*len(m.group(0)), data)
    print(result)

if __name__ == '__main__':
    main()
