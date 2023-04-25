from PyQt5 import QtGui


def set_shortcut(ui_obj, shortcut):
    ui_obj.setShortcut(QtGui.QKeySequence(shortcut))
