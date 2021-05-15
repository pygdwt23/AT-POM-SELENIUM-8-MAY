from faker import Faker
import random

class TestData():
    fake = Faker(["id_ID"])

    CHROME_PATH = "C:\Drivers\chromedriver.exe"

    BASE_URL = "https://www.cermati.com/gabung"

    # Registration Data
    EMAIL_DATA = fake.ascii_email()
    PASSWORD_DATA = fake.password()
    FIRSTNAME_DATA = fake.first_name()
    LASTNAME_DATA = fake.last_name()
    RANDOM_PHONE_GENERATOR = random.randrange(123456789)
    PHONE_NUMBER_DATA = "085"+ str(RANDOM_PHONE_GENERATOR)
    CITY_DATA = fake.city()