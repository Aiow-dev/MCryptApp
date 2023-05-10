from PyQt5 import QtWidgets

from controllers import (
    prm_controllers,
    cs_controllers,
    ms_controllers,
    dbl_pfr_controllers,
    systems_controllers,
)
from components import schemes, dialogs, setting
from helpers import time
from views import main_win_dark, main_win_light


class MainWindowApp(QtWidgets.QMainWindow):
    def closeEvent(self, event):
        is_confirm_quit = setting.is_confirm_quit()
        if is_confirm_quit:
            result = dialogs.question_msg(self,
                                          'Вы уверены, что хотите выйти? Все несохраненные изменения будут утеряны!',
                                          'Подтверждение выхода...')
            event.ignore()
            if result:
                event.accept()
        else:
            event.accept()


def init_styles(theme_window, ui_window):
    if theme_window == 'light':
        schemes.light_scheme(ui_window)
    else:
        schemes.dark_scheme(ui_window)


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