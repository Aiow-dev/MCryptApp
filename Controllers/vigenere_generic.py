from Assets import constants

from Utils.table_utils import vigenere_table, vigenere_table_text

from Utils.StyleUtils.modal_dialogs import show_error_msg


def vigenere_generic_handler(msg_obj, key_obj, enc_msg_obj,
                             table_txt_obj, table_obj, f_vigenere_obj):
    try:
        msg_txt: str = msg_obj.text().lower()
        key_txt: str = key_obj.text().lower()

        enc_msg, enc_msg_table = f_vigenere_obj(msg_txt, key_txt)
        enc_msg_obj.setText(enc_msg)
        table_txt_obj.setText(vigenere_table_text(msg_txt, key_txt, enc_msg))
        vigenere_table(enc_msg_table, table_obj)
    except ValueError as value_error:
        print(value_error)

        enc_msg_obj.setText(constants.ERROR_MESSAGE)
        table_txt_obj.setText(constants.ERROR_TABLE_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)

        show_error_msg('Произошла ошибка в приложении')
