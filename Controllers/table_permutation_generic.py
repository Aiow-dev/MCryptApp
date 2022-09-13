from typing import Dict

from Assets import styles, constants

from Utils import table_utils, controllers_utils


def table_permutation_generic_handler(message_obj, row_obj, column_obj, encrypt_message_obj,
                                      encryption_message_table_obj, function_permutation_obj):
    try:
        message_text: str = message_obj.text()
        number_row: int = int(row_obj.text())
        number_column: int = int(column_obj.text())

        check_ui_obj_list = [message_obj, row_obj, column_obj]

        colors: Dict[str, styles.Color] = {
            'default': styles.Color.dark_charcoal,
            'error': styles.Color.orange_red
        }

        tool_tips: Dict[str, str] = {
            'default': '',
            'error': 'Количество символов сообщения не соответствует произведению количества строк и столбцов'
        }

        if number_row * number_column != len(message_text.replace(' ', '')):
            controllers_utils.multi_set_status_handler(
                check_ui_obj_list, colors, tool_tips, True
            )

            return

        encrypt_message, encrypt_message_table = function_permutation_obj(message_text, number_row,
                                                                          number_column)
        encrypt_message_obj.setText(encrypt_message)
        encryption_message_table_obj.setText(table_utils.table_to_str(encrypt_message_table))

        controllers_utils.multi_set_status_handler(
            check_ui_obj_list, colors, tool_tips, False
        )
    except ValueError as value_error:
        print(value_error)

        encrypt_message_obj.setText(constants.ERROR_MESSAGE)
        encryption_message_table_obj.setText(constants.ERROR_TABLE_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)


def table_key_permutation_generic_handler(message_obj, row_obj, column_obj, key_obj,
                                          encrypt_message_obj, function_permutation_obj):
    try:
        message_text: str = message_obj.text()
        number_row: int = int(row_obj.text())
        number_column: int = int(column_obj.text())
        key_text: str = key_obj.text()

        colors: Dict[str, styles.Color] = {
            'default': styles.Color.dark_charcoal, 'error': styles.Color.orange_red
        }

        tool_tips: Dict[str, str] = {
            'default': '',
            'error': 'Количество символов сообщения не соответствует произведению количества строк и столбцов'
        }

        if number_row * number_column != len(message_text.replace(' ', '')):
            controllers_utils.multi_set_status_handler(
                [message_obj, row_obj, column_obj], colors, tool_tips, True
            )

            return

        if number_column != len(key_text.replace(' ', '')):
            tool_tips['error'] = 'Количество символов ключа не соответствует количеству столбцов'

            controllers_utils.multi_set_status_handler(
                [column_obj, key_obj], colors, tool_tips, True
            )

            return

        encrypt_message = function_permutation_obj(message_text, number_row,
                                                   number_column, key_text)
        encrypt_message_obj.setText(encrypt_message)

        controllers_utils.multi_set_status_handler(
            [message_obj, row_obj, column_obj, key_obj], colors, tool_tips, False
        )
    except ValueError as value_error:
        print(value_error)

        encrypt_message_obj.setText('Ошибка. Проверьте корректность введенных данных!')
    except AttributeError as attribute_error:
        print(attribute_error)
