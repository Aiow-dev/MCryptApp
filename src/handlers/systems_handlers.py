from src.helpers import tables
from src.components import enc_tables, dialogs, chars
from src.scripts.encryption import systems


def proc_playfair_trisemus(form, encryption):
    try:
        msg = form['msg_input'].text()
        rows = int(form['rows_input'].text())
        columns = int(form['columns_input'].text())
        key = form['key_input'].text()
        alphabet = chars.CUT_RU_ALPHABET
        enc_data = encryption(msg, key, alphabet, rows, columns)
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


def enc_proc_playfair(form):
    proc_playfair_trisemus(form, systems.enc_playfair)


def dec_proc_playfair(form):
    proc_playfair_trisemus(form, systems.dec_playfair)


def enc_proc_trisemus(form):
    proc_playfair_trisemus(form, systems.enc_trisemus)


def dec_proc_trisemus(form):
    proc_playfair_trisemus(form, systems.dec_trisemus)


def proc_vigenere(form, encryption):
    try:
        msg = form['msg_input'].text()
        key = form['key_input'].text()
        alphabet = chars.RU_ALPHABET
        enc_data = encryption(msg, key, alphabet)
        if enc_msg := enc_data.get('msg'):
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
