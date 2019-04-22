from bs4 import BeautifulSoup

with open("index.html") as fp:
    bs = BeautifulSoup(fp,"html.parser")

print(bs.title)
print(bs.title.text)


def findTable(caption):
    for table in bs.find_all("table"):
        if table.find("caption").text.strip() == caption:
            return table


savings = findTable("Monthly savings")
if savings:
    headers = [header.string for header in savings.find_all("th")]

    values = []
    for row in savings.find_all("tr"):
        temp = [col.text.strip() for col in row.find_all("td") if col]
        if len(temp) > 0:
            values.append(temp)

    print(headers[0], "\t\t", headers[1])
    print('-'*len(headers[0]), "\t\t", '-'*len(headers[1]))

    for value in values:
        print(value[0], "\t\t", value[1])
