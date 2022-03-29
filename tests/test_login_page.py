from pages.LoginPage import LoginPage


def test_register_new_user(browser):
    link = "http://demowebshop.tricentis.com/login"
    page = LoginPage(browser, link)
    page.open()
    Email = "Test1@fakemail.org"
    Password = "112233441"
    page.login_user(Email, Password)
    page.should_be_user_page()