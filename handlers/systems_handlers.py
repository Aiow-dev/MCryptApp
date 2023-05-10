from helpers import tables
from components import dialogs, chars, enc_tables
from scripts.encryption import systems


def proc_playfair_trisemus(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        rows = int(form_data['rows_input'].text())
        columns = int(form_data['columns_input'].text())
        key = form_data['key_input'].text()
        alphabet = chars.CUT_RU_ALPHABET
        enc_data = encryption(msg, key, alphabet, rows, columns)
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


def enc_proc_playfair(form_data):
    proc_playfair_trisemus(form_data, systems.enc_playfair)


def dec_proc_playfair(form_data):
    proc_playfair_trisemus(form_data, systems.dec_playfair)


def enc_proc_trisemus(form_data):
    proc_playfair_trisemus(form_data, systems.enc_trisemus)


def dec_proc_trisemus(form_data):
    proc_playfair_trisemus(form_data, systems.dec_trisemus)


def proc_vigenere(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        key = form_data['key_input'].text()
        alphabet = chars.RU_ALPHABET
        enc_data = encryption(msg, key, alphabet)
        if enc_msg := enc_data.get('msg'):
            enc_tbl = enc_tables.vigenere_table_text(enc_data.get('enc_table'), key, enc_msg, alphabet)
            form_data['enc_msg_input'].setText(enc_msg)
            form_data['enc_tbl_input'].setText(enc_tbl)
            enc_tables.vigenere_table(enc_data.get('enc_table'), form_data['enc_tbl_widget'], alphabet)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_vigenere(form_data):
    proc_vigenere(form_data, systems.enc_vigenere)


def dec_proc_vigenere(form_data):
    proc_vigenere(form_data, systems.dec_vigenere)
