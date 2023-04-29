from helpers import text, tables, items
from helpers.tables import table_item, table_size, unique_rand_table, table
from components import colors


def table_text(columns_values, tbl_header=None, columns_headers=None, placeholder='-', len_tbl_section=-1):
    tbl_str = ''
    len_section = len_tbl_section

    if len_section == -1:
        len_section = len(max(columns_headers, key=len))

    len_tbl = len_section * len(columns_headers)
    placeholder_line = placeholder * len_tbl + '\n'

    if tbl_header:
        tbl_str += placeholder_line
        tbl_str += f'{f"{tbl_header}": ^{len_tbl}}\n'
        tbl_str += placeholder_line

    if columns_headers:
        tbl_str += f'{f"{columns_headers[0]}": <{len_section}}'

        for index_column_header in range(1, len(columns_headers) - 1):
            tbl_str += f'{f"{columns_headers[index_column_header]}": ^{len_section}}'

        tbl_str += f'{f"{columns_headers[-1]}": >{len_section}}\n'

    tbl_str += placeholder_line

    for index_column_value in range(len(columns_values[0])):
        tbl_str += f'{f"{columns_values[0][index_column_value]}": <{len_section}}'

        for index_column in range(1, len(columns_values) - 1):
            tbl_str += f'{f"{columns_values[index_column][index_column_value]}": ^{len_section + 3}}'

        tbl_str += f'{f"{columns_values[-1][index_column_value]}": >{len_section}}\n'
        index_column_value += 1

    tbl_str += placeholder_line

    return tbl_str


def key_permutation_table_text(key_tbl):
    key = '\t'.join(key[0] for key in key_tbl).upper()
    one_letter_keys = ''.join(key[0] for key in key_tbl)
    key_indexes = '\t'.join(text.get_number_letter(one_letter_keys))
    part_tbl = tables.table_to_str(tables.transpose_table(list(key_tbl.values())))
    return f'{key}\n{key_indexes}\n{part_tbl}'


def double_permutation_table_text(msg_tbl, key_row, key_clm):
    result_tbl = ''
    h_header_row = '\t' + '\t'.join(sorted(key_clm))
    v_headers = sorted(key_row)
    for index_row, row in enumerate(msg_tbl):
        part_row = f'{v_headers[index_row]}\t'
        for clm in row:
            part_row += clm + '\t'
        result_tbl += part_row + '\n'
    return f'{h_header_row}\n{result_tbl}'


def affine_table_num_text(key_a_text, key_b_text):
    column_values = (
        [str(i) for i in range(11)], tables.affine_num_column(key_a_text, key_b_text, 0, 11),
        [str(i) for i in range(11, 22)], tables.affine_num_column(key_a_text, key_b_text, 11, 22),
        [str(i) for i in range(22, 33)], tables.affine_num_column(key_a_text, key_b_text, 22, 33)
    )
    return column_values, table_text(column_values, columns_headers=tables.affine_column_headers(
        key_a_text, key_b_text
    ))


def affine_table_letter_text(key_a_text, key_b_text, num_column_values, alphabet):
    column_values = (
        tables.affine_letter_column(num_column_values[0], alphabet),
        tables.affine_letter_column(num_column_values[1], alphabet),
        tables.affine_letter_column(num_column_values[2], alphabet),
        tables.affine_letter_column(num_column_values[3], alphabet),
        tables.affine_letter_column(num_column_values[4], alphabet),
        tables.affine_letter_column(num_column_values[5], alphabet)
    )
    return column_values, table_text(column_values, columns_headers=tables.affine_column_headers(
        key_a_text, key_b_text
    ))


def affine_table(key_a_text, key_b_text, column_values, tbl_obj):
    h_headers = tables.affine_column_headers(key_a_text, key_b_text)
    table(column_values, table_column, tbl_obj, h_headers=h_headers)


def caesar_key_table_text(replace_values, alphabet):
    column_headers = ('№', '->', '№', '->', '№', '->')
    column_values = (
        tables.affine_letter_column([str(i) for i in range(11)], alphabet),
        replace_values[:11],
        tables.affine_letter_column([str(i) for i in range(11, 22)], alphabet),
        replace_values[11:22],
        tables.affine_letter_column([str(i) for i in range(22, 33)], alphabet),
        replace_values[22:33]
    )

    return column_values, table_text(column_values, columns_headers=column_headers)


def caesar_key_table(column_values, table_obj):
    h_headers = ('№', '->', '№', '->', '№', '->')
    table(column_values, table_column, table_obj, h_headers=h_headers)


def vigenere_table_text(msg_txt, key_text, enc_msg_txt, alphabet):
    row_msg = list(msg_txt)
    row_key_word = list(text.repeat_on_str(msg_txt, key_text))
    row_index_key_word = list(text.get_index(row_key_word, alphabet))
    items.remove_item(' ', row_index_key_word)
    row_enc_msg = list(enc_msg_txt)
    enc_msg_table = [row_msg, row_key_word, row_index_key_word, row_enc_msg]
    return tables.table_to_str_size(enc_msg_table, 3, 2)


def vigenere_table(row_values, table_obj, alphabet):
    h_headers = list(alphabet)
    v_headers = [str(row) for row in range(32)]
    table(row_values, table_row, table_obj, h_headers, v_headers)


def table_row(num_row, row_value, tbl_obj, color=colors.ColorSet.white.value.to_rgb_q()):
    for num_column, value in enumerate(row_value):
        tbl_obj.setItem(num_row, num_column, table_item(value, color))


def table_column(num_column, column_value, tbl_obj, color=colors.ColorSet.white.value.to_rgb_q()):
    for num_row, value in enumerate(column_value):
        tbl_obj.setItem(num_row, num_column, table_item(value, color))


def table_rand(tbl_wgt, charset):
    size = table_size(tbl_wgt)
    if size[0] * size[1] > len(charset):
        return
    tbl_items = unique_rand_table(size[0], size[1], charset)
    table(tbl_items, table_row, tbl_wgt)
