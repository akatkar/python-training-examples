from bs4 import BeautifulSoup

with open("index.html") as fp:
    bs = BeautifulSoup(fp,"html.parser")


def findTable(caption):
    for table in bs.find_all("table"):
        if table.find("caption").text.strip() == caption:
            return table

savings = findTable("Monthly savings")
if savings:
    headers = [header.string for header in savings.find_all("th")]
    valueList = [col.text.strip() for row in savings.find_all("tr") for col in row.find_all("td")]
    values = [valueList[i * len(headers):(i + 1) * len(headers)] for i in range(len(valueList) // len(headers))]

    values.insert(0, ['-'*len(header) for header in headers])
    values.insert(0, headers)

    for row in values:
        for col in row:
            print(f"{col:20}", end='')
        print()