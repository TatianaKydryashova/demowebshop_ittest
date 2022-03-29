import pytest

from pages.LoginPage import LoginPage


class TestChangePasswordFromUserPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup_class(self, browser):
        link = "http://demowebshop.tricentis.com/login"
        page = LoginPage(browser, link)
        page.open()
        Email = "Test1@fakemail.org"
        Password = "112233441"
        page.login_user(Email, Password)
        page.should_be_user_page()

    def test_user_cant_change_password(self, browser):
        link = "http://demowebshop.tricentis.com/"
        page = LoginPage(browser, link, 10)
        page.open()
        old_password = "112233441"
        new_password = "1122334411"
        confirm_password = "1122334411"
        page.change_password(old_password, new_password, confirm_password)
        page.should_be_change_password()