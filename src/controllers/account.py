from src.services import user_service
from src.components import dialogs
from src.windows import main_window


def register_account(form, form_ui, window):
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
                user_service.set_authenticated('Authenticated')
                form.close()
                main_window.show_main_window(window)
        else:
            dialogs.show_err_msg(msg, 'Ошибка регистрации')


def login_account(form, form_ui, window):
    username = form_ui.login_username_txt.text().strip()
    form_ui.login_username_txt.setText(username)
    password = form_ui.login_password_txt.text()
    result = user_service.login_user(username, password)
    status = result.get('status')
    msg = result.get('msg')
    if status is not None and msg is not None:
        if status:
            user_service.set_authenticated('Authenticated')
            dialogs.show_info_msg(msg, 'Вход в учетную запись')
            form.close()
            main_window.show_main_window(window)
        else:
            dialogs.show_err_msg(msg, 'Ошибка входа')


def init_account(form, form_ui, window):
    form_ui.btn_registration.clicked.connect(lambda: register_account(form, form_ui, window))
    form_ui.btn_login.clicked.connect(lambda: login_account(form, form_ui, window))
