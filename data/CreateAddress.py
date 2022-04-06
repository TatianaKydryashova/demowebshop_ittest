from faker import Faker
import random


class TestAdress:

    def __init__(self, city, address, zip, phone):

        self.city = city
        self.address = address
        self.zip = zip
        self.phone = phone

    seed = random.randint(1, 999999999)
    fake = Faker()
    Faker.seed(seed)

    city = fake.city()
    address = fake.address()
    zip = fake.postcode()
    phone = fake.phone_number()


Adress = TestAdress(TestAdress.city, TestAdress.address, TestAdress.zip, TestAdress.phone)