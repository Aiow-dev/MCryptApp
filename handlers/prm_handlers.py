import random

from components import dialogs, enc_tables, dictionary
from helpers import tables, items, text
from scripts.encryption import prm
from handlers import messages


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
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_simple_prm(form_data):
    proc_simple_prm(form_data, prm.enc_simple_prm)


def dec_proc_simple_prm(form_data):
    proc_simple_prm(form_data, prm.dec_simple_prm)


def auto_simple_prm(parent, form_data):
    try:
        msg = form_data['msg_input'].text().replace(' ', '')
        rows_text = form_data['rows_input'].text().replace(' ', '')
        columns_text = form_data['columns_input'].text().replace(' ', '')
        if len(rows_text) > 0 or len(columns_text) > 0:
            result = dialogs.question_msg(parent, messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        len_msg = len(msg)
        if len_msg > 0:
            multipliers = items.get_multipliers(len_msg)
            if multipliers:
                rows, columns = items.couple_multipliers(multipliers)
                form_data['rows_input'].setText(str(rows))
                form_data['columns_input'].setText(str(columns))
            else:
                dialogs.show_err_msg(messages.MSG_PRIME_LEN, 'Ошибка')
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')


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
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_key_prm(form_data):
    proc_key_prm(form_data, prm.enc_key_prm)


def dec_proc_key_prm(form_data):
    proc_key_prm(form_data, prm.dec_key_prm)


def auto_key_prm(parent, form_data):
    try:
        msg = form_data['msg_input'].text().replace(' ', '')
        rows_text = form_data['rows_input'].text().replace(' ', '')
        columns_text = form_data['columns_input'].text().replace(' ', '')
        key_text = form_data['key_input'].text().replace(' ', '')
        if len(rows_text) > 0 or len(columns_text) > 0 or len(key_text) > 0:
            result = dialogs.question_msg(parent, messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        len_msg = len(msg)
        if len_msg > 0:
            multipliers = items.get_multipliers(len_msg)
            if multipliers:
                rows, columns = items.couple_multipliers(multipliers)
                key_words = text.get_words_len(dictionary.animals, columns)
                key = random.choice(key_words)
                form_data['rows_input'].setText(str(rows))
                form_data['columns_input'].setText(str(columns))
                form_data['key_input'].setText(key)
            else:
                dialogs.show_err_msg(messages.MSG_PRIME_LEN, 'Ошибка')
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')


def proc_double_prm(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        rows = int(form_data['rows_input'].text())
        columns = int(form_data['columns_input'].text())
        key_row = form_data['key_row_input'].text()
        key_column = form_data['key_column_input'].text()
        if not items.is_all_range(key_row, range(1, rows + 1)):
            err_msg = messages.KEY_ROW_RANGE_ERROR
            dialogs.show_err_msg(err_msg, 'Ошибка')
            return
        if not items.is_all_range(key_column, range(1, columns + 1)):
            err_msg = messages.KEY_CLM_RANGE_ERROR
            dialogs.show_err_msg(err_msg, 'Ошибка')
            return
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
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_double_prm(form_data):
    proc_double_prm(form_data, prm.enc_double_prm)


def dec_proc_double_prm(form_data):
    proc_double_prm(form_data, prm.dec_double_prm)
