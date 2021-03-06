from .BasePage import BasePage
from .locators import RegisterPageLocators
from data.CreateUser import TestUser, TestUserFaker
from data.URL import URL


class RegisterPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.url = URL.REGISTER_PAGE_URL

    def user_Gender(self, value):
        if value == "Male":
            self.browser.find_element(*RegisterPageLocators.GENDER_MALE).click()
        elif value == "Female":
            self.browser.find_element(*RegisterPageLocators.GENDER_FEMALE).click()

    def user_firstName(self, value):
        self.browser.find_element(*RegisterPageLocators.FIRST_NAME).send_keys(value)

    def user_lastName(self, value):
        self.browser.find_element(*RegisterPageLocators.LAST_NAME).send_keys(value)

    def user_Email(self, value):
        self.browser.find_element(*RegisterPageLocators.EMAIL).send_keys(value)

    def user_Password(self, value):
        self.browser.find_element(*RegisterPageLocators.PASSWORD).send_keys(value)

    def user_Confirm_Password(self, value):
        self.browser.find_element(*RegisterPageLocators.CONFIRM_PASSWORD).send_keys(value)

    def register_new_user(self, CreateUser:TestUser):
        self.user_Gender(CreateUser.Gender)
        self.user_firstName(CreateUser.firstName)
        self.user_lastName(CreateUser.lastName)
        self.user_Email(CreateUser.Email)
        self.user_Password(CreateUser.Password)
        self.user_Confirm_Password(CreateUser.Confirm_Password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_SUBMIT).click()

    def register_new_faker_user(self, CreateUser:TestUserFaker):
        self.user_Gender(CreateUser.gender)
        self.user_firstName(CreateUser.first_name)
        self.user_lastName(CreateUser.last_name)
        self.user_Email(CreateUser.email)
        self.user_Password(CreateUser.password)
        self.user_Confirm_Password(CreateUser.confirm_password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_SUBMIT).click()

    def register_new_user_without_gender(self, CreateUser:TestUserFaker):
        self.user_firstName(CreateUser.first_name)
        self.user_lastName(CreateUser.last_name)
        self.user_Email(CreateUser.email)
        self.user_Password(CreateUser.password)
        self.user_Confirm_Password(CreateUser.confirm_password)
        self.browser.find_element(*RegisterPageLocators.REGISTER_SUBMIT).click()



