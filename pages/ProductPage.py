from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pytest
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
from conftest import browser
from data.CreateAddress import TestAdress
from data.CreateUser import User
from pages.BasePage import BasePage
from .RegisterPage import RegisterPage
from .locators import ProductPageLocators, BasketPageLocators, BasePageLocators, CheckoutPageLocators


class ProductPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.wait = None

    def go_to_product_details(self):
        self.browser.find_element(*ProductPageLocators.BOOKS_LINK).click()
        self.browser.find_element(*ProductPageLocators.BOOK_ITEM).click()

    def go_to_product_list(self):
        self.browser.find_element(*ProductPageLocators.BOOKS_LINK).click()

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_CART_SUBMIT).click()

    def should_be_correct_add_name_book_from_the_product_details_page(self):
        name_book_in_product = self.browser.find_element(*ProductPageLocators.NAME_BOOK_IN_PRODUCT_PAGE)
        name_book_text = name_book_in_product.text
        print(name_book_text)
        name_book_in_basket = self.browser.find_element(*BasketPageLocators.NAME_BOOK_IN_BASKET_PAGE)
        name_book_text_basket = name_book_in_basket.text
        print(name_book_text_basket)
        assert name_book_text == name_book_text_basket, "Error in book title"

    def should_be_correct_add_name_book_from_the_product_list_page(self):
        name_book_in_product = self.browser.find_elements(*ProductPageLocators.NAME_BOOK_IN_PRODUCT_LIST_PAGE)
        name_book_text = name_book_in_product[0].text
        print(name_book_text)
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()
        name_book_in_basket = self.browser.find_element(*BasketPageLocators.NAME_BOOK_IN_BASKET_PAGE)
        name_book_text_basket = name_book_in_basket.text
        print(name_book_text_basket)
        assert name_book_text == name_book_text_basket, "Error in book title"

    def should_be_changing_the_quantity_and_recalculating(self):
        self.browser.find_element(*BasePageLocators.BASKET_LINK).click()
        price = self.browser.find_element(*BasketPageLocators.PRISE_PRODUCT_IN_BASKET_PAGE).text
        count = self.browser.find_element(*BasketPageLocators.COUNT_PRODUCT_IN_BASKET_PAGE)
        count.clear()
        count.send_keys(2)
        self.browser.find_element(*BasketPageLocators.UPDATE_CART_SUBMIT).click()
        final_price = self.browser.find_element(*BasketPageLocators.FINAL_PRISE_PRODUCT_IN_BASKET_PAGE).text
        result_prise = float(price) * 2
        assert round(result_prise) == round(float(final_price)), "Error in price"

    def should_be_sorting_price_low_to_high(self):
        prise_list = self.browser.find_elements(*ProductPageLocators.PRISE_BOOK_IN_PRODUCT_LIST_PAGE)
        prise_list_text = []
        for el in prise_list:
            element = float(el.text)
            prise_list_text.append(element)
        prise_list_text.sort()
        print(prise_list_text)
        self.browser.find_element(*ProductPageLocators.SORT_BY).click()
        self.browser.find_element(*ProductPageLocators.SORT_BY_PRICE_LOW_TO_HIGH).click()
        prise_list_sort = self.browser.find_elements(*ProductPageLocators.PRISE_BOOK_IN_PRODUCT_LIST_PAGE)
        prise_list_sort_text = []
        for el in prise_list_sort:
            element = float(el.text)
            prise_list_sort_text.append(element)
        print(prise_list_sort_text)
        assert prise_list_text == prise_list_sort_text, "Error in sort"

    def should_be_add_basket(self):
        assert self.element_present(*BasketPageLocators.CONTENT_ALERT), "Error add product in basket"

    def user_city(self, value):
        self.browser.find_element(*CheckoutPageLocators.CITY).send_keys(value)

    def user_address(self, value):
        self.browser.find_element(*CheckoutPageLocators.ADDRESS).send_keys(value)

    def user_zip(self, value):
        self.browser.find_element(*CheckoutPageLocators.ZIP).send_keys(value)

    def user_phone(self, value):
        self.browser.find_element(*CheckoutPageLocators.PHONE).send_keys(value)

    def should_be_billing_address(self, CreateAdress: TestAdress):
        self.browser.find_element(*BasketPageLocators.TERMS_OF_SERVICE_CHECKBOX).click()
        self.browser.find_element(*BasketPageLocators.CHECKOUT_SUBMIT).click()
        select = Select(self.browser.find_element(*BasketPageLocators.COUNTRY))
        select.select_by_value("2")
        self.user_city(CreateAdress.city)
        self.user_address(CreateAdress.address)
        self.user_zip(CreateAdress.zip)
        self.user_phone(CreateAdress.phone)
        self.browser.find_element(*CheckoutPageLocators.BILLING_ADDRESS_NEXT_BUTTON).click()

    def should_be_add_address(self):
        assert self.element_present(*CheckoutPageLocators.SHIPPING_ADDRESS_NEXT_BUTTON), "Error"

    def should_be_shipping_address(self, timeout=4):
        button = WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="shipping-buttons-container"]/input[1]')))
        button.click()

    def should_be_shipping_method(self, timeout=4):
        button = WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="shipping-method-buttons-container"]/input[1]')))
        button.click()

    def should_be_payment_method(self, timeout=4):
        button = WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="payment-method-buttons-container"]/input[1]')))
        button.click()

    def should_be_payment_information(self, timeout=4):
        button = WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="payment-info-buttons-container"]/input[1]')))
        button.click()

    def should_be_confirm_order(self, timeout=4):
        button = WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@id="confirm-order-buttons-container"]/input[1]')))
        button.click()

    def should_be_order_form(self):
        assert self.element_present(*CheckoutPageLocators.ORDER_FORM), "Error"














