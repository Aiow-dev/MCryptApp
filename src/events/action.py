from PyQt5 import QtGui

from src.components import enc_tables, dialogs


def set_shortcut(ui_obj, shortcut):
    ui_obj.setShortcut(QtGui.QKeySequence(shortcut))


def set_tbl_rank(tbl_obj, text_obj, max_limit):
    try:
        rank = int(text_obj.text())
        if 0 < rank < max_limit:
            tbl_obj.setRowCount(rank)
            tbl_obj.setColumnCount(rank)
    except ValueError as value_error:
        tbl_obj.setRowCount(1)
        tbl_obj.setColumnCount(1)


def set_tbl_row(tbl_obj, text_obj, max_limit):
    try:
        number = int(text_obj.text())
        if 0 < number < max_limit:
            tbl_obj.setRowCount(number)
    except ValueError as value_error:
        tbl_obj.setRowCount(1)


def set_tbl_clm(tbl_obj, text_obj, max_limit):
    try:
        number = int(text_obj.text())
        if 0 < number < max_limit:
            tbl_obj.setColumnCount(number)
    except ValueError as value_error:
        tbl_obj.setColumnCount(1)


def set_rand_tbl(tbl_obj, check_obj, charset):
    if check_obj.isChecked():
        enc_tables.table_rand(tbl_obj, charset)
    else:
        tbl_obj.clear()


def tbl_size_charset(check_obj, tbl_rows, tbl_columns, charset):
    if not check_obj.isChecked():
        return
    if tbl_rows * tbl_columns > len(charset):
        dialogs.show_err_msg(
            f'Размер таблицы ({tbl_rows}x{tbl_columns}) превышает количество символов ({len(charset)})',
            'Ошибка')
