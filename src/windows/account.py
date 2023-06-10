from PyQt5 import QtWidgets

from src.views import account_form
from . import profile
from src.controllers import account


def enable_visual_styles(form_ui):
    profile.init_elements(form_ui)


def init_load_pages(form, form_ui, window):
    form_ui.btn_registration_page.clicked.connect(lambda: profile.registration_account_page(form_ui))
    form_ui.btn_login_page.clicked.connect(lambda: profile.login_account_page(form_ui))
    account.init_account(form, form_ui, window)


def show_account_window(window):
    account_window = QtWidgets.QWidget()
    account_window.setFixedSize(934, 631)
    ui = account_form.Ui_account_form()
    ui.setupUi(account_window)
    enable_visual_styles(ui)
    init_load_pages(account_window, ui, window)
    account_window.show()
    return account_window
