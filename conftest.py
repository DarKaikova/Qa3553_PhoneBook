import pytest
from selenium import webdriver


@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) #неявное ожидание (чтобы сайт не ложился, если что-то не успело прогрузиться)
    driver.maximize_window() #расширение экрана
    driver.get("https://telranedu.web.app/")

    yield driver

    driver.quit()