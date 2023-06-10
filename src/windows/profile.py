from PyQt5 import QtWidgets


def registration_account_page(form_ui):
    form_ui.account_wgt.setCurrentIndex(0)


def login_account_page(form_ui):
    form_ui.account_wgt.setCurrentIndex(1)


def init_elements(form_ui):
    pass_fields = [form_ui.registration_password_txt, form_ui.registration_confirm_password_txt,
                   form_ui.login_password_txt]
    for field in pass_fields:
        field.setEchoMode(QtWidgets.QLineEdit.Password)
