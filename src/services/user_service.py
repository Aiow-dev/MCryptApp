import argon2

from src.helpers import file


def init_userdata():
    file.create_dir('../user')


def is_authenticated():
    try:
        with open('../user/authentication.txt', 'r') as f:
            status = f.read()
            ph = argon2.PasswordHasher()
            return ph.verify(status, 'Authenticated')
    except FileNotFoundError as file_error:
        return False
    except argon2.exceptions.VerifyMismatchError as verify_error:
        return False


def set_authenticated(status):
    with open('../user/authentication.txt', 'w+') as f:
        ph = argon2.PasswordHasher()
        status_hash = ph.hash(status)
        f.write(status_hash)


def create_user(username, password, confirm_password):
    name = username.strip()
    if not name:
        return {'status': False, 'msg': 'Имя пользователя не заполнено или содержит только пробелы!'}
    if not password:
        return {'status': False, 'msg': 'Поле пароля не заполнено!'}
    if not confirm_password:
        return {'status': False, 'msg': 'Поле подтверждения пароля не заполнено!'}

    if password != confirm_password:
        return {'status': False, 'msg': 'Пароли не совпадают!'}

    ph = argon2.PasswordHasher()
    username_hash = ph.hash(username)
    password_hash = ph.hash(password)

    with open('../user/username.txt', 'w+') as f:
        f.write(username_hash)

    with open('../user/password.txt', 'w+') as f:
        f.write(password_hash)

    return {'status': True, 'msg': 'Регистрация успешна!'}


def login_user(username, password):
    name = username.strip()
    if not name:
        return {'status': False, 'msg': 'Имя пользователя не заполнено или содержит только пробелы!'}
    if not password:
        return {'status': False, 'msg': 'Поле пароля не заполнено!'}

    try:
        ph = argon2.PasswordHasher()

        with open('../user/username.txt', 'r') as f:
            file_username = f.read()
            if not ph.verify(file_username, username):
                return {'status': False, 'msg': 'Имя пользователя или пароль не совпадают!'}

        with open('../user/password.txt', 'r') as f:
            file_password = f.read()
            return (
                {'status': True, 'msg': 'Вход успешен!'}
                if ph.verify(file_password, password)
                else {
                    'status': False,
                    'msg': 'Имя пользователя или пароль не совпадают!',
                }
            )
    except FileNotFoundError as file_error:
        return {'status': False, 'msg': 'Учетной записи не существует!'}
    except argon2.exceptions.VerifyMismatchError as verify_error:
        return {'status': False, 'msg': 'Имя пользователя или пароль не совпадают!'}
