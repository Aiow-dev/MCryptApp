from Assets import constants

from Utils.table_base_utils import table_num_items, table_row
from Utils.table_utils import table


def magic_square_generic_handler(msg_obj, key_table_obj, enc_msg_obj, table_obj,
                                 f_magic_square):
    try:
        msg_txt: str = msg_obj.text()
        key_table = table_num_items(key_table_obj)

        enc_msg, enc_msg_table = f_magic_square(msg_txt, key_table)
        enc_msg_obj.setText(enc_msg)
        table(enc_msg_table, table_row, table_obj)
    except ValueError as value_error:
        print(value_error)

        enc_msg_obj.setText(constants.ERROR_MESSAGE)
    except AttributeError as attribute_error:
        print(attribute_error)
