from src.components import dialogs, chars
from src.helpers import tables
from src.scripts.encryption import double_playfair


def proc_double_playfair(form, encryption):
    try:
        msg = form['msg_input'].text()
        rows = int(form['rows_input'].text())
        columns = int(form['columns_input'].text())
        num = len(chars.EXT_RU_ALPHABET)
        if rows * columns > num:
            dialogs.show_err_msg(f'Размерности таблиц превышают количество допустимых символов({num})!', 'Ошибка!')
            return
        left_tbl = tables.table_up_items(form['left_tbl_widget'])
        right_tbl = tables.table_up_items(form['right_tbl_widget'])
        enc_data = encryption(msg, left_tbl, right_tbl)
        enc_msg = enc_data.get('msg')
        if enc_msg == '':
            dialogs.show_err_msg('Параметры шифрования не заполнены!', 'Ошибка!')
            return
        if enc_msg:
            form['enc_msg_input'].setText(enc_msg)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_double_playfair(form):
    proc_double_playfair(form, double_playfair.enc_double_playfair)


def dec_proc_double_playfair(form):
    proc_double_playfair(form, double_playfair.dec_double_playfair)
