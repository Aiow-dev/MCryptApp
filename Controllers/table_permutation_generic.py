from typing import Dict

from Assets import styles, constants

from Utils import table_utils, controllers_utils, item_utils


def table_permutation_generic_handler(msg_obj, row_obj, clm_obj, enc_msg_obj,
                                      table_obj, f_permutation_obj):
    try:
        msg_txt: str = msg_obj.text()
        num_row: int = int(row_obj.text())
        num_column: int = int(clm_obj.text())

        check_ui_obj_list = [msg_obj, row_obj, clm_obj]

        colors: Dict[str, styles.Color] = styles.DEFAULT_COLORS

        tool_tips: Dict[str, str] = {
            'default': '',
            'error': 'Количество символов сообщения не соответствует произведению количества строк и столбцов'
        }

        if num_row * num_column != len(msg_txt.replace(' ', '')):
            controllers_utils.multi_set_status_handler(
                check_ui_obj_list, colors, tool_tips, True
            )

            return

        enc_msg, enc_msg_table = f_permutation_obj(msg_txt, num_row, num_column)
        enc_msg_obj.setText(enc_msg)
        table_obj.setText(table_utils.table_to_str(enc_msg_table))

        controllers_utils.multi_set_status_handler(
            check_ui_obj_list, colors, tool_tips, False
        )
    except ValueError as value_error:
        print(value_error)

        enc_msg_obj.setText(constants.ERROR_MESSAGE)
        table_obj.setText(constants.ERROR_TABLE_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)


def table_key_permutation_generic_handler(msg_obj, row_obj, clm_obj, key_obj,
                                          enc_msg_obj, table_obj, f_permutation_obj):
    try:
        msg_txt: str = msg_obj.text()
        num_row: int = int(row_obj.text())
        num_column: int = int(clm_obj.text())
        key_txt: str = key_obj.text()

        colors: Dict[str, styles.Color] = styles.DEFAULT_COLORS

        tool_tips: Dict[str, str] = {
            'default': '',
            'error': 'Количество символов сообщения не соответствует произведению количества строк и столбцов'
        }

        if num_row * num_column != len(msg_txt.replace(' ', '')):
            controllers_utils.multi_set_status_handler(
                [msg_obj, row_obj, clm_obj], colors, tool_tips, True
            )

            return

        if num_column != len(key_txt.replace(' ', '')):
            tool_tips['error'] = 'Количество символов ключа не соответствует количеству столбцов'

            controllers_utils.multi_set_status_handler(
                [clm_obj, key_obj], colors, tool_tips, True
            )

            return

        enc_msg, enc_msg_table = f_permutation_obj(msg_txt, num_row, num_column, key_txt)
        enc_msg_obj.setText(enc_msg)
        table_obj.setText(table_utils.key_permutation_table_text(enc_msg_table))

        controllers_utils.multi_set_status_handler(
            [msg_obj, row_obj, clm_obj, key_obj], colors, tool_tips, False
        )
    except ValueError as value_error:
        print(value_error)

        enc_msg_obj.setText('Ошибка. Проверьте корректность введенных данных!')
    except AttributeError as attribute_error:
        print(attribute_error)


def double_permutation_generic(msg_obj, row_obj, clm_obj, key_row_obj,
                               key_clm_obj, enc_msg_obj, table_obj, f_permutation_obj):
    try:
        msg_txt: str = msg_obj.text()
        num_row: int = int(row_obj.text())
        num_column: int = int(clm_obj.text())
        key_row: str = key_row_obj.text()
        key_clm: str = key_clm_obj.text()

        colors: Dict[str, styles.Color] = styles.DEFAULT_COLORS

        tool_tips: Dict[str, str] = {
            'default': '',
            'error': 'Количество символов сообщения не соответствует произведению количества строк и столбцов'
        }

        if num_row * num_column != len(msg_txt.replace(' ', '')):
            controllers_utils.multi_set_status_handler(
                [msg_obj, row_obj, clm_obj], colors, tool_tips, True
            )

            return

        if not item_utils.is_all_range(key_row, range(1, num_row + 1)):
            tool_tips['error'] = 'Количество символов или содержимое ключа строк не совпадает с количеством строк'

            controllers_utils.multi_set_status_handler(
                [row_obj, key_row_obj], colors, tool_tips, True
            )

            return

        if not item_utils.is_all_range(key_clm, range(1, num_column + 1)):
            tool_tips['error'] = 'Количество символов или содержимое ключа столбцов не совпадает с количеством столбцов'

            controllers_utils.multi_set_status_handler(
                [clm_obj, key_clm_obj], colors, tool_tips, True
            )

            return

        enc_msg, enc_msg_table = f_permutation_obj(msg_txt, num_row, num_column, key_row, key_clm)
        enc_msg_obj.setText(enc_msg)
        table_obj.setText(table_utils.double_permutation_table_text(enc_msg_table, key_row, key_clm))

        controllers_utils.multi_set_status_handler(
            [msg_obj, row_obj, clm_obj, key_row_obj, key_clm_obj], colors, tool_tips, False
        )
    except ValueError as value_error:
        print(value_error)

        enc_msg_obj.setText(constants.ERROR_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)
