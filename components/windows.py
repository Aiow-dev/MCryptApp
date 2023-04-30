from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from components import dialogs
from views import settings_window


def show_program_info():
    txt = 'MCrypt 1.9.1 Preview\nMCryptTeam, 2023, все права защищены'
    dialogs.show_info_msg(txt, 'Информация о программе')


def show_settings_window(parent):
    form = QtWidgets.QWidget(parent, Qt.Window)
    form.setFixedSize(1060, 740)
    ui = settings_window.Ui_Form()
    ui.setupUi(form)
    form.show()
