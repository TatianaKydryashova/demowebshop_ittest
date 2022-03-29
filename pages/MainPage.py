from .BasePage import BasePage
from .locators import RegisterPageLocators, LoginPageLocators


class MainPage(BasePage):
    def should_be_register_page(self):
        self.should_be_register_url()
        self.should_be_register_form()

    def should_be_register_url(self):
        assert "register" in self.browser.current_url, "'register' not in current url"

    def should_be_register_form(self):
        assert self.is_element_present(*RegisterPageLocators.REGISTER_FORM), "Register form is not presented"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "'login' not in current url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"