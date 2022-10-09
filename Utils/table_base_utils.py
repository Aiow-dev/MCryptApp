from typing import List, Tuple
from random import choice

from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QTableWidgetItem

from Assets import styles, constants


def transpose_table(tbl):
    clm_len: int = len(tbl[0])
    row_len: int = len(tbl)

    result = []

    for clm in range(clm_len):
        part_row = [tbl[row][clm] for row in range(row_len)]

        result.append(part_row)

    return result


def table(part_values, f_part, table_obj, h_headers=(), v_headers=()) -> None:
    table_obj.setHorizontalHeaderLabels(h_headers)
    table_obj.setVerticalHeaderLabels(v_headers)

    for part_num, part_value in enumerate(part_values):
        f_part(part_num, part_value, table_obj)


def unique_rand_table(num_row, num_column, charset):
    tbl = []

    for _ in range(num_row):
        part_table = []

        for _ in range(num_column):
            rand_symbol = choice(charset)
            part_table.append(rand_symbol)

            charset = charset.replace(rand_symbol, '')

        tbl.append(part_table)

    return tbl


def table_size(table_wgt):
    return table_wgt.rowCount(), table_wgt.columnCount()


def table_up_items(table_wgt):
    size = table_size(table_wgt)

    return [[table_wgt.item(row, column).text().upper() for column in range(size[1])] for row in range(size[0])]


def table_num_items(table_widget):
    size = table_size(table_widget)

    return [[int(table_widget.item(row, column).text()) for column in range(size[1])] for row in range(size[0])]


def fill_table_rand(tbl_wgt):
    size = table_size(tbl_wgt)

    if size[0] * size[1] > len(constants.EXT_RU_ALPHABET):
        return

    tbl_items = unique_rand_table(size[0], size[1], constants.EXT_RU_ALPHABET.upper())

    table(tbl_items, table_row, tbl_wgt)


def clear_table(tbl_wgt):
    tbl_wgt.clear()


def table_item(item_value, color: styles.Color) -> QTableWidgetItem:
    item: QTableWidgetItem = QTableWidgetItem(item_value)
    item.setForeground(QBrush(color.value))

    return item


def table_column(num_column, column_value, table_obj):
    for num_row, value in enumerate(column_value):
        table_obj.setItem(num_row, num_column, table_item(value, styles.Color.q_white))


def table_row(num_row, row_value, table_obj):
    for num_column, value in enumerate(row_value):
        table_obj.setItem(num_row, num_column, table_item(value, styles.Color.q_white))


def affine_column_headers(key_a_text: int, key_b_text: int) -> Tuple[str, str, str, str, str, str]:
    key_text = f'{key_a_text}t+{key_b_text}'

    return 't', key_text, 't', key_text, 't', key_text


def affine_num_column(key_a_text: int, key_b_text: int,
                      start_t: int, end_t: int) -> List[str]:
    return [str((key_a_text * t + key_b_text) % constants.NUM_LETTER) for t in range(start_t, end_t)]


def affine_letter_column(num_column_value) -> List[str]:
    return [constants.RU_ALPHABET[int(num_value)] for num_value in num_column_value]
