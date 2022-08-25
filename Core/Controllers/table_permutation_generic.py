from typing import Dict

from Core.Helpers import table_helpers
from Core.Helpers.HelpersUI import styles

from Core.Controllers import controllers_utilities


def table_permutation_generic_handler(message_obj, row_obj, column_obj, encrypt_message_obj,
                                      encryption_message_table_obj, function_permutation_obj):
    try:
        message_text: str = message_obj.text()
        number_row: int = int(row_obj.text())
        number_column: int = int(column_obj.text())

        error_status: bool = True

        if number_row * number_column == len(message_text.replace(' ', '')):
            error_status = False

            encrypt_message, encrypt_message_table = function_permutation_obj(message_text, number_row,
                                                                              number_column)
            encrypt_message_obj.setText(encrypt_message)
            encryption_message_table_obj.setText(table_helpers.table_to_str(encrypt_message_table))

        colors: Dict[str, styles.Color] = {'default': styles.Color.dark_charcoal, 'error': styles.Color.orange_red}
        tool_tips: Dict[str, str] = {
            'default': '',
            'error': 'Количество букв в сообщении не соответствует произведению количества строк и столбцов'
        }

        controllers_utilities.multi_set_status_handler(
            [message_obj, row_obj, column_obj], colors, tool_tips, error_status
        )
    except ValueError as value_error:
        print(value_error)

        encrypt_message_obj.setText('Ошибка. Проверьте корректность введенных данных!')
        encryption_message_table_obj.setText(
            'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
        )
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
            controllers_utilities.multi_set_status_handler(
                [message_obj, row_obj, column_obj], colors, tool_tips, True
            )

            return

        if number_column != len(key_text.replace(' ', '')):
            tool_tips['error'] = 'Количество символов ключа не соответствует количеству столбцов'

            controllers_utilities.multi_set_status_handler(
                [column_obj, key_obj], colors, tool_tips, True
            )

            return

        encrypt_message = function_permutation_obj(message_text, number_row,
                                                   number_column, key_text)
        encrypt_message_obj.setText(encrypt_message)

        controllers_utilities.multi_set_status_handler(
            [message_obj, row_obj, column_obj, key_obj], colors, tool_tips, False
        )
    except ValueError as value_error:
        print(value_error)

        encrypt_message_obj.setText('Ошибка. Проверьте корректность введенных данных!')
    except AttributeError as attribute_error:
        print(attribute_error)
