from selenium.webdriver.common.by import By


class BasePageLocators():
    REGISTER_LINK = (By.CLASS_NAME, "ico-register")
    LOGIN_LINK = (By.CLASS_NAME, "ico-login")
    USER_LINK = (By.CLASS_NAME, "account")


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


class UserPageLocators():
    USER_FORM = (By.XPATH, '//strong[text()="My account"]')
    CHANGE_PASSWORD = (By.CSS_SELECTOR, "[href='/customer/changepassword']")
    OLD_PASSWORD = (By.ID, "OldPassword")
    NEW_PASSWORD = (By.ID, "NewPassword")
    CONFIRM_PASSWORD = (By.ID, "ConfirmNewPassword")
    CHANGE_PASSWORD_SUBMIT = (By.CSS_SELECTOR, "[value='Change password']")
    CHANGE_PASSWORD_RESULT = (By.CLASS_NAME, 'result')
    ERROR_CHANGE_PASSWORD = (By.XPATH, '//li[text()="Old password doesn\'t match"]')