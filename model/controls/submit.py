from selene.support.shared import browser
from selene import command

def click_sbmt():
    browser.element('#submit').perform(command.js.click)
