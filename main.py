import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from View import main_window

from Core.Helpers.HelpersUI import style_helpers
from Core.Helpers.HelpersUI import styles

from Core.Controllers import controllers_wrapper


def styles_binding(ui):
    style_helpers.set_menu_bar_background(ui.menu_bar, styles.Color.dark_charcoal)


def controller_binding(controllers_wrapper_obj):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main_window.Ui_main_window()
    ui.setupUi(MainWindow)
    MainWindow.show()

    styles_binding(ui)

    controllers_wrapper_obj = controllers_wrapper.ControllersWrapper(ui)

    controller_binding(controllers_wrapper_obj)

    sys.exit(app.exec_())
