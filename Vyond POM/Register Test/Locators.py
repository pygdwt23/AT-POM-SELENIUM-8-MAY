from selenium.webdriver.common.by import By

class Locators():

    # Homepage
    HM_SIGN_UP_BTN = (By.XPATH, '//*[@id="app"]/div/div[1]/div[3]/ul/li[1]/a')

    # SIGN UP PAGE
    SIGN_UP_WITH_EMAIL_BTN = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div[1]/button')
    REG_FIRST_NAME = (By.NAME, 'FIRST_NAME')
    REG_LAST_NAME = (By.NAME, 'LAST_NAME')
    REG_COMPANY_NAME = (By.NAME, 'COMPANY_NAME')
    REG_JOB_ROLE = 'JOB_ROLE_ID'
    REG_JOB_ROLE_NAME = (By.NAME, 'JOB_ROLE_NAME')
    REG_TELEPHONE = (By.ID, 'phone-text-field')
    REG_COUNTRY = 'COUNTRY'
    REG_EMAIL = (By.NAME, 'WORK_EMAIL')
    REG_PASSWORD = (By.NAME, 'PASSWORD')
    REG_AGREE_CHECK = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/form/div[9]/label/span/span[1]')
    REG_YES_SUBSCRIBE = (By.XPATH , '//*[@id="app"]/div/div[2]/div[2]/div/form/div[10]/label[1]/span')
    REG_NO_SUBSCRIBE = (By.XPATH , '//*[@id="app"]/div/div[2]/div[2]/div/form/div[10]/label[2]/span')
    REG_SIGN_UP_SUBMIT_BTN = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/form/div[9]/label/span/span[1]')