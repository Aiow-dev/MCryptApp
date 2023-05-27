import random

from src.components import dialogs, chars, enc_tables
from src.helpers import tables, items
from src.scripts.encryption import double_playfair
from . import messages


def proc_double_playfair(form, encryption):
    try:
        msg = form['msg_input'].text()
        left_tbl = tables.table_up_items(form['left_tbl_widget'])
        right_tbl = tables.table_up_items(form['right_tbl_widget'])
        enc_data = encryption(msg, left_tbl, right_tbl, chars.EXT_RU_ALPHABET)
        enc_msg = enc_data.get('msg')
        if enc_msg == '':
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка!')
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


def auto_double_playfair(parent, form):
    try:
        msg = form['msg_input'].text().replace(' ', '')
        if not items.is_empty_table(form['left_tbl_widget']):
            result = dialogs.question_msg_result(messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        if msg:
            form['left_tbl_widget'].clear()
            form['right_tbl_widget'].clear()
            random_size = random.choice([(5, 7), (7, 5)])
            rows, columns = random_size[0], random_size[1]
            form['rows_input'].setText(str(rows))
            form['columns_input'].setText(str(columns))
            alphabet = chars.EXT_RU_ALPHABET
            enc_tables.table_rand(form['left_tbl_widget'], alphabet)
            enc_tables.table_rand(form['right_tbl_widget'], alphabet)
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')
