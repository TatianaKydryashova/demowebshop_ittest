from .BasePage import BasePage
from .locators import  LoginPageLocators
from data.URL import URL


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.url = URL.LOGIN_PAGE_URL

    def login_user(self, Email, Password):

        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(Email)
        self.browser.find_element(*LoginPageLocators.PASSWORD).send_keys(Password)
        self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT).click()







