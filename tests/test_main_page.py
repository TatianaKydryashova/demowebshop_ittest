from pages.MainPage import MainPage


def test_register_page(browser):
    page = MainPage(browser)
    page.open()
    page.go_to_register_page()
    page.should_be_register_page()


def test_login_page(browser):
    page = MainPage(browser)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()


def test_basket_page(browser):
    page = MainPage(browser)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_page()


