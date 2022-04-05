from pages.BasePage import BasePage
from pages.locators import BasketPageLocators
from data.URL import URL


class BasketPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)
        self.url = URL.BASKET_URL

    def should_not_be_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Basket is not empty, but should be"

    def should_be_correct_count(self):
        basket_count = self.browser.find_element(*BasketPageLocators.BASKET_COUNT).text
        count = "(0)"
        assert basket_count == count, \
            "Count is not 0, but should be"