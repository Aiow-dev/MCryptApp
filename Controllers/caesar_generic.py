from typing import Dict

from math import gcd

from Assets import styles, constants

from Utils import table_utils, controllers_utils


def caesar_classic_generic_handler(msg_obj, key_obj, enc_msg_obj, table_obj, f_caesar_obj):
    try:
        msg_txt: str = msg_obj.text()
        key_txt: int = int(key_obj.text())

        check_ui_obj_list = [msg_obj, key_obj]

        colors: Dict[str, styles.Color] = styles.DEFAULT_COLORS

        tool_tips: Dict[str, str] = {
            'default': '',
            'error': 'Значение ключа шифрования должно быть меньше 33 (количество букв алфавита)'
        }

        offset: int = constants.NUM_LETTER - 1

        if key_txt > offset:
            controllers_utils.multi_set_status_handler(
                check_ui_obj_list, colors, tool_tips, True
            )

            return

        enc_msg, msg_table, enc_msg_table = f_caesar_obj(msg_txt, key_txt)
        enc_msg_obj.setText(enc_msg)
        table_obj.setText(table_utils.tables_to_str(msg_table, enc_msg_table))

        controllers_utils.multi_set_status_handler(
            check_ui_obj_list, colors, tool_tips, False
        )
    except ValueError as value_error:
        print(value_error)

        enc_msg_obj.setText(constants.ERROR_MESSAGE)
        table_obj.setText(constants.ERROR_TABLE_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)


def caesar_affine_generic_handler(msg_obj, key_a_obj, key_b_obj, enc_msg_obj,
                                  table_num_obj, table_letter_obj, f_caesar_obj):
    try:
        msg_txt: str = msg_obj.text()
        key_a_text: int = int(key_a_obj.text())
        key_b_text: int = int(key_b_obj.text())

        colors: Dict[str, styles.Color] = styles.DEFAULT_COLORS

        tool_tips: Dict[str, str] = {
            'default': '',
            'error': 'Значение ключа a не может быть меньше значения ключа b'
        }

        if key_a_text < key_b_text:
            controllers_utils.multi_set_status_handler(
                [key_a_obj, key_b_obj], colors, tool_tips, True
            )

            return

        if gcd(key_a_text, constants.NUM_LETTER) != 1:
            tool_tips['error'] = 'Количество букв алфавита (33) и значение ключа a не являются взаимно простыми числами'

            controllers_utils.multi_set_status_handler(
                [msg_obj, key_a_obj], colors, tool_tips, True
            )

            return

        enc_msg, msg_table, enc_msg_table = f_caesar_obj(msg_txt, key_a_text, key_b_text)
        enc_msg_obj.setText(enc_msg)

        num_column_values, affine_table_num = table_utils.affine_table_num_text(
            key_a_text, key_b_text
        )

        letter_column_values, affine_table_letter = table_utils.affine_table_letter_text(
            key_a_text, key_b_text, num_column_values
        )

        table_utils.affine_table(key_a_text, key_b_text, num_column_values, table_num_obj)

        table_utils.affine_table(key_a_text, key_b_text, letter_column_values, table_letter_obj)

        controllers_utils.multi_set_status_handler(
            [msg_obj, key_a_obj, key_b_obj], colors, tool_tips, False
        )
    except ValueError:
        enc_msg_obj.setText(constants.ERROR_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)


def caesar_key_generic_handler(msg_obj, key_word_obj, key_k_obj, enc_msg_obj,
                               table_txt_obj, table_obj, f_caesar_obj):
    try:
        msg_txt: str = msg_obj.text()
        key_word_txt: str = key_word_obj.text().lower()
        key_k_txt: int = int(key_k_obj.text())

        check_ui_obj_list = [msg_obj, key_k_obj]

        colors: Dict[str, styles.Color] = styles.DEFAULT_COLORS

        tool_tips: Dict[str, str] = {
            'default': '',
            'error': 'Значение ключа k должно быть меньше 33 (количество букв алфавита)'
        }

        offset = constants.NUM_LETTER - 1

        if key_k_txt > offset:
            controllers_utils.multi_set_status_handler(
                check_ui_obj_list, colors, tool_tips, True
            )

            return

        enc_msg, enc_msg_table = f_caesar_obj(msg_txt, key_k_txt, key_word_txt)
        enc_msg_obj.setText(enc_msg)

        letter_column_values, caesar_key_table = table_utils.caesar_key_table_text(enc_msg_table)

        table_txt_obj.setText(caesar_key_table)

        table_utils.caesar_key_table(letter_column_values, table_obj)

        controllers_utils.multi_set_status_handler(
            check_ui_obj_list, colors, tool_tips, False
        )
    except ValueError as value_error:
        print(value_error)

        enc_msg_obj.setText(constants.ERROR_MESSAGE)
        table_txt_obj.setText(constants.ERROR_TABLE_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)
