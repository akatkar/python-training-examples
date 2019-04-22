import mechanicalsoup

# Create a browser object
browser = mechanicalsoup.StatefulBrowser()

url = "https://www.n11.com"
page = browser.get(url)

for form in page.soup.findAll('form'):
    print(form)
