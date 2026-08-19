import pytest
from selenium import webdriver
import random
import string
import time
from faker import Faker

@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) #неявное ожидание (чтобы сайт не ложился, если что-то не успело прогрузиться)
    driver.maximize_window() #расширение экрана
    driver.get("https://telranedu.web.app/")

    yield driver

    driver.quit()

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
    # Спецсимвол из ['$','~','-','_']
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