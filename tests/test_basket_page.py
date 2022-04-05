from pages.BasketPage import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser)
    page.open()
    page.should_not_be_product()
    page.should_be_correct_count()