import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from View import main_window

from Core.Controllers import controllers_wrapper


def controller_binding(controllers_wrapper_obj):
    pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = main_window.Ui_main_window()
    ui.setupUi(MainWindow)
    MainWindow.show()

    controllers_wrapper_obj = controllers_wrapper.ControllersWrapper(ui)

    controller_binding(controllers_wrapper_obj)

    sys.exit(app.exec_())
