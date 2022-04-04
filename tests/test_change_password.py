import pytest
import random
from data.CreateUser import User
from pages.RegisterPage import RegisterPage
from pages.UserPage import UserPage


@pytest.mark.smoke
class TestChangePasswordFromUserPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser)
        page.open()
        page.register_new_faker_user(User)

    def test_user_can_change_password(self, browser):
        page = UserPage(browser)
        page.open()
        old_password = User.password
        new_password = random.randint(100000, 999999)
        confirm_password = new_password
        page.change_password(old_password, new_password, confirm_password)
        page.should_be_change_password()

    def test_error_change_password(self, browser):
        page = UserPage(browser)
        page.open()
        old_password = random.randint(100000, 999999)
        new_password = random.randint(100000, 999999)
        confirm_password = new_password
        page.change_password(old_password, new_password, confirm_password)
        page.should_be_error_change_password()