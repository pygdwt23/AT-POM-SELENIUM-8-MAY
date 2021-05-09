from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

from TestData import TestData
from Locators import Locators
from Pages import HomePage
from Pages import AuthPage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=TestData.CHROME_PATH)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

class RegisterTest(BaseTest):
    def test_register_success(self):

        # Load Homeage
        self.homepage = HomePage(self.driver)

        # Click Sign In Button
        self.homepage.signin()

        # Load Auth Page
        self.authpage = AuthPage(self.homepage.driver)

        # Register Success
        self.authpage.register_success()

        time.sleep(3)

        # Assertion
        register_info = self.authpage.get_text(Locators.REG_ALERT_SUCCESS)
        self.assertEqual(TestData.ALERT_REGISTER_SUCCESS, register_info)

    def test_register_failed(self):

        # Load Homeage
        self.homepage = HomePage(self.driver)

        # Click Sign In Button
        self.homepage.signin()

        # Load Auth Page
        self.authpage = AuthPage(self.homepage.driver)

        # Register Failed
        self.authpage.register_failed()

        time.sleep(3)

        # Assertion
        register_info = self.authpage.get_text(Locators.REG_ALERT_FAILED)
        self.assertEqual(TestData.ALERT_REGISTER_FAILED, register_info)

    def test_already_registered(self):

        # Load Homepage
        self.homepage = HomePage(self.driver)

        # Click Sign In Button
        self.homepage.signin()

        # Load Auth Page
        self.authpage = AuthPage(self.homepage.driver)

        # Already Register
        self.authpage.register_failed_already_registered()

        time.sleep(3)

        # Assertion
        register_info = self.authpage.get_text(Locators.REG_ALERT_ALREADY_REGISTERED)
        self.assertEqual(TestData.ALERT_ALREADY_REGISTERED, register_info)


class AddToCartTest(BaseTest):
    def test_add_from_home(self):

        # Load Home Page
        self.homepage = HomePage(self.driver)

        # Add to Cart (From Home)
        self.homepage.add_from_home()

        # Assertion
        status = self.homepage.get_text(Locators.ADD_FROM_HOME_STATUS)
        self.assertEqual(status, TestData.ALERT_ADD_FROM_HOME)

    def test_add_from_category(self):

        # Load Home Page
        self.homepage = HomePage(self.driver)

        # Click Category
        self.homepage.category()

        # Add to Cart (From Category)
        self.homepage.add_from_category()

        # Assertion
        status = self.homepage.get_text(Locators.CATEGORY_ADD_TO_CART_STATUS)
        self.assertEqual(status, TestData.ALERT_ADD_FROM_CATEGORY)

    def test_add_from_details(self):
        # Load Home Page
        self.homepage = HomePage(self.driver)

        # Add from details
        self.homepage.add_from_details()

        # Assertion
        status = self.homepage.get_text(Locators.DETAIL_PRODUCT_STATUS)
        self.assertEqual(status, TestData.ALERT_ADD_FROM_DETAILS)

    def test_add_from_search(self):
        # Load Home Page
        self.homepage = HomePage(self.driver)

        # Add from Search
        self.homepage.add_from_search()

        # Assertion
        status = self.homepage.get_text(Locators.SEARCH_PRODUCT_STATUS)
        self.assertEqual(status, TestData.ALERT_ADD_FROM_SEARCH)