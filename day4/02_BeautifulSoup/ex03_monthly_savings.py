from bs4 import BeautifulSoup

with open("index.html") as fp:
    bs = BeautifulSoup(fp,"html.parser")

print(bs.title)
print(bs.title.text)

def findTable(caption):
    for table in bs.find_all("table"):
        if table.find("caption").text.strip() == caption:
            return table


def writeHeader(headers):
    for header in headers:
        print(header, '\t'*2, end='');
    print()
    for header in headers:
        print('-'*len(header), '\t'*2, end='');
    print()


savings = findTable("Monthly savings")
if savings:
    headers = [header.string for header in savings.find_all("th")]
    valueList = [col.text.strip() for row in savings.find_all("tr") for col in row.find_all("td")]
    values = [valueList[i * len(headers):(i + 1) * len(headers)] for i in range(len(valueList) // len(headers))]

    writeHeader(headers)

    for value in values:
        for i in value:
            print(i, '\t'*2, end='')
        print()