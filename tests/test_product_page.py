import time

from pages.ProductPage import ProductPage


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