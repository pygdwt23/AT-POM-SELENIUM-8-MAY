from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

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

    def select_dropdown_by_visible_text_name(self, locator, item):
        dropdown = Select(self.driver.find_element_by_name(locator))
        dropdown.select_by_visible_text(item)

    # Fungsi Hover
    def move_element_to(self,locator):
        hover = self.driver.find_element_by_xpath(locator)
        self.action.move_to_element(hover).perform()

    # Fungsi Click JS Alert
    def alert_click(self, locator):
        self.driver.find_element_by_xpath(locator).click()
        self.driver.switch_to.alert.accept()



class SignUpPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def signup(self):
        # Click Sign Up Button From Homepage
        self.click(Locators.HM_SIGN_UP_BTN)

        # Click Sign Up With Your Email Button
        self.click(Locators.SIGN_UP_WITH_EMAIL_BTN)

        # Type First Name
        self.enter_text(Locators.REG_FIRST_NAME, TestData.FIRST_NAME_VALUE)

        # Type Last Name
        self.enter_text(Locators.REG_LAST_NAME, TestData.LAST_NAME_VALUE)

        # Type Company Name
        self.enter_text(Locators.REG_COMPANY_NAME, TestData.COMPANY_VALUE)

        # Select Job Role
        self.select_dropdown_by_visible_text_name(Locators.REG_JOB_ROLE, TestData.JOB_ROLE_VALUE)

        # Type Job Role Value
        self.enter_text(Locators.REG_JOB_ROLE_NAME, TestData.JOB_ROLE_NAME_VALUE)

        # Type Phone Number
        self.enter_text(Locators.REG_TELEPHONE, TestData.TELEPHONE_VALUE)

        # Select Country
        self.select_dropdown_by_visible_text_name(Locators.REG_COUNTRY, TestData.COUNTRY_VALUE)

        # Type Email
        self.enter_text(Locators.REG_EMAIL, TestData.EMAIL_VALUE)

        # Type Password
        self.enter_text(Locators.REG_PASSWORD, TestData.PASSWORD_VALUE)

        # Click CheckBox
        self.click(Locators.REG_AGREE_CHECK)

        # Click Subscribe
        self.click(Locators.REG_YES_SUBSCRIBE)

        # Wait for visible
        self.is_visible(Locators.REG_SIGN_UP_SUBMIT_BTN)