import time

import pytest

from data.CreateAddress import Adress
from data.CreateUser import User
from pages.ProductPage import ProductPage
from pages.RegisterPage import RegisterPage


def test_guest_can_add_product_to_basket_from_the_product_details_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_product_details()
    page.add_to_basket()
    page.should_be_correct_add_name_book_from_the_product_details_page()


def test_guest_can_add_product_to_basket_from_the_product_list_page(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_product_list()
    page.add_to_basket()
    page.should_be_correct_add_name_book_from_the_product_list_page()


def test_changing_the_quantity_of_product_in_the_basket_and_recalculating_the_basket(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_product_details()
    page.add_to_basket()
    page.should_be_changing_the_quantity_and_recalculating()


def test_sorting(browser):
    page = ProductPage(browser)
    page.open()
    page.go_to_product_list()
    page.should_be_sorting_price_low_to_high()


class TestUserOrdering():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser)
        page.open()
        page.register_new_faker_user(User)

    def test_user_cant_ordering(self, browser):
        page = ProductPage(browser)
        page.open()
        page.go_to_product_details()
        page.add_to_basket()
        page.should_be_add_basket()
        page.go_to_basket_page()
        page.should_be_billing_address(Adress)
        page.should_be_add_address()
        page.should_be_shipping_address()
        #time.sleep(4)