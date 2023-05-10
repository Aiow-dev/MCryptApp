from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from views import settings_win_dark
from components import widgets
from controllers import color_style_controllers


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


def init_settings_styles(ui):
    widgets.frame_compl_color_style_sys(ui.compl_light_win_color)
    widgets.frame_compl_color_style_sys(ui.compl_dark_win_color)
    widgets.frame_color_style_sys(ui.accent_light_win_color)
    widgets.frame_color_style_sys(ui.accent_dark_win_color)



def init_settings_panel(ui):
    ui.btn_program_info.clicked.connect(switch_settings_page(ui, 0))
    ui.btn_color_style.clicked.connect(switch_settings_page(ui, 1))
    ui.btn_privacy_policy.clicked.connect(switch_settings_page(ui, 2))


def init_settings_pages(ui):
    color_style_controllers.init_color_styles(ui)


def show_settings_window(func_single, parent):
    form = SettingsWindow(func_single, parent, Qt.Window)
    form.setFixedSize(1060, 740)
    ui = settings_win_dark.Ui_settings_form()
    ui.setupUi(form)
    init_settings_styles(ui)
    init_settings_panel(ui)
    init_settings_pages(ui)
    form.show()
