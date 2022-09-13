from typing import List, Tuple

from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QTableWidgetItem

from Assets import styles, constants


def table_item(item_value, color: styles.Color) -> QTableWidgetItem:
    item: QTableWidgetItem = QTableWidgetItem(item_value)
    item.setForeground(QBrush(color.value))

    return item


def table_column(number_column, column_value, encryption_message_table_obj):
    for number_row, value in enumerate(column_value):
        encryption_message_table_obj.setItem(number_row, number_column, table_item(value, styles.Color.q_white))


def table_row(number_row, row_value, encryption_message_table_obj):
    for number_column, value in enumerate(row_value):
        encryption_message_table_obj.setItem(number_row, number_column, table_item(value, styles.Color.q_white))


def affine_column_headers(key_a_text: int, key_b_text: int) -> Tuple[str, str, str, str, str, str]:
    key_text = f'{key_a_text}t+{key_b_text}'

    return 't', key_text, 't', key_text, 't', key_text


def affine_num_column(key_a_text: int, key_b_text: int,
                      start_t: int, end_t: int) -> List[str]:
    number_letter: int = 33

    return [str((key_a_text * t + key_b_text) % number_letter) for t in range(start_t, end_t)]


def affine_letter_column(number_column_value) -> List[str]:
    return [constants.RU_ALPHABET[int(number_value)] for number_value in number_column_value]
