from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from TestData import TestData
from Locators import Locators

class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    # Fungsi Klik Locator
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    # Fungsi Hapus Data
    def clear_text(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).clear()

    # Fungsi input data
    def enter_text(self, locator, teks):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(teks)

    # Fungsi ambil teks
    def get_text(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).text

    # Fungsi cek elemen visible
    def is_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return bool(element)
        except TimeoutException:
            return False

    # Fungsi select dropdown
    def select_dropdown_by_value(self, locator, item):
        dropdown = Select(self.driver.find_element_by_id(locator))
        dropdown.select_by_value(item)

    def select_dropdown_by_visible_text(self, locator, item):
        dropdown = Select(self.driver.find_element_by_id(locator))
        dropdown.select_by_visible_text(item)

    # Fungsi Hover
    def move_element_to(self,locator):
        hover = self.driver.find_element_by_xpath(locator)
        self.action.move_to_element(hover).perform()

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def signin(self):
        # Fungsi untuk klik tombol Sign In di Home Page
        self.click(Locators.SIGN_IN_BUTTON)
        self.is_visible(Locators.REG_EMAIL_FIELD)

    def logo(self):
        self.click(Locators.LOGO_URL)

    def add_from_home(self):
        self.move_element_to(Locators.PRODUCT_CARD)
        self.click(Locators.ADD_TO_CART_BUTTON)
        self.is_visible(Locators.ADD_FROM_HOME_STATUS)

class AuthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def sign_in_success(self):
        # Type Email
        self.enter_text(Locators.SIGN_IN_EMAIL_FIELD, TestData.SIGN_IN_EMAIL)

        # Type Password
        self.enter_text(Locators.SIGN_IN_PASSWORD_FIELD, TestData.SIGN_IN_PASSWORD)

        # Click Sign In Button
        self.click(Locators.SUBMIT_SIGN_IN)

    def register_success(self):
        # Type Email
        self.enter_text(Locators.REG_EMAIL_FIELD, TestData.SIGN_UP_VALID_EMAIL)

        # Click Create an account button
        self.click(Locators.SUBMIT_CREATE_ACCOUNT)

        # Select Gender
        self.click(Locators.REG_RADIO_GENDER_1)

        # Type First Name
        self.enter_text(Locators.REG_FIRST_NAME, TestData.SIGN_UP_VALID_FIRST_NAME)

        # Type Last Name
        self.enter_text(Locators.REG_LAST_NAME, TestData.SIGN_UP_VALID_LAST_NAME)

        # Type Password
        self.enter_text(Locators.REG_PASSWORD, TestData.SIGN_UP_VALID_PASSWORD)

        # Select Date of Birth
        self.select_dropdown_by_value(Locators.REG_DROP_DAYS, TestData.DROP_DAYS_VALUE)
        self.select_dropdown_by_value(Locators.REG_DROP_MONTHS, TestData.DROP_MONTHS_VALUE)
        self.select_dropdown_by_value(Locators.REG_DROP_YEARS, TestData.DROP_YEARS_VALUE)

        # Type Company
        self.enter_text(Locators.REG_COMPANY, TestData.SIGN_UP_VALID_COMPANY)

        # Type Address
        self.enter_text(Locators.REG_ADDRESS1, TestData.SIGN_UP_VALID_ADDRESS)

        # Type City
        self.enter_text(Locators.REG_CITY, TestData.SIGN_UP_VALID_CITY)

        # Select State
        self.select_dropdown_by_visible_text(Locators.REG_STATE, TestData.SIGN_UP_VALID_STATE)

        # Type Post Code
        self.enter_text(Locators.REG_POSTAL_CODE, TestData.SIGN_UP_VALID_POSTAL_CODE)

        # Select Country
        self.select_dropdown_by_visible_text(Locators.REG_COUNTRY, TestData.SIGN_UP_VALID_COUNTRY)

        # Type Additional Info
        self.enter_text(Locators.REG_ADDITIONAL_INFO, TestData.SIGN_UP_VALID_ADDITIONAL_INFO)

        # Type Mobile Phone
        self.enter_text(Locators.REG_MOBILE_PHONE, TestData.SIGN_UP_VALID_MOBILE_PHONE)

        # Type Address Alias
        self.clear_text(Locators.REG_ADDRESS_ALIAS)
        self.enter_text(Locators.REG_ADDRESS_ALIAS, TestData.SIGN_UP_VALID_ADDRESS_ALIAS)

        # Click Register Button
        self.click(Locators.REG_SUBMIT_REGISTER)

    def register_failed(self):
        # Type Email
        self.enter_text(Locators.REG_EMAIL_FIELD, TestData.SIGN_UP_VALID_EMAIL)

        # Click Create an account button
        self.click(Locators.SUBMIT_CREATE_ACCOUNT)

        # Select Gender
        self.click(Locators.REG_RADIO_GENDER_1)

        # Type First Name
        self.enter_text(Locators.REG_FIRST_NAME, TestData.SIGN_UP_INVALID_FIRST_NAME)

        # Type Last Name
        self.enter_text(Locators.REG_LAST_NAME, TestData.SIGN_UP_INVALID_LAST_NAME)

        # Type Password
        self.enter_text(Locators.REG_PASSWORD, TestData.SIGN_UP_INVALID_PASSWORD)

        # Select Date of Birth
        self.select_dropdown_by_value(Locators.REG_DROP_DAYS, TestData.DROP_DAYS_INVALID_VALUE)
        self.select_dropdown_by_value(Locators.REG_DROP_MONTHS, TestData.DROP_MONTHS_INVALID_VALUE)
        self.select_dropdown_by_value(Locators.REG_DROP_YEARS, TestData.DROP_YEARS_INVALID_VALUE)

        # Type Company
        self.enter_text(Locators.REG_COMPANY, TestData.SIGN_UP_INVALID_COMPANY)

        # Type Address
        self.enter_text(Locators.REG_ADDRESS1, TestData.SIGN_UP_INVALID_ADDRESS)

        # Type City
        self.enter_text(Locators.REG_CITY, TestData.SIGN_UP_INVALID_CITY)

        # Select State
        self.select_dropdown_by_visible_text(Locators.REG_STATE, TestData.SIGN_UP_VALID_STATE)

        # Type Post Code
        self.enter_text(Locators.REG_POSTAL_CODE, TestData.SIGN_UP_INVALID_POSTAL_CODE)

        # Select Country
        self.select_dropdown_by_visible_text(Locators.REG_COUNTRY, TestData.SIGN_UP_VALID_COUNTRY)

        # Type Additional Info
        self.enter_text(Locators.REG_ADDITIONAL_INFO, TestData.SIGN_UP_INVALID_ADDITIONAL_INFO)

        # Type Mobile Phone
        self.enter_text(Locators.REG_MOBILE_PHONE, TestData.SIGN_UP_INVALID_MOBILE_PHONE)

        # Type Address Alias
        self.clear_text(Locators.REG_ADDRESS_ALIAS)
        self.enter_text(Locators.REG_ADDRESS_ALIAS, TestData.SIGN_UP_INVALID_ADDRESS_ALIAS)

        # Click Register Button
        self.click(Locators.REG_SUBMIT_REGISTER)

    def register_failed_already_registered(self):
        # Type Email
        self.enter_text(Locators.REG_EMAIL_FIELD, TestData.EMAIL_ALREADY_REGISTERED)

        # Click Create an account button
        self.click(Locators.SUBMIT_CREATE_ACCOUNT)