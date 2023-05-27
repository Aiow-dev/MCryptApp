import sys

from PyQt5 import QtWidgets, QtCore

from src.windows import main_window
from src.components import app


if __name__ == '__main__':
    app_obj = QtWidgets.QApplication(sys.argv)
    app.enable_visual_styles()

    qt_translator = QtCore.QTranslator()
    if qt_translator.load('../resources/qtbase_ru'):
        app_obj.installTranslator(qt_translator)

    MainWindow = main_window.MainWindowApp()
    main_window.init_window(MainWindow)
    MainWindow.show()
    sys.exit(app_obj.exec_())
