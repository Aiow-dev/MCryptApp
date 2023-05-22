from src.components import dialogs, chars
from src.helpers import tables
from src.scripts.encryption import double_playfair


def proc_double_playfair(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        rows = int(form_data['rows_input'].text())
        columns = int(form_data['columns_input'].text())
        num = len(chars.EXT_RU_ALPHABET)
        if rows * columns > num:
            dialogs.show_err_msg(f'Размерности таблиц превышают количество допустимых символов({num})!', 'Ошибка!')
            return
        left_tbl = tables.table_up_items(form_data['left_tbl_widget'])
        right_tbl = tables.table_up_items(form_data['right_tbl_widget'])
        enc_data = encryption(msg, left_tbl, right_tbl)
        enc_msg = enc_data.get('msg')
        if enc_msg == '':
            dialogs.show_err_msg('Параметры шифрования не заполнены!', 'Ошибка!')
            return
        if enc_msg:
            form_data['enc_msg_input'].setText(enc_msg)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_double_playfair(form_data):
    proc_double_playfair(form_data, double_playfair.enc_double_playfair)


def dec_proc_double_playfair(form_data):
    proc_double_playfair(form_data, double_playfair.dec_double_playfair)
