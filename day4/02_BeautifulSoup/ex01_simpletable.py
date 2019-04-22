from bs4 import BeautifulSoup

with open("simpletable.html") as fp:
    bs = BeautifulSoup(fp,"html.parser")

print(bs.title)
print(bs.title.text)

table = bs.find('table', "Simple Table")

# using iteration
# data = []
# for row in table.find_all("tr"):
#     for col in row.find_all("td"):
#         data.append(col.string.strip())
# print(data)

# using list comprehension
data = [col.string.strip() for row in table.find_all("tr") for col in row.find_all("td")]

print('Simple Table:', data)
