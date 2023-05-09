from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from views import settings_window


class SettingsWindow(QtWidgets.QWidget):
    def __init__(self, func_single, parent, flags):
        self.__func_single = func_single
        super().__init__(parent, flags)

    def show(self):
        if self.__func_single.is_call():
            super().show()

    def closeEvent(self, event):
        self.__func_single.reset()
        super().closeEvent(event)


def switch_settings_page(ui, index):
    return lambda: ui.section_widget.setCurrentIndex(index)


def init_settings_panel(ui):
    ui.btn_program_info.clicked.connect(switch_settings_page(ui, 0))
    ui.btn_color_style.clicked.connect(switch_settings_page(ui, 1))
    ui.btn_privacy_policy.clicked.connect(switch_settings_page(ui, 2))


def show_settings_window(func_single, parent):
    form = SettingsWindow(func_single, parent, Qt.Window)
    form.setFixedSize(1060, 740)
    ui = settings_window.Ui_Form()
    ui.setupUi(form)
    init_settings_panel(ui)
    form.show()
