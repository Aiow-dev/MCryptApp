import random

from src.helpers import tables, items
from src.components import enc_tables, dialogs, chars, dictionary
from src.scripts.encryption import systems
from . import messages


def proc_playfair(form, encryption):
    try:
        msg = form['msg_input'].text().replace(' ', '').lower()
        if len(msg) % 2 == 1:
            msg += 'ъ'

        rows = int(form['rows_input'].text())
        columns = int(form['columns_input'].text())
        key = form['key_input'].text().replace(' ', '').lower()
        alphabet = chars.CUT_RU_ALPHABET
        enc_data = encryption(msg, key, alphabet, rows, columns)

        if enc_msg := enc_data.get('msg'):
            joined_msg, msg_parts_text = enc_tables.playfair_parts_text(msg, enc_data.get('parts'))
            form['msg_input'].setText(joined_msg)
            enc_tbl = tables.table_to_str(enc_data.get('enc_table'))
            form['enc_msg_input'].setText(enc_msg)
            form['enc_tbl_input'].setText(enc_tbl)
            form['parts_input'].setText(msg_parts_text)
            return

        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_playfair(form):
    proc_playfair(form, systems.enc_playfair)


def dec_proc_playfair(form):
    proc_playfair(form, systems.dec_playfair)


def proc_trisemus(form, encryption):
    try:
        msg = form['msg_input'].text().lower()
        rows = int(form['rows_input'].text())
        columns = int(form['columns_input'].text())
        key = form['key_input'].text().replace(' ', '').lower()
        alphabet = chars.CUT_RU_ALPHABET
        enc_data = encryption(msg, key, alphabet, rows, columns)

        if enc_msg := enc_data.get('msg'):
            msg_list = items.remove_all_items(' ', list(msg))
            parts = items.remove_all_items(' ', enc_data.get('parts'))
            msg_parts_text = tables.tables_to_str(msg_list, parts)
            form['msg_input'].setText(msg)
            enc_tbl = tables.table_to_str(enc_data.get('enc_table'))
            form['enc_msg_input'].setText(enc_msg)
            form['enc_tbl_input'].setText(enc_tbl)
            form['parts_input'].setText(msg_parts_text)
            return

        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_trisemus(form):
    proc_trisemus(form, systems.enc_trisemus)


def dec_proc_trisemus(form):
    proc_trisemus(form, systems.dec_trisemus)


def auto_playfair_trisemus(form):
    try:
        msg = form['msg_input'].text().replace(' ', '')
        rows_text = form['rows_input'].text().replace(' ', '')
        columns_text = form['columns_input'].text().replace(' ', '')
        key_text = form['key_input'].text().replace(' ', '')
        if any([rows_text, columns_text, key_text]):
            result = dialogs.question_msg_result(messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        if msg:
            random_size = random.choice([(16, 2), (2, 16), (4, 8), (8, 4)])
            rows, columns = random_size[0], random_size[1]
            key_index = random.randint(2, len(dictionary.animals))
            if key_words := dictionary.animals.get(key_index):
                key = random.choice(key_words)
                form['rows_input'].setText(str(rows))
                form['columns_input'].setText(str(columns))
                form['key_input'].setText(key)
            else:
                dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')


def proc_vigenere(form, encryption):
    try:
        msg = form['msg_input'].text().lower()
        key = form['key_input'].text().replace(' ', '').lower()
        alphabet = chars.RU_ALPHABET
        enc_data = encryption(msg, key, alphabet)
        if enc_msg := enc_data.get('msg'):
            form['msg_input'].setText(msg)
            enc_tbl = enc_tables.vigenere_table_text(enc_data.get('enc_table'), key, enc_msg, alphabet)
            form['enc_msg_input'].setText(enc_msg)
            form['enc_tbl_input'].setText(enc_tbl)
            enc_tables.vigenere_table(enc_data.get('enc_table'), form['enc_tbl_widget'], alphabet)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_vigenere(form):
    proc_vigenere(form, systems.enc_vigenere)


def dec_proc_vigenere(form):
    proc_vigenere(form, systems.dec_vigenere)


def auto_vigenere(form):
    try:
        msg = form['msg_input'].text().replace(' ', '')
        if form['key_input'].text().replace(' ', ''):
            result = dialogs.question_msg_result(messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        if msg:
            key_index = random.randint(2, len(dictionary.animals))
            if key_words := dictionary.animals.get(key_index):
                key = random.choice(key_words)
                form['key_input'].setText(key)
            else:
                dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')
