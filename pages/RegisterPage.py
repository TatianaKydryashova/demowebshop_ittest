from .BasePage import BasePage
from .locators import RegisterPageLocators, BasePageLocators


class RegisterPage(BasePage):
    def register_new_user(self, firstName, lastName, Email, Password, Confirm_Password):
        user_firstName = self.browser.find_element(*RegisterPageLocators.FIRST_NAME)
        user_firstName.send_keys(firstName)
        user_lastName = self.browser.find_element(*RegisterPageLocators.LAST_NAME)
        user_lastName.send_keys(lastName)
        user_Email = self.browser.find_element(*RegisterPageLocators.EMAIL)
        user_Email.send_keys(Email)
        user_Password = self.browser.find_element(*RegisterPageLocators.PASSWORD)
        user_Password.send_keys(Password)
        user_Confirm_Password = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD)
        user_Confirm_Password.send_keys(Confirm_Password)
        button_registration = self.browser.find_element(*RegisterPageLocators.REGISTER_SUBMIT)
        button_registration.click()


