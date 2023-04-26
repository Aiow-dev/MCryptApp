from PyQt5 import QtGui


def set_shortcut(ui_obj, shortcut):
    ui_obj.setShortcut(QtGui.QKeySequence(shortcut))


def set_tbl_rank(tbl_obj, text_obj, limit):
    try:
        rank = int(text_obj.text())
        if 0 < rank < limit:
            tbl_obj.setRowCount(rank)
            tbl_obj.setColumnCount(rank)
    except ValueError as value_error:
        tbl_obj.setRowCount(1)
        tbl_obj.setColumnCount(1)
