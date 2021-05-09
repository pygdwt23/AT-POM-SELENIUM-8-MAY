from faker import Faker

class TestData():
    fake = Faker(["id_ID"])

    CHROME_PATH = "C:\Drivers\chromedriver.exe"

    BASE_URL = "http://automationpractice.com/index.php"


    # EMAIL SIGN IN
    SIGN_IN_EMAIL = 'narto@konoha.com'
    SIGN_IN_PASSWORD = '123narto321'

    # EMAIL SIGN UP (VALID)
    EMAIL_ALREADY_REGISTERED = "narto@konoha.com"

    SIGN_UP_VALID_FIRST_NAME = fake.first_name()
    SIGN_UP_VALID_LAST_NAME = fake.last_name()
    SIGN_UP_VALID_EMAIL = fake.ascii_email()
    SIGN_UP_VALID_PASSWORD = fake.password()
    DROP_DAYS_VALUE = "20"
    DROP_MONTHS_VALUE = "5"
    DROP_YEARS_VALUE = "2005"
    SIGN_UP_VALID_COMPANY = fake.company()
    SIGN_UP_VALID_ADDRESS = "1587 Elizabeth Trail Apt. 821"
    SIGN_UP_VALID_CITY = fake.city()
    SIGN_UP_VALID_STATE = "California"
    SIGN_UP_VALID_POSTAL_CODE = "90001"
    SIGN_UP_VALID_COUNTRY = "United States"
    SIGN_UP_VALID_ADDITIONAL_INFO = fake.text()
    SIGN_UP_VALID_MOBILE_PHONE = fake.phone_number()
    SIGN_UP_VALID_ADDRESS_ALIAS = "Home"

    # EMAIL SIGN UP (INVALID)
    SIGN_UP_INVALID_FIRST_NAME = "Y@JU7"
    SIGN_UP_INVALID_LAST_NAME = "M@7UJ"
    SIGN_UP_INVALID_EMAIL = "emailinvalid.com"
    SIGN_UP_INVALID_PASSWORD = "P@s5"
    DROP_DAYS_INVALID_VALUE = ""
    DROP_MONTHS_INVALID_VALUE = ""
    DROP_YEARS_INVALID_VALUE = ""
    SIGN_UP_INVALID_COMPANY = "K0MP@NY"
    SIGN_UP_INVALID_ADDRESS = "ALAMAT PALSU"
    SIGN_UP_INVALID_CITY = "C@LIURAN6"
    SIGN_UP_INVALID_STATE = ""
    SIGN_UP_INVALID_POSTAL_CODE = "POBOX911"
    SIGN_UP_INVALID_COUNTRY = ""
    SIGN_UP_INVALID_ADDITIONAL_INFO = "L0R3M!"
    SIGN_UP_INVALID_MOBILE_PHONE = "OB!0989999"
    SIGN_UP_INVALID_ADDRESS_ALIAS = "H0M3!"

    SEARCH_VALUE = 'dress'

    # ALERT REGISTER
    ALERT_REGISTER_SUCCESS = "Welcome to your account. Here you can manage all of your personal information and orders."
    ALERT_REGISTER_FAILED = "There are 6 errors"
    ALERT_ALREADY_REGISTERED = "An account using this email address has already been registered. Please enter a valid password or request a new one."

    # ALERT ADD TO CART
    ALERT_ADD_FROM_HOME = 'Product successfully added to your shopping cart'
    ALERT_ADD_FROM_CATEGORY = 'Product successfully added to your shopping cart'
    ALERT_ADD_FROM_DETAILS = 'Product successfully added to your shopping cart'
    ALERT_ADD_FROM_SEARCH = 'Product successfully added to your shopping cart'