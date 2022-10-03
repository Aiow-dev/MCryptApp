from typing import List, Tuple, Dict

from Assets import constants

from Utils import item_utils, str_utils, table_base_utils


def table_to_str(msg_table: List[List[str]]) -> str:
    return ''.join('\t'.join(row) + '\n' for row in msg_table)


def table_to_str_size(msg_table: List[List[str]], size_h: int = 1, size_v: int = 1) -> str:
    table_str = ''

    for row in msg_table:
        for symbol in row:
            table_str += f'{f"{symbol}": <{size_h}}'

        table_str += '\n' * size_v

    return table_str


def table_dict_to_str(table_dict: Dict[str, str]) -> str:
    placeholder_len = 30

    return ''.join(key + '\t->\t' + value + f'\n{placeholder_len}\n'
                   for key, value in table_dict.items())


def tables_to_str(message_table: str, encrypt_message_table: str) -> str:
    table_dict: Dict[str, str] = {
        message_table[index]: encrypt_message_table[index]
        for index in range(len(message_table))
    }

    return table_dict_to_str(table_dict)


def table_text(columns_values: tuple, table_header: str = None, columns_headers: tuple = None,
               placeholder: str = '-', len_table_section: int = -1) -> str:
    table_str = ''

    len_section = len_table_section

    if len_section == -1:
        len_section = len(max(columns_headers, key=len))

    len_table = len_section * len(columns_headers)

    placeholder_line = placeholder * len_table + '\n'

    if table_header:
        table_str += placeholder_line
        table_str += f'{f"{table_header}": ^{len_table}}\n'
        table_str += placeholder_line

    if columns_headers:
        table_str += f'{f"{columns_headers[0]}": <{len_section}}'

        for index_column_header in range(1, len(columns_headers) - 1):
            table_str += f'{f"{columns_headers[index_column_header]}": ^{len_section}}'

        table_str += f'{f"{columns_headers[-1]}": >{len_section}}\n'

    table_str += placeholder_line

    for index_column_value in range(len(columns_values[0])):
        table_str += f'{f"{columns_values[0][index_column_value]}": <{len_section}}'

        for index_column in range(1, len(columns_values) - 1):
            table_str += f'{f"{columns_values[index_column][index_column_value]}": ^{len_section + 3}}'

        table_str += f'{f"{columns_values[-1][index_column_value]}": >{len_section}}\n'
        index_column_value += 1

    table_str += placeholder_line

    return table_str


def table(part_values, f_part, table_obj, h_headers=(), v_headers=()) -> None:
    table_obj.setHorizontalHeaderLabels(h_headers)
    table_obj.setVerticalHeaderLabels(v_headers)

    for part_num, part_value in enumerate(part_values):
        f_part(part_num, part_value, table_obj)


def key_permutation_table_text(key_table):
    key = '\t'.join(key[0] for key in key_table).upper()
    one_letter_keys = ''.join(key[0] for key in key_table)
    key_indexes = '\t'.join(str_utils.get_number_letter(one_letter_keys))

    part_table = table_to_str(table_base_utils.transpose_table(list(key_table.values())))

    return f'{key}\n{key_indexes}\n{part_table}'


def affine_table_num_text(
        key_a_text: int,
        key_b_text: int
) -> Tuple[Tuple[List[str], List[str], List[str], List[str], List[str], List[str]], str]:
    column_values: Tuple[List[str], List[str], List[str], List[str], List[str], List[str]] = (
        [str(i) for i in range(11)], table_base_utils.affine_num_column(key_a_text, key_b_text, 0, 11),
        [str(i) for i in range(11, 22)], table_base_utils.affine_num_column(key_a_text, key_b_text, 11, 22),
        [str(i) for i in range(22, 33)], table_base_utils.affine_num_column(key_a_text, key_b_text, 22, 33)
    )

    return column_values, table_text(column_values, columns_headers=table_base_utils.affine_column_headers(
        key_a_text, key_b_text
    ))


def affine_table_letter_text(key_a_text: int, key_b_text: int, num_column_values):
    column_values = (
        table_base_utils.affine_letter_column(num_column_values[0]),
        table_base_utils.affine_letter_column(num_column_values[1]),
        table_base_utils.affine_letter_column(num_column_values[2]),
        table_base_utils.affine_letter_column(num_column_values[3]),
        table_base_utils.affine_letter_column(num_column_values[4]),
        table_base_utils.affine_letter_column(num_column_values[5])
    )

    return column_values, table_text(column_values, columns_headers=table_base_utils.affine_column_headers(
        key_a_text, key_b_text
    ))


def affine_table(key_a_text, key_b_text, column_values, table_obj):
    h_headers = table_base_utils.affine_column_headers(key_a_text, key_b_text)

    table(column_values, table_base_utils.table_column, table_obj, h_headers=h_headers)


def caesar_key_table_text(replace_values):
    column_headers = ('№', '->', '№', '->', '№', '->')

    column_values = (
        table_base_utils.affine_letter_column([str(i) for i in range(11)]),
        replace_values[:11],
        table_base_utils.affine_letter_column([str(i) for i in range(11, 22)]),
        replace_values[11:22],
        table_base_utils.affine_letter_column([str(i) for i in range(22, 33)]),
        replace_values[22:33]
    )

    return column_values, table_text(column_values, columns_headers=column_headers)


def caesar_key_table(column_values, table_obj):
    h_headers = ('№', '->', '№', '->', '№', '->')

    table(column_values, table_base_utils.table_column, table_obj, h_headers=h_headers)


def vigenere_table_text(msg_txt: str, key_text: str, enc_msg_txt: str) -> str:
    row_msg: List[str] = list(msg_txt)
    row_key_word: List[str] = list(str_utils.repeat_on_str(msg_txt, key_text))
    row_index_key_word: List[str] = list(str_utils.get_index(row_key_word, constants.CUT_RU_ALPHABET))
    item_utils.remove_item(' ', row_index_key_word)
    row_enc_msg: List[str] = list(enc_msg_txt)

    enc_msg_table: List[List[str], List[str], List[str], List[str]] = [
        row_msg,
        row_key_word,
        row_index_key_word,
        row_enc_msg,
    ]

    return table_to_str_size(enc_msg_table, 3, 2)


def vigenere_table(row_values, table_obj):
    h_headers = list(constants.CUT_RU_ALPHABET)
    v_headers = [str(row) for row in range(32)]

    table(row_values, table_base_utils.table_row, table_obj, h_headers, v_headers)
