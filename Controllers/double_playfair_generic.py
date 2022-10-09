from Assets import constants

from Utils.table_base_utils import table_up_items

from Utils.StyleUtils.modal_dialogs import show_error_msg


def double_playfair_generic_handler(msg_obj, left_tbl_obj, right_tbl_obj, enc_msg_obj,
                                    f_double_playfair):
    try:
        msg_txt: str = msg_obj.text().upper()

        left_tbl = table_up_items(left_tbl_obj)
        right_tbl = table_up_items(right_tbl_obj)

        enc_msg = f_double_playfair(msg_txt, left_tbl, right_tbl)
        enc_msg_obj.setText(enc_msg)
    except ValueError as value_error:
        print(value_error)

        enc_msg_obj.setText(constants.ERROR_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)

        show_error_msg('Произошла ошибка в приложении', 'Ошибка')
