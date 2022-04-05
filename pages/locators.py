from selenium.webdriver.common.by import By


class BasePageLocators():
    REGISTER_LINK = (By.CLASS_NAME, "ico-register")
    LOGIN_LINK = (By.CLASS_NAME, "ico-login")
    USER_LINK = (By.CLASS_NAME, "account")
    BASKET_LINK = (By.CLASS_NAME, "ico-cart")


class RegisterPageLocators():
    REGISTER_FORM = (By.NAME, "__RequestVerificationToken")
    GENDER_MALE = (By.ID, "gender-male")
    GENDER_FEMALE = (By.ID, "gender-female")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_SUBMIT = (By.ID, "register-button")
    RESULT = (By.CLASS_NAME, "result")
    ERROR_REGISTER_NAME = (By.CSS_SELECTOR, "[for='FirstName']")
    ERROR_REGISTER_PASSWORD = (By.CSS_SELECTOR, "[for='Password']")


class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, "returning-wrapper")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_SUBMIT = (By.CSS_SELECTOR, "[value='Log in']")
    ERROR_LOGIN_NAME = (By.CLASS_NAME, "validation-summary-errors")
    LOG_OUT = (By.CSS_SELECTOR, "[href='/logout']")


class UserPageLocators():
    USER_FORM = (By.XPATH, '//strong[text()="My account"]')
    CHANGE_PASSWORD = (By.CSS_SELECTOR, "[href='/customer/changepassword']")
    OLD_PASSWORD = (By.ID, "OldPassword")
    NEW_PASSWORD = (By.ID, "NewPassword")
    CONFIRM_PASSWORD = (By.ID, "ConfirmNewPassword")
    CHANGE_PASSWORD_SUBMIT = (By.CSS_SELECTOR, "[value='Change password']")
    CHANGE_PASSWORD_RESULT = (By.CLASS_NAME, 'result')
    ERROR_CHANGE_PASSWORD = (By.XPATH, '//li[text()="Old password doesn\'t match"]')


class BasketPageLocators():
    BASKET_FORM = (By.XPATH, '//h1[text()="Shopping cart"]')
    BASKET_ITEM = (By.CLASS_NAME, 'cart')
    BASKET_COUNT = (By.CLASS_NAME, 'cart-qty')
    NAME_BOOK_IN_BASKET_PAGE = (By.CLASS_NAME, 'product-name')
    PRISE_PRODUCT_IN_BASKET_PAGE = (By.CLASS_NAME, 'product-unit-price')
    FINAL_PRISE_PRODUCT_IN_BASKET_PAGE = (By.CLASS_NAME, 'product-subtotal')
    COUNT_PRODUCT_IN_BASKET_PAGE = (By.CSS_SELECTOR, "[name='itemquantity2337316']")


class ProductPageLocators():
    BOOKS_LINK = (By.CSS_SELECTOR, "[href='/books']")
    BOOKS_COLLECTION = (By.CLASS_NAME, 'product-item')
    BOOK_ITEM = (By.CSS_SELECTOR, "[href='/computing-and-internet']")
    ADD_TO_CART_SUBMIT = (By.CSS_SELECTOR, "[value='Add to cart']")
    NAME_BOOK_IN_PRODUCT_PAGE = (By.CSS_SELECTOR, "[itemprop='name']")
    PRISE_BOOK_IN_PRODUCT_PAGE = (By.CSS_SELECTOR, "[itemprop='price']")
    NAME_BOOK_IN_PRODUCT_LIST_PAGE = (By.XPATH, '//h2/a')
    PRISE_BOOK_IN_PRODUCT_LIST_PAGE = (By.CLASS_NAME, 'price actual-price')