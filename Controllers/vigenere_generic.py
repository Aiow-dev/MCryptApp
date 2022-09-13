from Assets import constants

from Utils import table_utils

from Utils.StyleUtils import modal_dialogs


def vigenere_generic_handler(msg_obj, key_obj, enc_msg_obj,
                             table_txt_obj, table_obj, f_vigenere_obj):
    try:
        msg_txt: str = msg_obj.text().lower()
        key_text: str = key_obj.text().lower()

        enc_msg, enc_msg_table = f_vigenere_obj(msg_txt, key_text)
        enc_msg_obj.setText(enc_msg)
        table_txt_obj.setText(table_utils.construct_vigenere_table_text(msg_txt, key_text, enc_msg))
        table_utils.construct_vigenere_table(enc_msg_table, table_obj)
    except ValueError as value_error:
        print(value_error)

        enc_msg_obj.setText(constants.ERROR_MESSAGE)
        table_txt_obj.setText(constants.ERROR_TABLE_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)

        modal_dialogs.show_error_message('Произошла ошибка в приложении')
