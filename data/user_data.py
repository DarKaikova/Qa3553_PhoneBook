from faker import Faker

from models.user import User

fake = Faker()


def create_user(email=None, password=None):
    return User(
        email=email if email is not None else fake.unique.email(),
        password=password if password is not None else fake.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
    )

EXISTING_USER_EMAIL = "darion@gmail.com"
EXISTING_USER_PASSWORD = "Ddar126$!"
INVALID_EMAIL = "darigmail.com"
INVALID_PASSWORD = "Ddar123"


def exiting_user():
    return create_user(email=EXISTING_USER_EMAIL, password=EXISTING_USER_PASSWORD)

def invalid_email_user():
    return create_user(email=INVALID_EMAIL, password=EXISTING_USER_PASSWORD)

def invalid_password_user():
    return create_user(email=EXISTING_USER_EMAIL, password=INVALID_PASSWORD)