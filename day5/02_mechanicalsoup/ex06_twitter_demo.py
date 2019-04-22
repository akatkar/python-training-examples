import mechanicalsoup
import getpass
"""
YOU SHOULD RUN FROM TERMINAL
getpass does not work from pycharm
"""

def main():
    URL = 'https://twitter.com/login'
    LOGIN = 'alikatkar@hotmail.com'
    PASSWORD = getpass.getpass()
    TWITTER_NAME = 'alikatkar'

    # Create a browser object
    browser = mechanicalsoup.StatefulBrowser()

    # request Twitter login page
    login_page = browser.get(URL)

    # we grab the login form
    login_form = login_page.soup.find('form', {'class': 'signin'})

    browser.select_form(login_form)
    browser['session[username_or_email]'] = LOGIN
    browser['session[password]'] = PASSWORD
    # browser.get_current_form().print_summary()
    resp = browser.submit_selected()

    # verify we are now logged in
    page = browser.get_current_page()
    print(page)

if __name__ == '__main__':
    main()
