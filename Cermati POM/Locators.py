from selenium.webdriver.common.by import By

class Locators():

    # Registration Page
    REG_EMAIL_FIELD = (By.ID, 'email')
    REG_PASSWORD_FIELD = (By.ID, 'password')
    REG_CONFIRM_PASSWORD_FIELD = (By.ID, 'confirm-password')
    REG_FIRST_NAME_FIELD = (By.ID, 'first-name')
    REG_LAST_NAME_FIELD = (By.ID, 'last-name')
    REG_PHONE_NUMBER_FIELD = (By.ID, 'mobile-phone')
    REG_CITY_FIELD = (By.ID, 'residence-city')
    REG_CITY_POP_UP = (By.XPATH, '//*[@id="join-container"]/div/div/div[2]/div/div[7]/div/div[2]/div')
    REG_SUBMIT_BUTTON = (By.XPATH, '//*[@id="join-container"]/div/div/div[2]/div/div[9]/button')