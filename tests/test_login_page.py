import pytest

from data.CreateUser import User
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage


def test_login_user(browser):
    link = "http://demowebshop.tricentis.com/login"
    page = LoginPage(browser, link)
    page.open()
    Email = "Test1@fakemail.org"
    Password = "112233441"
    page.login_user(Email, Password)
    page.should_be_user_page()


@pytest.mark.smoke
class TestLoginUserPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser)
        page.open()
        page.register_new_faker_user(User)

    def test_login(self, browser):
        page = LoginPage(browser)
        page.open()
        Email = User.EMAIL
        Password = User.PASSWORD
        page.login_user(Email, Password)
        page.should_be_user_page()

    def test_login_without_required_fields(self, browser):
        page = LoginPage(browser)
        page.open()
        Email = ""
        Password = User.PASSWORD
        page.login_user(Email, Password)
        page.should_be_error_login_message()


