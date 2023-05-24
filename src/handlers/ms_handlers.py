import math
import random

from src.helpers import items, tables
from src.components import enc_tables, dialogs, enc
from src.scripts.encryption import ms
from src.handlers import messages


def proc_ms(form, encryption):
    try:
        msg = form['msg_input'].text().replace(' ', '')
        tbl_rank = int(form['rank_input'].text())
        key_tbl = tables.table_num_items(form['key_tbl_widget'])
        if len(msg) != tbl_rank ** 2 or tbl_rank <= 0:
            err_msg = messages.MSG_RANK_ERR
            dialogs.show_err_msg(err_msg, 'Ошибка')
            return
        enc_data = encryption(msg, key_tbl)
        if enc_msg := enc_data.get('msg'):
            form['enc_msg_input'].setText(enc_msg)
            tables.table(enc_data.get('enc_table'), enc_tables.table_row, form['enc_tbl_widget'])
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_ms(form):
    proc_ms(form, ms.enc_magic_square)


def dec_proc_ms(form):
    proc_ms(form, ms.dec_magic_square)


def auto_ms(parent, form):
    try:
        msg = form['msg_input'].text().replace(' ', '')
        if not items.is_empty_table(form['key_tbl_widget']):
            result = dialogs.question_msg(parent, messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        len_msg = len(msg)
        if len_msg > 0:
            square = math.floor(math.sqrt(len_msg))
            if square * square == len_msg:
                if square < 3 or square > 6:
                    dialogs.show_err_msg(messages.MSG_OVER_LEN_ERR, 'Ошибка')
                    return
                form['rank_input'].setText(str(square))
                random_min = 3
                random_max = 8
                if square == 3:
                    random_min = 1
                    random_max = 3
                elif square == 5:
                    random_min = 9
                    random_max = 12
                elif square == 6:
                    random_min = 13
                    random_max = 14
                random_number = random.randint(random_min, random_max)
                table = enc.magic_squares.get(random_number)
                table_text = items.table_str_items(table)
                tables.table(table_text, enc_tables.table_row, form['key_tbl_widget'])
            else:
                dialogs.show_err_msg(messages.MSG_ROOT_LEN_ERR, 'Ошибка')
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')
