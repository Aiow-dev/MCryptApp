from Core.Helpers import table_helpers


def trisemus_generic_handler(msg_obj, row_obj, clm_obj, key_obj,
                             enc_msg_obj, table_txt_obj, f_trisemus_obj):
    try:
        msg_txt: str = msg_obj.text()
        number_row: int = int(row_obj.text())
        number_column: int = int(clm_obj.text())
        key_text = key_obj.text()

        enc_msg, enc_msg_table = f_trisemus_obj(msg_txt, key_text, number_row, number_column)
        enc_msg_obj.setText(enc_msg)
        table_txt_obj.setText(table_helpers.table_to_str(enc_msg_table))
    except ValueError as value_error:
        print(value_error)

        msg_obj.setText('Ошибка. Проверьте корректность введенных данных!')
        table_txt_obj.setText(
            'Ошибка. Невозможно построить таблицу. Проверьте корректность введенных данных!'
        )
    except AttributeError as attribute_error:
        print(attribute_error)
