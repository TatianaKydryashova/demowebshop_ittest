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

    def __init__(self, gender, first_name, last_name, email, password, confirm_password):
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    seed = random.randint(1, 999999999)
    fake = Faker()
    Faker.seed(seed)
    gender_lst = ["Male", "Female"]
    gender = random.choice(gender_lst)
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    password = random.randint(100000, 999999)
    confirm_password = password


User = TestUserFaker(TestUserFaker.gender, TestUserFaker.first_name, TestUserFaker.last_name, TestUserFaker.email, TestUserFaker.password, TestUserFaker.confirm_password)
UserWithoutGender = TestUserFaker("", TestUserFaker.first_name, TestUserFaker.last_name, TestUserFaker.email, TestUserFaker.password, TestUserFaker.confirm_password)
UserWithoutRequiredFields = TestUserFaker(TestUserFaker.gender, "", TestUserFaker.last_name, TestUserFaker.email, TestUserFaker.password, TestUserFaker.confirm_password)
UserPasswordIsLess6Symbols = TestUserFaker(TestUserFaker.gender, TestUserFaker.first_name, TestUserFaker.last_name, TestUserFaker.email, "111", "111")