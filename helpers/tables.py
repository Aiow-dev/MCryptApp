from random import choice

from PyQt5.QtGui import QBrush


def transpose_table(tbl):
    clm_len = len(tbl[0])
    row_len = len(tbl)
    result = []
    for clm in range(clm_len):
        part_row = [tbl[row][clm] for row in range(row_len)]
        result.append(part_row)
    return result


def table(part_values, f_part, tbl_obj, h_headers=(), v_headers=()):
    tbl_obj.setHorizontalHeaderLabels(h_headers)
    tbl_obj.setVerticalHeaderLabels(v_headers)
    for part_num, part_value in enumerate(part_values):
        f_part(part_num, part_value, tbl_obj)


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
    return ''.join(key + '\t->\t' + value + f'\n{placeholder_len}\n'
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
    return [[tbl_wgt.item(row, column).text().upper() for column in range(size[1])] for row in range(size[0])]


def table_num_items(tbl_wgt):
    size = table_size(tbl_wgt)
    return [[int(tbl_wgt.item(row, column).text()) for column in range(size[1])] for row in range(size[0])]


def fill_table_rand(tbl_wgt, charset):
    size = table_size(tbl_wgt)
    if size[0] * size[1] > len(charset):
        return
    tbl_items = unique_rand_table(size[0], size[1], charset)
    table(tbl_items, table_row, tbl_wgt)


def clear_table(tbl_wgt):
    tbl_wgt.clear()


def table_item(item_value, color):
    item = QTableWidgetItem(item_value)
    item.setForeground(QBrush(color.value))
    return item


def table_column(num_column, column_value, tbl_obj, color):
    for num_row, value in enumerate(column_value):
        tbl_obj.setItem(num_row, num_column, table_item(value, color))


def table_row(num_row, row_value, tbl_obj, color):
    for num_column, value in enumerate(row_value):
        tbl_obj.setItem(num_row, num_column, table_item(value, color))


def affine_column_headers(key_a_text, key_b_text):
    key_text = f'{key_a_text}t+{key_b_text}'
    return 't', key_text, 't', key_text, 't', key_text


def affine_num_column(key_a_text, key_b_text, start_t, end_t):
    letters_num = 33
    return [str((key_a_text * t + key_b_text) % letters_num) for t in range(start_t, end_t)]


def affine_letter_column(num_column_value, alphabet):
    return [alphabet[int(num_value)] for num_value in num_column_value]
