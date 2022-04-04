from .BasePage import BasePage
from .locators import UserPageLocators, BasePageLocators
from data.URL import URL


class UserPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.url = URL.USER_URL

    def change_password(self, old_password, new_password, confirm_password):
        self.browser.find_element(*BasePageLocators.USER_LINK).click()
        self.browser.find_element(*UserPageLocators.CHANGE_PASSWORD).click()
        self.browser.find_element(*UserPageLocators.OLD_PASSWORD).send_keys(old_password)
        self.browser.find_element(*UserPageLocators.NEW_PASSWORD).send_keys(new_password)
        self.browser.find_element(*UserPageLocators.CONFIRM_PASSWORD).send_keys(confirm_password)
        self.browser.find_element(*UserPageLocators.CHANGE_PASSWORD_SUBMIT).click()