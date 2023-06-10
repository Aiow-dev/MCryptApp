import hashlib

from src.helpers import file


def init_userdata():
    file.create_dir('../user')


def set_username(username):
    with open('../user/username.txt', 'w+') as f:
        f.write(username)


def set_password(password):
    with open('../user/password.txt', 'w+') as f:
        f.write(password)


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

    hash_m = hashlib.sha3_256()
    hash_m.update(bytes(password, 'utf-8'))
    password_hash = hash_m.hexdigest()
    set_username(username)
    set_password(password_hash)
    return {'status': True, 'msg': 'Регистрация успешна!'}


def login_user(username, password):
    name = username.strip()
    if not name:
        return {'status': False, 'msg': 'Имя пользователя не заполнено или содержит только пробелы!'}
    if not password:
        return {'status': False, 'msg': 'Поле пароля не заполнено!'}

    try:
        with open('../user/username.txt', 'r') as f:
            file_username = f.read()
            if file_username != name:
                return {'status': False, 'msg': 'Имя пользователя или пароль не совпадают!'}

        with open('../user/password.txt', 'r') as f:
            file_password = f.read()
            hash_m = hashlib.sha3_256()
            hash_m.update(bytes(password, 'utf-8'))
            password_hash = hash_m.hexdigest()
            if file_password != password_hash:
                return {'status': False, 'msg': 'Имя пользователя или пароль не совпадают!'}
            return {'status': True, 'msg': 'Вход успешен!'}
    except FileNotFoundError as file_error:
        return {'status': False, 'msg': 'Учетной записи не существует!'}
