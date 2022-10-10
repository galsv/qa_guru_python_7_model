from selene import command, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss
from model.controls import input, dropdown, modal, upload
from typing import Tuple
from tests.test_data.users import Subject, Hobby


def given_opened():
    browser.open('/automation-practice-form')
    ads = ss('[id^=google_ads][id$=container__]')
    if ads.with_(timeout=10).wait.until(have.size_greater_than_or_equal(3)):
        ads.perform(command.js.remove)

def set_first_name(value: str):
    input.type_by_id('#firstName', value)


def set_last_name(value: str):
    input.type_by_id('#lastName', value)


def set_email(value: str):
    input.type_by_id('#userEmail', value)


def set_gender(value: str):
    browser.element(f'[id^=gender-radio][value={value}]').perform(command.js.click)


def set_user_number(value: str):
    input.type_by_id('#userNumber', value)


def set_date_of_birthday(value: str):
    input.type_date_of_bithday(value)


def add_subjects(values: Tuple[Subject]):
    for subject in values:
        browser.element('#subjectsInput').type(subject.value).press_enter()


def select_hobbies_cb(values: Tuple[Hobby]):
    for hobby in values:
        browser.all('[id^=hobbies]').by(have.value(hobby.value)).first.element(
            '..'
        ).click()


def upload_picture(value: str):
    upload.picture_up('#uploadPicture', value)

def set_current_address(value: str):
    input.type_by_id('#currentAddress', value)


def scroll_to_bottom():
    browser.element('#state').perform(command.js.scroll_into_view)


def set_state(value: str):
    dropdown.select(browser.element('#state'), value)


def set_city(value: str):
    dropdown.select(browser.element('#city'), value)


def should_have_submitted(data):
    rows = modal.dialog.all('tbody tr')
    for row, value in data:
        rows.element_by(have.text(row)).all('td')[1].should(have.exact_text(value))