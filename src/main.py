import sys

from PyQt5 import QtWidgets, QtCore

from src.windows import main_window, load
from src.components import app, setting


if __name__ == '__main__':
    app_obj = QtWidgets.QApplication(sys.argv)
    app.enable_visual_styles()
    MainWindow = main_window.MainWindowApp()

    is_load = setting.get_parameter('show-load')
    if is_load:
        load.show_load_window(MainWindow)
    else:
        main_window.show_main_window(MainWindow)

    qt_translator = QtCore.QTranslator()
    if qt_translator.load('../resources/qtbase_ru'):
        app_obj.installTranslator(qt_translator)

    sys.exit(app_obj.exec_())
