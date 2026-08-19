import time

from conftest import generate_unique_email, generate_valid_password
from pages.regestration_page import RegistrationPage

ALREADY_REG_EMAIL = 'doritos654@gmail.com'
WRONG_REG_EMAIL = 'doritos654gmail.com'
ALREADY_REG_PASSWORD = 'Ddas!223466'
WRONG_REG_PASSWORD = 'Dda'

def test_registration_success(driver):
    reg_page = RegistrationPage(driver)

    reg_page.open_login_form()
    reg_page.fill_email(generate_unique_email())
    reg_page.fill_password(generate_valid_password())
    reg_page.registration()
    time.sleep(2)

    assert reg_page.registration_success_text() == 'Add new by clicking on Add in NavBar!'


def test_with_wrong_email(driver):
    reg_page = RegistrationPage(driver)

    reg_page.open_login_form()
    reg_page.fill_email(WRONG_REG_EMAIL)
    reg_page.fill_password(generate_valid_password())
    reg_page.registration()


    expected_text = """Wrong email or password format
            Email must contains one @ and minimum 2 symbols after last dot
            Password must contain at least one uppercase letter!
            Password must contain at least one lowercase letter!
            Password must contain at least one digit!
            Password must contain at least one special symbol from [‘$’,’~’,’-‘,’_’]!"""

    assert reg_page.get_alert_text() == expected_text
    reg_page.accept_alert()


def test_with_wrong_password(driver):
    reg_page = RegistrationPage(driver)

    reg_page.open_login_form()
    reg_page.fill_email(generate_unique_email())
    reg_page.fill_password(WRONG_REG_PASSWORD)
    reg_page.registration()

    expected_text = """Wrong email or password format
            Email must contains one @ and minimum 2 symbols after last dot
            Password must contain at least one uppercase letter!
            Password must contain at least one lowercase letter!
            Password must contain at least one digit!
            Password must contain at least one special symbol from [‘$’,’~’,’-‘,’_’]!"""

    assert reg_page.get_alert_text() == expected_text
    reg_page.accept_alert()


def test_with_registered_data_already(driver):
    reg_page = RegistrationPage(driver)

    reg_page.open_login_form()
    reg_page.fill_email(ALREADY_REG_EMAIL)
    reg_page.fill_password(ALREADY_REG_PASSWORD)
    reg_page.registration()

    assert reg_page.get_alert_text() == 'User already exist'
    reg_page.accept_alert()


def test_with_registered_email_and_another_password(driver):
    reg_page = RegistrationPage(driver)

    reg_page.open_login_form()
    reg_page.fill_email(ALREADY_REG_EMAIL)
    reg_page.fill_password(generate_valid_password())
    reg_page.registration()

    assert reg_page.get_alert_text() == 'User already exist'
    reg_page.accept_alert()