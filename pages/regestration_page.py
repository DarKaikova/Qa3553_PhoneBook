from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait



class RegistrationPage:

    LOGIN_NAV_LINK = (By.CSS_SELECTOR, "[href='/login']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    REGISTRATION_BTN = (By.CSS_SELECTOR, "button[name='registration']")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, "h2")


    def __init__(self, driver):
        self.driver = driver

    def open_login_form(self):
        self.driver.find_element(*self.LOGIN_NAV_LINK).click()

    def fill_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).clear()
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def registration(self):
        self.driver.find_element(*self.REGISTRATION_BTN).click()


    def registration_success_text(self):
        element = WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.visibility_of_element_located(self.CONFIRMATION_TEXT)
        )
        return element.text

    def get_alert_text(self):
        alert = WebDriverWait(self.driver, timeout=5).until(
            expected_conditions.alert_is_present()
        )

        return alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()
