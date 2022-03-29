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


class LoginPageLocators():
    LOGIN_FORM = (By.CLASS_NAME, "returning-wrapper")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_SUBMIT = (By.CLASS_NAME, "button-1 login-button")


class UserPageLocators():
    USER_FORM = (By.XPATH, '//strong[text()="My account"]')
    CHANGE_PASSWORD = (By.CSS_SELECTOR, "[href='/customer/changepassword'] ")
    OLD_PASSWORD = (By.ID, "OldPassword")
    NEW_PASSWORD = (By.ID, "NewPassword")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    CHANGE_PASSWORD_SUBMIT = (By.CLASS_NAME, "button-1 change-password-button")