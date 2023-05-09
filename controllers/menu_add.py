from PyQt5.QtWidgets import qApp

from components import windows, app, dialogs
from controllers import menu


def settings_menu():
    dialogs.show_info_msg('Переход в настройки в данном окне недоступен. Перейдите в главное окно!', 'Информация')


def new_window_menu():
    dialogs.show_info_msg('Создание окна в данном окне недоступно. Перейдите в главное окно!', 'Информация')


def init_menu_add(ui):
    ui.action_program_info.triggered.connect(windows.show_program_info)
    ui.action_settings_win.triggered.connect(settings_menu)
    ui.action_new_win.triggered.connect(new_window_menu)
    ui.action_exit.triggered.connect(qApp.quit)
    ui.action_reboot.triggered.connect(app.restart)
    menu.init_menu_pages(ui)
