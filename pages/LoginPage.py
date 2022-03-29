from .BasePage import BasePage
from .locators import UserPageLocators, LoginPageLocators, BasePageLocators


class LoginPage(BasePage):
    def login_user(self, Email, Password):
        user_Email = self.browser.find_element(*LoginPageLocators.EMAIL)
        user_Email.send_keys(Email)
        user_Password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        user_Password.send_keys(Password)
        button_login = self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT)
        button_login.click()

    def change_password(self, old_password, new_password, confirm_password):
        user_page = self.browser.find_element(*BasePageLocators.USER_LINK)
        user_page.click()
        change_password = self.browser.find_element(*UserPageLocators.CHANGE_PASSWORD)
        change_password.click()
        user_old_password = self.browser.find_element(*UserPageLocators.OLD_PASSWORD)
        user_old_password.send_keys(old_password)
        user_new_password = self.browser.find_element(*UserPageLocators.NEW_PASSWORD)
        user_new_password.send_keys(new_password)
        user_confirm_password = self.browser.find_element(*UserPageLocators.CONFIRM_PASSWORD)
        user_confirm_password.send_keys(confirm_password)
        button_change_password = self.browser.find_element(*UserPageLocators.CHANGE_PASSWORD_SUBMIT)
        button_change_password.click()


