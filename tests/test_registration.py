import time
import uuid

from models.user import User
from pages.regestration_page import RegistrationPage

random_suffix = uuid.uuid4().hex[:8]



def test_registration_success(driver):
    reg_page = RegistrationPage(driver)

    user = User(
        f"rio{random_suffix}@gmail.com",
        "Ddas!223466"
    )

    reg_page.open_login_form()
    reg_page.fill_registration_form(user)
    reg_page.registration()
    time.sleep(2)

    assert reg_page.registration_success_text() == 'Add new by clicking on Add in NavBar!'





def test_with_wrong_email(driver):
    reg_page = RegistrationPage(driver)

    user = User(
        f"riogmail.com",
        "Ddas!223466"
    )

    reg_page.open_login_form()
    reg_page.fill_registration_form(user)
    reg_page.registration()
    time.sleep(2)



    assert "Wrong email or password format" in reg_page.get_alert_text()
    reg_page.accept_alert()


def test_with_wrong_password(driver):
    reg_page = RegistrationPage(driver)

    user = User(
        f"rio{random_suffix}@gmail.com",
        "D!2"
    )

    reg_page.open_login_form()
    reg_page.fill_registration_form(user)
    reg_page.registration()
    time.sleep(2)

    assert "Wrong email or password format" in reg_page.get_alert_text()
    reg_page.accept_alert()





def test_with_registered_data_already(driver):
    reg_page = RegistrationPage(driver)

    user = User(
        f"doritos654@gmail.com",
        "Ddas!223466"
    )

    reg_page.open_login_form()
    reg_page.fill_registration_form(user)
    reg_page.registration()
    time.sleep(2)

    assert reg_page.get_alert_text() == 'User already exist'
    reg_page.accept_alert()


def test_with_registered_email_and_another_password(driver):
    reg_page = RegistrationPage(driver)

    user = User(
        f"doritos654@gmail.com",
        "mdmNN!223466"
    )

    reg_page.open_login_form()
    reg_page.fill_registration_form(user)
    reg_page.registration()
    time.sleep(2)

    assert reg_page.get_alert_text() == 'User already exist'
    reg_page.accept_alert()