import sys
from typing import Dict

from PyQt5.QtWidgets import QApplication, QMainWindow

from View import main_window

from Utils.StyleUtils import style_utils

from Assets import styles

from Controllers import controllers_wrapper, event_controllers_wrapper, menu_controllers_wrapper


def styles_binding(ui: main_window.Ui_main_window) -> None:
    style_utils.set_menu_bar_dark_style(ui.menu_bar)


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    ui: main_window.Ui_main_window = main_window.Ui_main_window()
    MainWindow: QMainWindow = QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    styles_binding(ui)

    controllers_wrapper_obj: controllers_wrapper.ControllersWrapper \
        = controllers_wrapper.ControllersWrapper(ui)

    controllers_wrapper_obj.controller_binding()

    event_controllers_wrapper_obj: event_controllers_wrapper.EventControllersWrapper \
        = event_controllers_wrapper.EventControllersWrapper(ui, styles.DEFAULT_COLORS)

    event_controllers_wrapper_obj.event_controller_binding()

    menu_controllers_wrapper_obj: menu_controllers_wrapper.MenuControllersWrapper \
        = menu_controllers_wrapper.MenuControllersWrapper(ui)

    menu_controllers_wrapper_obj.menu_controller_binding()

    sys.exit(app.exec_())
