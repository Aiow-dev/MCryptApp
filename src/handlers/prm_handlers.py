import random

from src.components import enc_tables, dialogs, dictionary
from src.helpers import items, tables
from src.scripts.encryption import prm
from src.handlers import messages


def proc_simple_prm(form, encryption):
    try:
        msg = form['msg_input'].text()
        rows = int(form['rows_input'].text())
        columns = int(form['columns_input'].text())
        enc_data = encryption(msg, rows, columns)
        if enc_msg := enc_data.get('msg'):
            enc_tbl = tables.table_to_str(enc_data.get('enc_table'))
            form['enc_msg_input'].setText(enc_msg)
            form['enc_tbl_input'].setText(enc_tbl)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_simple_prm(form):
    proc_simple_prm(form, prm.enc_simple_prm)


def dec_proc_simple_prm(form):
    proc_simple_prm(form, prm.dec_simple_prm)


def auto_simple_prm(parent, form):
    try:
        msg = form['msg_input'].text().replace(' ', '')
        rows_text = form['rows_input'].text().replace(' ', '')
        columns_text = form['columns_input'].text().replace(' ', '')
        if rows_text or columns_text:
            result = dialogs.question_msg_result(messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        len_msg = len(msg)
        if len_msg > 0:
            if multipliers := items.get_multipliers(len_msg):
                rows, columns = items.couple_multipliers(multipliers)
                form['rows_input'].setText(str(rows))
                form['columns_input'].setText(str(columns))
            else:
                dialogs.show_err_msg(messages.MSG_PRIME_LEN_ERR, 'Ошибка')
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')


def proc_key_prm(form, encryption):
    try:
        msg = form['msg_input'].text()
        rows = int(form['rows_input'].text())
        columns = int(form['columns_input'].text())
        key = form['key_input'].text()
        enc_data = encryption(msg, rows, columns, key)
        if enc_msg := enc_data.get('msg'):
            enc_tbl = enc_tables.key_permutation_table_text(enc_data.get('enc_table'))
            form['enc_msg_input'].setText(enc_msg)
            form['enc_tbl_input'].setText(enc_tbl)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_key_prm(form):
    proc_key_prm(form, prm.enc_key_prm)


def dec_proc_key_prm(form):
    proc_key_prm(form, prm.dec_key_prm)


def auto_key_prm(parent, form):
    try:
        msg = form['msg_input'].text().replace(' ', '')
        rows_text = form['rows_input'].text().replace(' ', '')
        columns_text = form['columns_input'].text().replace(' ', '')
        key_text = form['key_input'].text().replace(' ', '')
        if any([rows_text, columns_text, key_text]):
            result = dialogs.question_msg_result(messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        len_msg = len(msg)
        if len_msg > 0:
            if multipliers := items.get_multipliers(len_msg):
                rows, columns = items.couple_multipliers(multipliers)
                if key_words := dictionary.animals.get(columns):
                    key = random.choice(key_words)
                    form['rows_input'].setText(str(rows))
                    form['columns_input'].setText(str(columns))
                    form['key_input'].setText(key)
                else:
                    dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')
            else:
                dialogs.show_err_msg(messages.MSG_PRIME_LEN_ERR, 'Ошибка')
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')


def proc_double_prm(form, encryption):
    try:
        msg = form['msg_input'].text()
        rows = int(form['rows_input'].text())
        columns = int(form['columns_input'].text())
        key_row = form['key_row_input'].text()
        key_column = form['key_column_input'].text()
        if not items.is_all_range(key_row, range(1, rows + 1)):
            err_msg = messages.KEY_ROW_RANGE_ERR
            dialogs.show_err_msg(err_msg, 'Ошибка')
            return
        if not items.is_all_range(key_column, range(1, columns + 1)):
            err_msg = messages.KEY_CLM_RANGE_ERR
            dialogs.show_err_msg(err_msg, 'Ошибка')
            return
        enc_data = encryption(msg, rows, columns, key_row, key_column)
        if enc_msg := enc_data.get('msg'):
            enc_tbl = enc_tables.double_permutation_table_text(enc_data.get('enc_table'), key_row, key_column)
            form['enc_msg_input'].setText(enc_msg)
            form['enc_tbl_input'].setText(enc_tbl)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_double_prm(form):
    proc_double_prm(form, prm.enc_double_prm)


def dec_proc_double_prm(form):
    proc_double_prm(form, prm.dec_double_prm)


def auto_double_prm(parent, form):
    try:
        msg = form['msg_input'].text().replace(' ', '')
        rows_text = form['rows_input'].text().replace(' ', '')
        columns_text = form['columns_input'].text().replace(' ', '')
        key_row_text = form['key_row_input'].text().replace(' ', '')
        key_column_text = form['key_column_input'].text().replace(' ', '')
        if any([rows_text, columns_text, key_row_text, key_column_text]):
            result = dialogs.question_msg_result(messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        len_msg = len(msg)
        if len_msg > 0:
            if multipliers := items.get_multipliers(len_msg):
                rows, columns = items.couple_multipliers(multipliers)
                row_range = list(range(1, rows + 1))
                random.shuffle(row_range)
                key_row = ''.join(str(number) for number in row_range)
                column_range = list(range(1, columns + 1))
                random.shuffle(column_range)
                key_column = ''.join(str(number) for number in column_range)
                form['rows_input'].setText(str(rows))
                form['columns_input'].setText(str(columns))
                form['key_row_input'].setText(key_row)
                form['key_column_input'].setText(key_column)
            else:
                dialogs.show_err_msg(messages.MSG_PRIME_LEN_ERR, 'Ошибка')
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')
