import pytest
from random_word import RandomWords

from pages.BasePage import BasePage
from pages.RegisterPage import RegisterPage


def test_register_new_user(browser):
    link = "http://demowebshop.tricentis.com/register"
    page = RegisterPage(browser, link)
    page.open()
    firstName = "Test1"
    lastName = "Test1"
    Email = "Test1@fakemail.org"
    Password = "112233441"
    Confirm_Password = "112233441"
    page.register_new_user(firstName, lastName, Email, Password, Confirm_Password)
    page.should_be_register_user()

