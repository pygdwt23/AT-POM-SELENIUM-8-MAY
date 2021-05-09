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


