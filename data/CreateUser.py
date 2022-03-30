from dataclasses import dataclass
from faker import Faker
import random


@dataclass(frozen=True)
class TestUser:
    Gender: str
    firstName: str
    lastName: str
    Email: str
    Password: str
    Confirm_Password: str


UserGender = TestUser("Male", "Test6", "Test6", "Test6@mail.ru", "11472589", "11472589")


class TestUserFaker:

    def __init__(self, GENDER, FIRST_NAME, LAST_NAME, EMAIL, PASSWORD, CONFIRM_PASSWORD):
        self.GENDER = GENDER
        self.FIRST_NAME = FIRST_NAME
        self.LAST_NAME = LAST_NAME
        self.EMAIL = EMAIL
        self.PASSWORD = PASSWORD
        self.CONFIRM_PASSWORD = CONFIRM_PASSWORD

    fake = Faker()
    gender_lst = ["Male", "Female"]
    GENDER = random.choice(gender_lst)
    FIRST_NAME = fake.first_name()
    LAST_NAME = fake.last_name()
    EMAIL = fake.email()
    PASSWORD = random.randint(100000, 999999)
    CONFIRM_PASSWORD = PASSWORD


User = TestUserFaker(TestUserFaker.GENDER, TestUserFaker.FIRST_NAME, TestUserFaker.LAST_NAME, TestUserFaker.EMAIL, TestUserFaker.PASSWORD, TestUserFaker.CONFIRM_PASSWORD)


