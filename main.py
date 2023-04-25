import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from views import main_window
from controllers import (
    prm_controllers,
    cs_controllers,
    page,
    menu,
)
from components import menu_bars


def init_styles(ui_window):
    menu_bars.menu_bar_dark(ui_window.menu_bar)


def init_pages(ui_window):
    prm_controllers.init_simple_permutation(ui_window)
    prm_controllers.init_key_permutation(ui_window)
    prm_controllers.init_double_permutation(ui_window)
    cs_controllers.init_classic_caesar(ui_window)
    cs_controllers.init_affine_caesar(ui_window)
    cs_controllers.init_key_caesar(ui_window)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = main_window.Ui_main_window()
    MainWindow = QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    init_pages(ui)
    page.init_page(ui)
    menu.init_menu(ui)
    init_styles(ui)
    sys.exit(app.exec_())
