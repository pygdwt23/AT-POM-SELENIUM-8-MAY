from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

from TestData import TestData
from Locators import Locators
from Pages import SignUpPage

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=TestData.CHROME_PATH)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


class RegisterTest(BaseTest):
    def test_sign_up_with_email(self):
        # Load Page
        self.signuptest = SignUpPage(self.driver)

        # Execute Code
        self.signuptest.signup()

        time.sleep(5)