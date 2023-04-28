from components import dialogs, enc_tables
from helpers import tables
from scripts.encryption import prm


def proc_simple_prm(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        rows = int(form_data['rows_input'].text())
        columns = int(form_data['columns_input'].text())
        enc_data = encryption(msg, rows, columns)
        if enc_msg := enc_data.get('msg'):
            enc_tbl = tables.table_to_str(enc_data.get('enc_table'))
            form_data['enc_msg_input'].setText(enc_msg)
            form_data['enc_tbl_input'].setText(enc_tbl)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!')


def enc_proc_simple_prm(form_data):
    proc_simple_prm(form_data, prm.enc_simple_prm)


def dec_proc_simple_prm(form_data):
    proc_simple_prm(form_data, prm.dec_simple_prm)


def proc_key_prm(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        rows = int(form_data['rows_input'].text())
        columns = int(form_data['columns_input'].text())
        key = form_data['key_input'].text()
        enc_data = encryption(msg, rows, columns, key)
        if enc_msg := enc_data.get('msg'):
            enc_tbl = enc_tables.key_permutation_table_text(enc_data.get('enc_table'))
            form_data['enc_msg_input'].setText(enc_msg)
            form_data['enc_tbl_input'].setText(enc_tbl)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!')


def enc_proc_key_prm(form_data):
    proc_key_prm(form_data, prm.enc_key_prm)


def dec_proc_key_prm(form_data):
    proc_key_prm(form_data, prm.dec_key_prm)


def proc_double_prm(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        rows = int(form_data['rows_input'].text())
        columns = int(form_data['columns_input'].text())
        key_row = form_data['key_row_input'].text()
        key_column = form_data['key_column_input'].text()
        enc_data = encryption(msg, rows, columns, key_row, key_column)
        if enc_msg := enc_data.get('msg'):
            enc_tbl = enc_tables.double_permutation_table_text(enc_data.get('enc_table'), key_row, key_column)
            form_data['enc_msg_input'].setText(enc_msg)
            form_data['enc_tbl_input'].setText(enc_tbl)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!')


def enc_proc_double_prm(form_data):
    proc_double_prm(form_data, prm.enc_double_prm)


def dec_proc_double_prm(form_data):
    proc_double_prm(form_data, prm.dec_double_prm)
