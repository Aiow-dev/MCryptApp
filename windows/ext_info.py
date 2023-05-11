from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from views import ext_info_win_dark


class ExtendedInfoWindow(QtWidgets.QWidget):
    def __init__(self, func_single, parent, flags):
        self.__func_single = func_single
        super().__init__(parent, flags)

    def show(self):
        if self.__func_single.is_call():
            super().show()

    def closeEvent(self, event):
        self.__func_single.reset()
        super().closeEvent(event)


def show_settings_window(func_single, parent):
    form = ExtendedInfoWindow(func_single, parent, Qt.Window)
    form.setFixedSize(1589, 963)
    ui = ext_info_win_dark.Ui_extended_info_form()
    ui.setupUi(form)
    form.show()
