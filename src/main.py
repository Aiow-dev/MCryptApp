import sys

from PyQt5 import QtWidgets
from PyQt5 import QtCore

from src.windows import main_window

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    qt_translator = QtCore.QTranslator()
    if qt_translator.load('../resources/qtbase_ru'):
        app.installTranslator(qt_translator)

    MainWindow = main_window.MainWindowApp()
    main_window.init_window(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
