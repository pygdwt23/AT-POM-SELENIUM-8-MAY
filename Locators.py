from selenium.webdriver.common.by import By

class Locators():

    # Homepage
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "a.login")
    PRODUCT_CARD = (By.XPATH, '//*[@id="homefeatured"]/li[2]')
    MORE_BUTTON = (By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a[2]/span')
    ADD_TO_CART_BUTTON = (By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[2]/div[2]/a[1]/span')
    QUICKVIEW_BUTTON = (By.XPATH, '//*[@id="homefeatured"]/li[2]/div/div[1]/div/a[2]/span')
    CATEGORIES_WOMEN_BUTTON = (By.XPATH,'//*[@id="footer"]/div/section[2]/div/div/ul/li/a')
    SEARCH_FIELD = (By.ID, 'search_query_top')
    SEARCH_SUBMIT = (By.NAME, 'submit_search')

    # AUTH PAGE
    REG_EMAIL_FIELD = (By.ID, 'email_create')
    SUBMIT_CREATE_ACCOUNT = (By.ID, 'SubmitCreate')
    SIGN_IN_EMAIL_FIELD = (By.ID, 'email')
    SIGN_IN_PASSWORD_FIELD = (By.ID, 'passwd')
    SUBMIT_SIGN_IN = (By.ID, 'SubmitLogin')

    # REGISTRATION PAGE
    REG_RADIO_GENDER_1 = (By.ID, 'id_gender1')
    REG_RADIO_GENDER_2 = (By.ID, 'id_gender2')
    REG_FIRST_NAME = (By.ID, 'customer_firstname')
    REG_LAST_NAME = (By.ID, 'customer_lastname')
    REG_PASSWORD = (By.ID, 'passwd')
    REG_DROP_DAYS = 'days'
    REG_DROP_MONTHS = 'months'
    REG_DROP_YEARS = 'years'
    REG_COMPANY = (By.ID, 'company')
    REG_ADDRESS1 = (By.ID, 'address1')
    REG_CITY = (By.ID, 'city')
    REG_STATE = 'id_state'
    REG_POSTAL_CODE = (By.ID, 'postcode')
    REG_COUNTRY = 'id_country'
    REG_ADDITIONAL_INFO = (By.ID, 'other')
    REG_MOBILE_PHONE = (By.ID, 'phone_mobile')
    REG_ADDRESS_ALIAS = (By.ID, 'alias')
    REG_SUBMIT_REGISTER = (By.ID, 'submitAccount')
    REG_ALERT_SUCCESS = (By.CSS_SELECTOR, 'p.info-account')
    REG_ALERT_FAILED = (By.XPATH, '//*[@id="center_column"]/div/p')
    REG_ALERT_ALREADY_REGISTERED = (By.XPATH, '//*[@id="create_account_error"]/ol/li')





