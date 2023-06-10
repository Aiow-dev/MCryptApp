from src.services import user_service
from src.components import dialogs


def register_user(form_ui):
    username = form_ui.registration_username_txt.text().strip()
    form_ui.registration_username_txt.setText(username)
    password = form_ui.registration_password_txt.text()
    confirm_password = form_ui.registration_confirm_password_txt.text()
    result = user_service.create_user(username, password, confirm_password)
    status = result.get('status')
    msg = result.get('msg')
    if status is not None and msg is not None:
        if status:
            dialogs.show_info_msg(msg, 'Регистрация учетной записи')
            if user_service.login_user(username, password).get('status'):
                form_ui.btn_next_account.click()
        else:
            dialogs.show_err_msg(msg, 'Ошибка регистрации')


def login_user(form_ui):
    username = form_ui.login_username_txt.text().strip()
    form_ui.login_username_txt.setText(username)
    password = form_ui.login_password_txt.text()
    result = user_service.login_user(username, password)
    status = result.get('status')
    msg = result.get('msg')
    if status is not None and msg is not None:
        if status:
            dialogs.show_info_msg(msg, 'Вход в учетную запись')
            form_ui.btn_next_account.click()
        else:
            dialogs.show_err_msg(msg, 'Ошибка входа')


def init_user(form_ui):
    form_ui.btn_registration.clicked.connect(lambda: register_user(form_ui))
    form_ui.btn_login.clicked.connect(lambda: login_user(form_ui))
