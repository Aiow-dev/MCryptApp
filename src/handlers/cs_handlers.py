import random

from src.components import enc_tables, dialogs, chars, dictionary
from src.helpers import tables
from src.scripts.encryption import cs
from . import messages


def proc_classic_cs(form, encryption):
    try:
        msg = form['msg_input'].text()
        key = int(form['key_input'].text())
        alphabet = chars.RU_ALPHABET
        enc_data = encryption(msg, key, alphabet)
        if enc_msg := enc_data.get('msg'):
            enc_tbl = tables.tables_to_str(enc_data.get('table'), enc_data.get('enc_table'))
            form['enc_msg_input'].setText(enc_msg)
            form['enc_tbl_input'].setText(enc_tbl)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_classic_cs(form):
    proc_classic_cs(form, cs.enc_classic_cs)


def dec_proc_classic_cs(form):
    proc_classic_cs(form, cs.dec_classic_cs)


def auto_classic_cs(form):
    try:
        msg = form['msg_input'].text().replace(' ', '')
        if form['key_input'].text():
            result = dialogs.question_msg_result(messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        if msg:
            key = random.randint(1, len(chars.RU_ALPHABET))
            form['key_input'].setText(str(key))
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')


def proc_affine_cs(form, encryption):
    try:
        msg = form['msg_input'].text()
        key_a = int(form['key_a_input'].text())
        key_b = int(form['key_b_input'].text())
        alphabet = chars.RU_ALPHABET
        enc_data = encryption(msg, key_a, key_b, alphabet)
        if enc_msg := enc_data.get('msg'):
            nums_column, num_tbl = enc_tables.affine_table_num_text(key_a, key_b)
            letters_column, letters_tbl = enc_tables.affine_table_letter_text(key_a, key_b, nums_column, alphabet)
            form['enc_msg_input'].setText(enc_msg)
            enc_tables.affine_table(key_a, key_b, nums_column, form['enc_tbl_num_widget'])
            enc_tables.affine_table(key_a, key_b, letters_column, form['enc_tbl_letter_widget'])
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_affine_cs(form):
    proc_affine_cs(form, cs.enc_affine_cs)


def dec_proc_affine_cs(form):
    proc_affine_cs(form, cs.dec_affine_cs)


def auto_affine_cs(form):
    try:
        msg = form['msg_input'].text().replace(' ', '')
        key_a_text = form['key_a_input'].text().replace(' ', '')
        key_b_text = form['key_b_input'].text().replace(' ', '')
        if key_a_text or key_b_text:
            result = dialogs.question_msg_result(messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        if msg:
            a_keys = [a for a in range(1, 99) if a % 3 != 0 and a % 11 != 0]
            key_a = random.choice(a_keys)
            key_b = random.randint(-100, 100)
            form['key_a_input'].setText(str(key_a))
            form['key_b_input'].setText(str(key_b))
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')


def proc_key_cs(form, encryption):
    try:
        msg = form['msg_input'].text()
        key = form['key_input'].text()
        key_k = int(form['key_k_input'].text())
        alphabet = chars.RU_ALPHABET
        enc_data = encryption(msg, key_k, key, alphabet)
        if enc_msg := enc_data.get('msg'):
            letters_column, enc_tbl = enc_tables.caesar_key_table_text(enc_data.get('enc_table'), alphabet)
            form['enc_msg_input'].setText(enc_msg)
            form['enc_tbl_input'].setText(enc_tbl)
            enc_tables.caesar_key_table(letters_column, form['enc_tbl_widget'])
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_key_cs(form):
    proc_key_cs(form, cs.enc_key_cs)


def dec_proc_key_cs(form):
    proc_key_cs(form, cs.dec_key_cs)


def auto_key_cs(form):
    try:
        msg = form['msg_input'].text().replace(' ', '')
        key_text = form['key_input'].text().replace(' ', '')
        key_k_text = form['key_k_input'].text().replace(' ', '')
        if key_text or key_k_text:
            result = dialogs.question_msg_result(messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        if msg:
            key_index = random.randint(2, len(dictionary.animals))
            key = random.choice(dictionary.animals[key_index])
            key_k = random.randint(1, 32)
            form['key_input'].setText(str(key))
            form['key_k_input'].setText(str(key_k))
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')
