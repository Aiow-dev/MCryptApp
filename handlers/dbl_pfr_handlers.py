from components import dialogs
from helpers import tables
from scripts.encryption import double_playfair


def proc_double_playfair(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        left_tbl = tables.table_up_items(form_data['left_tbl_widget'])
        right_tbl = tables.table_up_items(form_data['right_tbl_widget'])
        enc_data = encryption(msg, left_tbl, right_tbl)
        if enc_msg := enc_data.get('msg'):
            form_data['enc_msg_input'].setText(enc_msg)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!')


def enc_proc_double_playfair(form_data):
    proc_double_playfair(form_data, double_playfair.enc_double_playfair)


def dec_proc_double_playfair(form_data):
    proc_double_playfair(form_data, double_playfair.dec_double_playfair)
