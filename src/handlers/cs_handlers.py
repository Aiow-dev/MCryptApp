from src.components import enc_tables, dialogs, chars
from src.helpers import tables
from src.scripts.encryption import cs


def proc_classic_cs(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        key = int(form_data['key_input'].text())
        alphabet = chars.RU_ALPHABET
        enc_data = encryption(msg, key, alphabet)
        if enc_msg := enc_data.get('msg'):
            enc_tbl = tables.tables_to_str(enc_data.get('table'), enc_data.get('enc_table'))
            form_data['enc_msg_input'].setText(enc_msg)
            form_data['enc_tbl_input'].setText(enc_tbl)
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_classic_cs(form_data):
    proc_classic_cs(form_data, cs.enc_classic_cs)


def dec_proc_classic_cs(form_data):
    proc_classic_cs(form_data, cs.dec_classic_cs)


def proc_affine_cs(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        key_a = int(form_data['key_a_input'].text())
        key_b = int(form_data['key_b_input'].text())
        alphabet = chars.RU_ALPHABET
        enc_data = encryption(msg, key_a, key_b, alphabet)
        if enc_msg := enc_data.get('msg'):
            nums_column, num_tbl = enc_tables.affine_table_num_text(key_a, key_b)
            letters_column, letters_tbl = enc_tables.affine_table_letter_text(key_a, key_b, nums_column, alphabet)
            form_data['enc_msg_input'].setText(enc_msg)
            enc_tables.affine_table(key_a, key_b, nums_column, form_data['enc_tbl_num_widget'])
            enc_tables.affine_table(key_a, key_b, letters_column, form_data['enc_tbl_letter_widget'])
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_affine_cs(form_data):
    proc_affine_cs(form_data, cs.enc_affine_cs)


def dec_proc_affine_cs(form_data):
    proc_affine_cs(form_data, cs.dec_affine_cs)


def proc_key_cs(form_data, encryption):
    try:
        msg = form_data['msg_input'].text()
        key = form_data['key_input'].text()
        key_k = int(form_data['key_k_input'].text())
        alphabet = chars.RU_ALPHABET
        enc_data = encryption(msg, key_k, key, alphabet)
        if enc_msg := enc_data.get('msg'):
            letters_column, enc_tbl = enc_tables.caesar_key_table_text(enc_data.get('enc_table'), alphabet)
            form_data['enc_msg_input'].setText(enc_msg)
            form_data['enc_tbl_input'].setText(enc_tbl)
            enc_tables.caesar_key_table(letters_column, form_data['enc_tbl_widget'])
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_key_cs(form_data):
    proc_key_cs(form_data, cs.enc_key_cs)


def dec_proc_key_cs(form_data):
    proc_key_cs(form_data, cs.dec_key_cs)
