import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from views import main_window
from controllers import (
    prm_controllers,
    cs_controllers,
    ms_controllers,
    dbl_pfr_controllers,
    systems_controllers,
    page,
    menu,
)
from components import schemes, setting


def init_styles(ui_window):
    theme = setting.app_theme()
    if theme == 'light':
        schemes.light_scheme(ui_window)
    else:
        schemes.dark_scheme(ui_window)
    # widgets.menu_bar_dark(ui.menu_bar)


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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = main_window.Ui_main_window()
    MainWindow = QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    init_styles(ui)
    init_pages(ui)
    page.init_page(ui)
    menu.init_menu(MainWindow, ui)
    sys.exit(app.exec_())
