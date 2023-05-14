from PyQt5 import QtWidgets
from PyQt5 import QtGui

from controllers import (
    prm_controllers,
    cs_controllers,
    ms_controllers,
    dbl_pfr_controllers,
    systems_controllers,
)
from components import schemes, dialogs, setting
from helpers import time, func
from views import main_win_dark, main_win_light
from windows import settings, messages


class MainWindowApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.__func_single = func.FuncSingleCall()
        self.shortcut_settings = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+S'), self)
        self.shortcut_settings.activated.connect(self.open_settings)
        self.shortcut_settings.setEnabled(False)
        self.check_menu_line()

    def closeEvent(self, event):
        if setting.get_parameter('confirm-quit'):
            result = dialogs.question_msg(self, messages.CONFIRM_QUIT, 'Подтверждение выхода...')
            event.ignore()
            if result:
                event.accept()
        else:
            event.accept()

    def open_settings(self):
        settings.show_settings_window(self.__func_single, self)

    def check_menu_line(self):
        if not setting.get_parameter('show-menu'):
            self.shortcut_settings.setEnabled(True)


def init_styles(theme_window, ui_window):
    if theme_window == 'light':
        schemes.light_scheme(ui_window)
    else:
        schemes.dark_scheme(ui_window)


def init_elements(ui_window):
    menu_line_status = setting.get_parameter('show-menu')
    quick_panel_status = setting.get_parameter('show-quick-panel')
    if not menu_line_status:
        ui_window.menu_bar.setHidden(True)
    if not quick_panel_status:
        ui_window.status_frame.setVisible(False)
        ui_window.enc_combo_box.setVisible(False)


def init_win_styles(is_light_win, ui_window):
    schemes.system_scheme(ui_window, is_light_win)


def init_time_styles():
    current_hour = time.get_current_hour()
    if 5 < current_hour < 18:
        ui_win = main_win_light.Ui_main_window()
        schemes.light_scheme(ui_win)
    else:
        ui_win = main_win_dark.Ui_main_window()
        schemes.dark_scheme(ui_win)


def init_tab_styles(theme_window, tab_style, ui):
    if tab_style == 'radius':
        if theme_window == 'light':
            schemes.light_tab_rad_scheme(ui)
        else:
            schemes.dark_tab_rad_scheme(ui)
    elif tab_style == 'top-radius':
        if theme_window == 'light':
            schemes.light_tab_top_rad_scheme(ui)
        else:
            schemes.dark_tab_top_rad_scheme(ui)
    elif tab_style == 'corner-radius':
        if theme_window == 'light':
            schemes.light_tab_corn_rad_scheme(ui)
        else:
            schemes.dark_tab_corn_rad_scheme(ui)
    elif theme_window == 'light':
        schemes.light_tab_corn_scheme(ui)
    else:
        schemes.dark_tab_corn_scheme(ui)


def init_sys_tab_styles(is_light, tab_style, ui):
    if tab_style == 'radius':
        if is_light:
            schemes.light_sys_tab_rad_scheme(ui)
        else:
            schemes.dark_sys_tab_rad_scheme(ui)
    elif tab_style == 'top-radius':
        if is_light:
            schemes.light_sys_tab_top_rad_scheme(ui)
        else:
            schemes.dark_sys_tab_top_rad_scheme(ui)
    elif tab_style == 'corner-radius':
        if is_light:
            schemes.light_sys_tab_corn_rad_scheme(ui)
        else:
            schemes.dark_sys_tab_corn_rad_scheme(ui)
    elif is_light:
        schemes.light_sys_tab_corn_scheme(ui)
    else:
        schemes.dark_sys_tab_corn_scheme(ui)


def init_pages(parent, ui_window):
    prm_controllers.init_simple_permutation(parent, ui_window)
    prm_controllers.init_key_permutation(parent, ui_window)
    prm_controllers.init_double_permutation(parent, ui_window)
    cs_controllers.init_classic_caesar(ui_window)
    cs_controllers.init_affine_caesar(ui_window)
    cs_controllers.init_key_caesar(ui_window)
    ms_controllers.init_magic_square(parent, ui_window)
    dbl_pfr_controllers.init_double_playfair(ui_window)
    systems_controllers.init_playfair(ui_window)
    systems_controllers.init_trisemus(ui_window)
    systems_controllers.init_vigenere(ui_window)
