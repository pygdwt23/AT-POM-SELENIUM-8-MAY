from faker import Faker
import random

class TestData():
    fake = Faker(["pl_PL"])

    CHROME_PATH = "C:\Drivers\chromedriver.exe"

    BASE_URL = "https://app.vyond.com"

    # SIGN UP DATA
    FIRST_NAME_VALUE = fake.first_name()
    LAST_NAME_VALUE = fake.last_name()
    COMPANY_VALUE = fake.company()
    JOB_ROLE_VALUE = "Other"
    JOB_ROLE_NAME_VALUE = fake.job()
    RANDOM_PHONE = random.randrange(123456789)
    TELEPHONE_VALUE = fake.phone_number()
    COUNTRY_VALUE = "Poland"
    EMAIL_VALUE = fake.ascii_email()
    PASSWORD_VALUE = fake.password()