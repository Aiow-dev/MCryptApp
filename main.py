import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from View import main_window

from Assets import styles

from Controllers import controllers_wrapper, event_controllers_wrapper, menu_controllers_wrapper

from Utils.StyleUtils import style_utils


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    ui: main_window.Ui_main_window = main_window.Ui_main_window()
    MainWindow: QMainWindow = QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    controllers_wrapper_obj: controllers_wrapper.ControllersWrapper \
        = controllers_wrapper.ControllersWrapper(ui)

    controllers_wrapper_obj.controller_binding()

    event_controllers_wrapper_obj: event_controllers_wrapper.EventControllersWrapper \
        = event_controllers_wrapper.EventControllersWrapper(ui, styles.DEFAULT_COLORS)

    event_controllers_wrapper_obj.event_controller_binding()

    menu_controllers_wrapper_obj: menu_controllers_wrapper.MenuControllersWrapper \
        = menu_controllers_wrapper.MenuControllersWrapper(ui)

    menu_controllers_wrapper_obj.menu_controller_binding()

    style_utils.styles_binding(ui)

    sys.exit(app.exec_())
