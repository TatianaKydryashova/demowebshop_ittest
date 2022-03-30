import pytest
from random_word import RandomWords

from data.CreateUser import UserGender, TestUserFaker, User
from pages.BasePage import BasePage
from pages.RegisterPage import RegisterPage


def test_register_new_user(browser):
    link = "http://demowebshop.tricentis.com/register"
    page = RegisterPage(browser, link)
    page.open()
    page.register_new_user(UserGender)
    page.should_be_register_user()


def test_register_new_user_with_faker(browser):
    link = "http://demowebshop.tricentis.com/register"
    page = RegisterPage(browser, link)
    page.open()
    page.register_new_faker_user(User)
    page.should_be_register_user()

