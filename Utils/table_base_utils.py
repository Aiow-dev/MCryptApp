from typing import List, Tuple

from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QTableWidgetItem

from Assets import styles, constants


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