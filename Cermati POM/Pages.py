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

    # Fungsi Click JS Alert
    def alert_click(self, locator):
        self.driver.find_element_by_xpath(locator).click()
        self.driver.switch_to.alert.accept()

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def signup(self):
        # Type Email
        self.enter_text(Locators.REG_EMAIL_FIELD, TestData.EMAIL_DATA)

        # Type Password
        self.enter_text(Locators.REG_PASSWORD_FIELD, TestData.PASSWORD_DATA)

        # Retype Password
        self.enter_text(Locators.REG_CONFIRM_PASSWORD_FIELD, TestData.PASSWORD_DATA)

        # Type First Name
        self.enter_text(Locators.REG_FIRST_NAME_FIELD, TestData.FIRSTNAME_DATA)

        # Type Last Name
        self.enter_text(Locators.REG_LAST_NAME_FIELD, TestData.LASTNAME_DATA)

        # Type Phone Number
        self.enter_text(Locators.REG_PHONE_NUMBER_FIELD, TestData.PHONE_NUMBER_DATA)

        # Type City
        self.enter_text(Locators.REG_CITY_FIELD, TestData.CITY_DATA)

        # Wait For
        self.is_visible(Locators.REG_CITY_POP_UP)

        # Click Pop Up
        self.click(Locators.REG_CITY_POP_UP)

