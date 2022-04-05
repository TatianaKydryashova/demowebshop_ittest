from pages.BasePage import BasePage
from .locators import ProductPageLocators, BasketPageLocators, BasePageLocators


class ProductPage(BasePage):
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









