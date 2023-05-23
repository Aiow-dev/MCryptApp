from random import choice

from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QTableWidgetItem


def transpose_table(tbl):
    clm_len = len(tbl[0])
    row_len = len(tbl)
    result = []
    for clm in range(clm_len):
        part_row = [tbl[row][clm] for row in range(row_len)]
        result.append(part_row)
    return result


def table_to_str(msg_tbl):
    return ''.join('\t'.join(row) + '\n' for row in msg_tbl)


def table_to_str_size(msg_tbl, size_h=1, size_v=1):
    tbl_str = ''
    for row in msg_tbl:
        for symbol in row:
            tbl_str += f'{f"{symbol}": <{size_h}}'
        tbl_str += '\n' * size_v
    return tbl_str


def table_dict_to_str(tbl_dict, placeholder_len=30):
    placeholder = '-' * placeholder_len
    return ''.join(key + '\t->\t' + value + f'\n{placeholder}\n'
                   for key, value in tbl_dict.items())


def tables_to_str(msg_tbl, enc_msg_tbl):
    table_dict = {
        msg_tbl[index]: enc_msg_tbl[index]
        for index in range(len(msg_tbl))
    }
    return table_dict_to_str(table_dict)


def unique_rand_table(num_row, num_column, charset):
    tbl = []
    for _ in range(num_row):
        part_tbl = []
        for _ in range(num_column):
            rand_symbol = choice(charset)
            part_tbl.append(rand_symbol)
            charset = charset.replace(rand_symbol, '')
        tbl.append(part_tbl)
    return tbl


def table_size(tbl_wgt):
    return tbl_wgt.rowCount(), tbl_wgt.columnCount()


def table_up_items(tbl_wgt):
    size = table_size(tbl_wgt)
    items = []
    for row in range(size[0]):
        row_items = []
        for column in range(size[1]):
            item_obj = tbl_wgt.item(row, column)
            if item_obj is None:
                break
            item = item_obj.text().upper()
            row_items.append(item)
        items.append(row_items)
    return items


def table_num_items(tbl_wgt):
    size = table_size(tbl_wgt)
    return [[int(tbl_wgt.item(row, column).text()) for column in range(size[1])] for row in range(size[0])]


def table_item(item_value, color):
    item = QTableWidgetItem(item_value)
    item.setForeground(QBrush(color))
    return item


def affine_column_headers(key_a, key_b):
    sign = '' if key_b < 0 else '+'
    key_text = f'{key_a}t{sign}{key_b}'
    return 't', key_text, 't', key_text, 't', key_text


def affine_num_column(key_a, key_b, start_t, end_t):
    letters_num = 33
    return [str((key_a * t + key_b) % letters_num) for t in range(start_t, end_t)]


def affine_letter_column(num_column_value, alphabet):
    return [alphabet[int(num_value)] for num_value in num_column_value]


def table(part_values, f_part, tbl_obj, h_headers=(), v_headers=()):
    tbl_obj.setHorizontalHeaderLabels(h_headers)
    tbl_obj.setVerticalHeaderLabels(v_headers)
    for part_num, part_value in enumerate(part_values):
        f_part(part_num, part_value, tbl_obj)
