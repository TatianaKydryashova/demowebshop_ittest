import pytest
from data.CreateUser import User
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage


@pytest.mark.smoke
class TestLoginUserPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser)
        page.open()
        page.register_new_faker_user(User)
        page.logout()

    def test_login(self, browser):
        page = LoginPage(browser)
        page.open()
        Email = User.email
        Password = User.password
        page.login_user(Email, Password)
        page.should_be_user_page()

    def test_login_without_required_fields(self, browser):
        page = LoginPage(browser)
        page.open()
        Email = ""
        Password = User.password
        page.login_user(Email, Password)
        page.should_be_error_login_message()


