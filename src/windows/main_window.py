from PyQt5 import QtWidgets, QtGui

from src.controllers import (
    page,
    menu,
    cs_controllers,
    prm_controllers,
    ms_controllers,
    systems_controllers,
    dbl_pfr_controllers
)
from src.components import dialogs, setting, schemes, visual
from src.helpers import time, func, win
from src.windows import settings, messages
from src.views import main_win_light, main_win_dark


class MainWindowApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.__func_single = func.FuncSingleCall()
        self.__shortcut_settings = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+S'), self)
        self.__shortcut_settings.activated.connect(self.open_settings)
        self.__shortcut_settings.setEnabled(False)
        self.check_menu_line()

    def closeEvent(self, event):
        if setting.get_parameter('confirm-quit'):
            result = dialogs.question_msg_result(messages.CONFIRM_QUIT, 'Подтверждение выхода')
            event.ignore()
            if result:
                event.accept()
        else:
            event.accept()

    def open_settings(self):
        settings.show_settings_window(self.__func_single, self)

    def check_menu_line(self):
        if not setting.get_parameter('show-menu'):
            self.__shortcut_settings.setEnabled(True)


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


def init_menu_line_styles(theme_window, menu_style, ui):
    if menu_style == 'color-style':
        if theme_window == 'light':
            visual.menu_bar_light_color(ui.menu_bar)
        else:
            visual.menu_bar_dark_color(ui.menu_bar)
    elif theme_window == 'light':
        visual.menu_bar_light(ui.menu_bar)
    else:
        visual.menu_bar_dark(ui.menu_bar)


def init_sys_menu_line_styles(is_light, menu_style, ui):
    if menu_style == 'color-style':
        if is_light:
            visual.menu_bar_light_color_sys(ui.menu_bar)
        else:
            visual.menu_bar_dark_color_sys(ui.menu_bar)
    elif is_light:
        visual.menu_bar_light_sys(ui.menu_bar)
    else:
        visual.menu_bar_dark_sys(ui.menu_bar)


def init_pages(ui_window):
    prm_controllers.init_simple_permutation(ui_window)
    prm_controllers.init_key_permutation(ui_window)
    prm_controllers.init_double_permutation(ui_window)
    cs_controllers.init_classic_caesar(ui_window)
    cs_controllers.init_affine_caesar(ui_window)
    cs_controllers.init_key_caesar(ui_window)
    ms_controllers.init_magic_square(ui_window)
    dbl_pfr_controllers.init_double_playfair(ui_window)
    systems_controllers.init_playfair(ui_window)
    systems_controllers.init_trisemus(ui_window)
    systems_controllers.init_vigenere(ui_window)


def enable_visual_styles(window):
    theme = setting.get_parameter('theme')
    menu_line_style = setting.get_parameter('menu-style')
    tab_style = setting.get_parameter('tab-style')
    if theme == 'system':
        is_light = win.is_light_win_theme()
        ui = main_win_dark.Ui_main_window()
        if is_light:
            ui = main_win_light.Ui_main_window()
        ui.setupUi(window)
        init_win_styles(is_light, ui)
        init_sys_menu_line_styles(is_light, menu_line_style, ui)
        init_sys_tab_styles(is_light, tab_style, ui)
    elif theme == 'time':
        current_hour = time.get_current_hour()
        time_theme = 'dark'
        ui = main_win_dark.Ui_main_window()
        if 5 < current_hour < 18:
            time_theme = 'light'
            ui = main_win_light.Ui_main_window()
            schemes.light_scheme()
        ui.setupUi(window)
        init_menu_line_styles(time_theme, menu_line_style, ui)
        init_tab_styles(time_theme, tab_style, ui)
    else:
        ui = main_win_dark.Ui_main_window()
        if theme == 'light':
            ui = main_win_light.Ui_main_window()
            schemes.light_scheme()
        ui.setupUi(window)
        init_menu_line_styles(theme, menu_line_style, ui)
        init_tab_styles(theme, tab_style, ui)
    init_elements(ui)
    return ui


def init_window(window):
    ui = enable_visual_styles(window)
    init_pages(ui)
    page.init_page(ui)
    menu.init_menu(window, ui)


def show_main_window(window):
    init_window(window)
    window.show()
