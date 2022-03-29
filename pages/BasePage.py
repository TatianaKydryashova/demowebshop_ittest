from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators, RegisterPageLocators, LoginPageLocators, UserPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

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

    def should_be_user_page(self):
        assert self.is_element_present(*BasePageLocators.USER_LINK), "probably login user"

    def should_be_change_password(self):
        assert self.is_element_present(*UserPageLocators.CHANGE_PASSWORD_RESULT), "probably change password"

