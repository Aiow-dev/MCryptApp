from helpers import tables
from components import enc_tables, dialogs
from scripts.encryption import ms


def proc_ms(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        tbl_rank = int(form_data['rank_input'].text())
        key_tbl = tables.table_num_items(form_data['key_tbl_widget'])
        enc_data = encryption(msg, key_tbl)
        if enc_msg := enc_data.get('msg'):
            form_data['enc_msg_input'].setText(enc_msg)
            tables.table(enc_data.get('enc_table'), enc_tables.table_row, form_data['enc_tbl_widget'])
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!')


def enc_proc_ms(form_data):
    proc_ms(form_data, ms.enc_magic_square)


def dec_proc_ms(form_data):
    proc_ms(form_data, ms.dec_magic_square)
