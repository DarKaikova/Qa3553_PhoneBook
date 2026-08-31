import pytest
from selenium import webdriver
import random
import string
import time
from faker import Faker

from pages.login_page import LoginPage
from tests.test_login import VALID_PASSWORD, VALID_EMAIL


@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) #неявное ожидание (чтобы сайт не ложился, если что-то не успело прогрузиться)
    driver.maximize_window() #расширение экрана
    driver.get("https://telranedu.web.app/")

    yield driver

    driver.quit()


@pytest.fixture
def authenticated_driver(driver):
    login_page = LoginPage(driver)
    login_page.open_login_form()
    login_page.fill_email(VALID_EMAIL)
    login_page.fill_password(VALID_PASSWORD)
    login_page.submit_login()

    return driver








fake = Faker()

def generate_unique_email() -> str:
    # Создаем уникальный email на основе текущего времени (время постоянно меняется и уникальности точно не будет)
    timestamp = int(time.time())
    return f"user_{timestamp}@testmail.com"

def generate_valid_password():
    # Требования:
    # Заглавная буква
    # Строчная буква
    # Цифра
    # Спецсимвол из ["@","$","#","^","&","*","!"] - согласно документации
    uppercase = random.choice(string.ascii_uppercase)
    #ascii_uppercase — это заранее заготовленная строка внутри встроенной библиотеки string.
    #то есть грубо говоря - random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    special = random.choice(["@","$","#","^","&","*","!"])

    # Добавляем еще несколько случайных букв для длины
    extra_chars = "".join(
        random.choices(string.ascii_letters + string.digits, k=4) #k-количество рандомных символов, которое нам нужно
    )

    # Собираем
    password_list = list(uppercase + lowercase + digit + special + extra_chars)
    random.shuffle(password_list)

    return "".join(password_list)
