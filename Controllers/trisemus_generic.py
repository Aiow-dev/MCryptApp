from Utils import table_utils

from Assets import constants


def trisemus_generic_handler(msg_obj, row_obj, clm_obj, key_obj,
                             enc_msg_obj, table_txt_obj, f_trisemus_obj):
    try:
        msg_txt: str = msg_obj.text()
        num_row: int = int(row_obj.text())
        num_column: int = int(clm_obj.text())
        key_txt: str = key_obj.text().lower()

        enc_msg, enc_msg_table = f_trisemus_obj(msg_txt, key_txt, num_row, num_column)
        enc_msg_obj.setText(enc_msg)
        table_txt_obj.setText(table_utils.table_to_str(enc_msg_table))
    except ValueError as value_error:
        print(value_error)

        enc_msg_obj.setText(constants.ERROR_MESSAGE)
        table_txt_obj.setText(constants.ERROR_TABLE_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)
