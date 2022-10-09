from typing import Dict

from Assets import constants, styles

from Utils.table_base_utils import table_num_items, table_row
from Utils.table_base_utils import table

from Utils.StyleUtils.modal_dialogs import show_error_msg
from Utils.StyleUtils.style_utils import set_line_edit_border_color, set_table_color


def magic_square_generic_handler(msg_obj, rank_obj, key_table_obj, enc_msg_obj, table_obj,
                                 f_magic_square):
    try:
        msg_txt: str = msg_obj.text()
        table_rank: int = int(rank_obj.text())
        key_table = table_num_items(key_table_obj)

        colors: Dict[str, styles.Color] = styles.DEFAULT_COLORS

        tool_tips: Dict[str, str] = {
            'default': '',
            'error': 'Количество символов сообщения не соответствует размерности таблицы'
        }

        if len(msg_txt) < table_rank ** 2:
            set_line_edit_border_color(msg_obj, colors['error'])
            set_table_color(key_table_obj, colors['error'])

            msg_obj.setToolTip(tool_tips['error'])
            key_table_obj.setToolTip(tool_tips['error'])

            return

        enc_msg, enc_msg_table = f_magic_square(msg_txt, key_table)
        enc_msg_obj.setText(enc_msg)
        table(enc_msg_table, table_row, table_obj)

        set_line_edit_border_color(msg_obj, colors['default'])
        set_table_color(key_table_obj, colors['default'])

        msg_obj.setToolTip(tool_tips['default'])
        key_table_obj.setToolTip(tool_tips['default'])
    except ValueError as value_error:
        print(value_error)

        enc_msg_obj.setText(constants.ERROR_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)

        show_error_msg('Произошла ошибка в приложении', 'Ошибка')
