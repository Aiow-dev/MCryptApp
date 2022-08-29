import sys
from typing import Dict

from PyQt5.QtWidgets import QApplication

from View import main_window

from Core.Helpers.HelpersUI import style_helpers
from Core.Helpers.HelpersUI import styles
from Core.Helpers.HelpersUI import widgets

from Core.Controllers import controllers_wrapper
from Core.Controllers import event_controllers_wrapper
from Core.Controllers import menu_controllers_wrapper


def styles_binding(ui: main_window.Ui_main_window) -> None:
    style_helpers.set_menu_bar_dark_style(ui.menu_bar)


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    ui: main_window.Ui_main_window = main_window.Ui_main_window()
    MainWindow: widgets.Window = widgets.Window(ui)
    ui.setupUi(MainWindow)
    MainWindow.show()

    styles_binding(ui)

    controllers_wrapper_obj: controllers_wrapper.ControllersWrapper \
        = controllers_wrapper.ControllersWrapper(ui)

    controllers_wrapper_obj.controller_binding()

    colors: Dict[str, styles.Color] = {'default': styles.Color.dark_charcoal, 'error': styles.Color.orange_red}

    event_controllers_wrapper_obj: event_controllers_wrapper.EventControllersWrapper \
        = event_controllers_wrapper.EventControllersWrapper(ui, colors)

    event_controllers_wrapper_obj.event_controller_binding()

    menu_controllers_wrapper_obj: menu_controllers_wrapper.MenuControllersWrapper \
        = menu_controllers_wrapper.MenuControllersWrapper(ui)

    menu_controllers_wrapper_obj.menu_controller_binding()

    sys.exit(app.exec_())
