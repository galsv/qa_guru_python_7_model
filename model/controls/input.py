import sys
from selene.support.shared import browser
from selenium.webdriver import Keys


def type_by_id(id, value):
    browser.element(id).type(value)

def type_date_of_bithday(date):
    name_os = sys.platform
    if name_os == 'win32':
        browser.element("#dateOfBirthInput").send_keys(Keys.CONTROL + 'a').type(date).press_enter()
    else:
        browser.element("#dateOfBirthInput").send_keys(Keys.COMMAND + 'a').type(date).press_enter()