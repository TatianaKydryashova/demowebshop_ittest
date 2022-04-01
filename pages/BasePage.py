from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators, RegisterPageLocators, LoginPageLocators, UserPageLocators
from data.URL import URL


class BasePage():
    def __init__(self, browser):
        self.browser = browser
        self.url = URL.BASE_URL

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def go_to_register_page(self):
        link = self.browser.find_element(*BasePageLocators.REGISTER_LINK)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_user_page(self):
        link = self.browser.find_element(*BasePageLocators.USER_LINK)
        link.click()

    def should_be_register_user(self):
        assert self.is_element_present(*RegisterPageLocators.RESULT), "probably register user"

    def should_be_error_register_user(self):
        assert self.is_element_present(*RegisterPageLocators.ERROR_REGISTER_NAME), "First name is required"

    def should_be_error_password_register_user(self):
        assert self.is_element_present(*RegisterPageLocators.ERROR_REGISTER_PASSWORD), "The password should have at least 6 characters"

    def should_be_error_login_message(self):
        assert self.is_element_present(
            *LoginPageLocators.ERROR_LOGIN_NAME), "Login was unsuccessful. Please correct the errors and try again."

    def should_be_error_change_password(self):
        assert self.is_element_present(
            *UserPageLocators.ERROR_CHANGE_PASSWORD), "Login was unsuccessful. Please correct the errors and try again."

    def should_be_user_page(self):
        assert self.is_element_present(*BasePageLocators.USER_LINK), "probably login user"

    def should_be_change_password(self):
        assert self.is_element_present(*UserPageLocators.CHANGE_PASSWORD_RESULT), "probably change password"

