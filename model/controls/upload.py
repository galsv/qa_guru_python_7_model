from selene.support.shared import browser
from utils import path


def picture_up(picture: str):
    browser.element("#uploadPicture").send_keys(path.to_resource(picture))