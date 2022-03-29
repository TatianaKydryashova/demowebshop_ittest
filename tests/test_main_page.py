from pages.MainPage import MainPage


def test_register_page(browser):
    link = "http://demowebshop.tricentis.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_register_page()
    page.should_be_register_page()


def test_login_page(browser):
    link = "http://demowebshop.tricentis.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()

