import pytest

from .BasePage import BasePage
from .locators import UserPageLocators, LoginPageLocators, BasePageLocators
from data.URL import URL


@pytest.mark.smoke
class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.url = URL.LOGIN_PAGE_URL

    def login_user(self, Email, Password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(Email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(Password)
        self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT).click()

    def change_password(self, old_password, new_password, confirm_password):
        self.browser.find_element(*BasePageLocators.USER_LINK).click()
        self.browser.find_element(*UserPageLocators.CHANGE_PASSWORD).click()
        self.browser.find_element(*UserPageLocators.OLD_PASSWORD).send_keys(old_password)
        self.browser.find_element(*UserPageLocators.NEW_PASSWORD).send_keys(new_password)
        self.browser.find_element(*UserPageLocators.CONFIRM_PASSWORD).send_keys(confirm_password)
        self.browser.find_element(*UserPageLocators.CHANGE_PASSWORD_SUBMIT).click()


