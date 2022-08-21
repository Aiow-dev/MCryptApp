from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow

from Core.Helpers.HelpersUI import utilities


class Window(QMainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self, ui=None):
        super(Window, self).__init__()

        self.ui = ui

        self.resized.connect(lambda: utilities.get_equal_tab_padding(self.ui.smp_types_tab, self.width()))
    
    def resizeEvent(self, event):
        self.resized.emit()

        return super(Window, self).resizeEvent(event)
