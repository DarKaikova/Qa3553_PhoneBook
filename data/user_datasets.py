# * Подготовка наборов данных (Users) для авторизации и регистрации
# * -------------------------------------------------------------
# * ЗАЧЕМ: Берем готовые объекты пользователей (invalid_email_user и др.)
# * и вешаем на них ярлыки id="..." для красивого отображения в pytest.
# * -------------------------------------------------------------

import pytest

# * Импортируем готовые объекты пользователей и функцию/данные из модуля data
from data.user_data import invalid_email_user, invalid_password_user, create_user

# * 1. Список пользователей для проверки НЕУСПЕШНОГО ВХОДА (Login)
INVALID_LOGIN_USERS = [
    # * pytest.param(объект_пользователя, id="понятное_имя_в_отчете")
    pytest.param(invalid_email_user, id="invalid_email"),
    pytest.param(invalid_password_user, id="invalid_password"),
    pytest.param(create_user, id="unregistered_user"),
]

# * 2. Список пользователей для проверки НЕУСПЕШНОГО СОЗДАНИЯ АККАУНТА (Registration)
INVALID_REGISTRATION_USERS = [
    pytest.param(invalid_email_user, id="invalid-email"),
    pytest.param(invalid_password_user, id="invalid-password"),
]

# * -------------------------------------------------------------
# * КАК ЭТО БУДЕТ ВЫГЛЯДЕТЬ В ФАЙЛЕ С ТЕСТАМИ:
# *
# * @pytest.mark.parametrize("user", INVALID_LOGIN_USERS)
# * def test_login_negative(user):
# *     # Тест запустится 3 раза для разных пользователей
# *     pass
# *
# * В консоли PyCharm будет видно:
# * test_login_negative[invalid_email] PASSED
# * test_login_negative[invalid_password] PASSED
# * test_login_negative[unregistered_user] PASSED
# * -------------------------------------------------------------