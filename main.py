import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from View import main_window

from Controllers.controllers_wrapper import ControllersWrapper
from Controllers.event_controllers_wrapper import EventControllersWrapper
from Controllers.menu_controllers_wrapper import MenuControllersWrapper

from Utils.StyleUtils import style_utils


if __name__ == '__main__':
    app: QApplication = QApplication(sys.argv)
    ui: main_window.Ui_main_window = main_window.Ui_main_window()
    MainWindow: QMainWindow = QMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    control: ControllersWrapper = ControllersWrapper(ui)
    control.controller_binding()

    event_control: EventControllersWrapper = EventControllersWrapper(ui)
    event_control.event_controller_binding()

    menu_control: MenuControllersWrapper = MenuControllersWrapper(ui)
    menu_control.menu_controller_binding()

    style_utils.styles_binding(ui)

    sys.exit(app.exec_())
