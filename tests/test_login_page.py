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


class TestLoginUserPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://demowebshop.tricentis.com/register"
        page = RegisterPage(browser, link)
        page.open()
        page.register_new_faker_user(User)

    def test_login(self, browser):
        link = "http://demowebshop.tricentis.com/login"
        page = LoginPage(browser, link)
        page.open()
        page.login_user(User.EMAIL, User.PASSWORD)
        page.should_be_user_page()
