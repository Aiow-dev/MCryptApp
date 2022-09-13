from typing import List, Tuple, Dict

from Assets import constants

from Utils import item_utils, str_utils, table_base_utils


def table_to_str(encrypt_message_table: List[List[str]]) -> str:
    return ''.join('\t'.join(row) + '\n' for row in encrypt_message_table)


def table_to_str_size(encrypt_message_table: List[List[str]], size_h: int = 1, size_v: int = 1) -> str:
    table = ''

    for row in encrypt_message_table:
        for symbol in row:
            table += f'{f"{symbol}": <{size_h}}'

        table += '\n' * size_v

    return table


def table_dict_to_str(table_dict: Dict[str, str]) -> str:
    return ''.join(key + '\t->\t' + value + '\n-------------------------------------\n'
                   for key, value in table_dict.items())


def tables_to_str(message_table: str, encrypt_message_table: str) -> str:
    table_dict: Dict[str, str] = {
        message_table[index]: encrypt_message_table[index]
        for index in range(len(message_table))
    }

    return table_dict_to_str(table_dict)


def construct_table(columns_values: tuple, table_header: str = None, columns_headers: tuple = None,
                    placeholder: str = '-', len_table_section: int = -1) -> str:
    table = ''

    len_section = len_table_section

    if len_section == -1:
        len_section = len(max(columns_headers, key=len))

    len_table = len_section * len(columns_headers)

    placeholder_line = placeholder * len_table + '\n'

    if table_header:
        table += placeholder_line
        table += f'{f"{table_header}": ^{len_table}}\n'
        table += placeholder_line

    if columns_headers:
        table += f'{f"{columns_headers[0]}": <{len_section}}'

        for index_column_header in range(1, len(columns_headers) - 1):
            table += f'{f"{columns_headers[index_column_header]}": ^{len_section}}'

        table += f'{f"{columns_headers[-1]}": >{len_section}}\n'

    table += placeholder_line

    for index_column_value in range(len(columns_values[0])):
        table += f'{f"{columns_values[0][index_column_value]}": <{len_section}}'

        for index_column in range(1, len(columns_values) - 1):
            table += f'{f"{columns_values[index_column][index_column_value]}": ^{len_section + 3}}'

        table += f'{f"{columns_values[-1][index_column_value]}": >{len_section}}\n'
        index_column_value += 1

    table += placeholder_line

    return table


def construct_affine_table_number_text(
        key_a_text: int,
        key_b_text: int
) -> Tuple[Tuple[List[str], List[str], List[str], List[str], List[str], List[str]], str]:
    column_values: Tuple[List[str], List[str], List[str], List[str], List[str], List[str]] = (
        [str(i) for i in range(11)], table_base_utils.affine_num_column(key_a_text, key_b_text, 0, 11),
        [str(i) for i in range(11, 22)], table_base_utils.affine_num_column(key_a_text, key_b_text, 11, 22),
        [str(i) for i in range(22, 33)], table_base_utils.affine_num_column(key_a_text, key_b_text, 22, 33)
    )

    return column_values, construct_table(column_values, columns_headers=table_base_utils.affine_column_headers(
        key_a_text, key_b_text
    ))


def construct_affine_table_letter_text(key_a_text: int, key_b_text: int, number_column_values):
    column_values = (
        table_base_utils.affine_letter_column(number_column_values[0]),
        table_base_utils.affine_letter_column(number_column_values[1]),
        table_base_utils.affine_letter_column(number_column_values[2]),
        table_base_utils.affine_letter_column(number_column_values[3]),
        table_base_utils.affine_letter_column(number_column_values[4]),
        table_base_utils.affine_letter_column(number_column_values[5])
    )

    return column_values, construct_table(column_values, columns_headers=table_base_utils.affine_column_headers(
        key_a_text, key_b_text
    ))


def construct_affine_table(key_a_text, key_b_text, column_values, encryption_message_table_obj):
    encryption_message_table_obj.setHorizontalHeaderLabels(
        table_base_utils.affine_column_headers(key_a_text, key_b_text)
    )

    for number_column, column_value in enumerate(column_values):
        table_base_utils.table_column(number_column, column_value, encryption_message_table_obj)


def construct_caesar_key_table_text(replace_values):
    column_headers = ('№', '->', '№', '->', '№', '->')

    column_values = (
        table_base_utils.affine_letter_column([str(i) for i in range(11)]),
        replace_values[:11],
        table_base_utils.affine_letter_column([str(i) for i in range(11, 22)]),
        replace_values[11:22],
        table_base_utils.affine_letter_column([str(i) for i in range(22, 33)]),
        replace_values[22:33]
    )

    return column_values, construct_table(column_values, columns_headers=column_headers)


def construct_caesar_key_table(column_values, encryption_message_table_obj):
    column_headers = ('№', '->', '№', '->', '№', '->')

    encryption_message_table_obj.setHorizontalHeaderLabels(column_headers)

    for number_column, column_value in enumerate(column_values):
        table_base_utils.table_column(number_column, column_value, encryption_message_table_obj)


def construct_vigenere_table_text(msg_txt: str, key_text: str, enc_msg_txt: str) -> str:
    row_msg: List[str] = list(msg_txt)
    row_key_word: List[str] = list(str_utils.repeat_on_str(msg_txt, key_text))
    row_index_key_word: List[str] = list(str_utils.get_index(row_key_word, constants.RU_ALPHABET))
    item_utils.remove_item(' ', row_index_key_word)
    row_enc_msg: List[str] = list(enc_msg_txt)

    enc_msg_table: List[List[str], List[str], List[str], List[str]] = [
        row_msg,
        row_key_word,
        row_index_key_word,
        row_enc_msg,
    ]

    return table_to_str_size(enc_msg_table, 3, 2)


def construct_vigenere_table(row_values, enc_msg_table_obj):
    column_headers = list(constants.RU_ALPHABET)
    row_headers = [str(row) for row in range(32)]

    enc_msg_table_obj.setHorizontalHeaderLabels(column_headers)
    enc_msg_table_obj.setVerticalHeaderLabels(row_headers)

    for number_row, row_value in enumerate(row_values):
        table_base_utils.table_row(number_row, row_value, enc_msg_table_obj)
