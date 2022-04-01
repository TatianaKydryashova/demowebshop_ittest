import pytest
from random_word import RandomWords

from data.CreateUser import UserGender, UserWithoutGender, User, UserWithoutRequiredFields, UserPasswordIsLess6Symbols
from pages.BasePage import BasePage
from pages.RegisterPage import RegisterPage


def test_register_new_user(browser):
    page = RegisterPage(browser)
    page.open()
    page.register_new_user(UserGender)
    page.should_be_register_user()


@pytest.mark.smoke
def test_register_new_user_with_faker(browser):
    page = RegisterPage(browser)
    page.open()
    page.register_new_faker_user(User)
    page.should_be_register_user()


def test_register_new_user_without_gender(browser):
    page = RegisterPage(browser)
    page.open()
    page.register_new_faker_user(UserWithoutGender)
    page.should_be_register_user()


@pytest.mark.smoke
def test_register_new_user_without_required_fields(browser):
    page = RegisterPage(browser)
    page.open()
    page.register_new_faker_user(UserWithoutRequiredFields)
    page.should_be_error_register_user()


def test_register_new_user_password_is_less_6_symbols(browser):
    page = RegisterPage(browser)
    page.open()
    page.register_new_faker_user(UserPasswordIsLess6Symbols)
    page.should_be_error_password_register_user()

