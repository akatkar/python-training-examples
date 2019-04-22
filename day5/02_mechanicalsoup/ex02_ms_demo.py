import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()

browser.open("http://httpbin.org/")

print(browser.get_url())

browser.follow_link("forms")

# page = browser.get_current_page()
# print(page)
#
# print(browser.get_current_page().find_all('legend'))
#
browser.select_form('form[action="/post"]')
# browser.get_current_form().print_summary()
# #
# # For text fields, it’s simple: just give a value for input element based on their name attribute:
browser["custname"] = "Ali"
browser["custtel"] = "+90 532 555 6677"
browser["custemail"] = "nobody@example.com"
browser["comments"] = "This pizza looks really good :-)"
# #
#For radio buttons: radio buttons have several input tag with the same name and different values,
# just select the one you need
# ("size" is the name attribute, "medium" is the "value" attribute of the element we want to tick):
browser["size"] = "medium"
# #
# For checkboxes, one can use the same mechanism to check one box:
browser["topping"] = "bacon"
# But we can also check any number of boxes by assigning a list to the field:
browser["topping"] = ("bacon", "cheese")
#
# # # we can launch on a browser
# # browser.launch_browser()
# # # or we can print
# browser.get_current_form().print_summary()
# #
# submit the form
response = browser.submit_selected()

print(response.text)