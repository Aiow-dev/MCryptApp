import math
import random

from helpers import tables, items
from components import enc_tables, dialogs, enc
from scripts.encryption import ms
from handlers import messages


def proc_ms(form_data, encryption):
    try:
        msg = form_data['msg_input'].text().replace(' ', '')
        tbl_rank = int(form_data['rank_input'].text())
        key_tbl = tables.table_num_items(form_data['key_tbl_widget'])
        if len(msg) != tbl_rank ** 2 or tbl_rank <= 0:
            err_msg = messages.MSG_RANK_ERROR
            dialogs.show_err_msg(err_msg, 'Ошибка')
            return
        enc_data = encryption(msg, key_tbl)
        if enc_msg := enc_data.get('msg'):
            form_data['enc_msg_input'].setText(enc_msg)
            tables.table(enc_data.get('enc_table'), enc_tables.table_row, form_data['enc_tbl_widget'])
            return
        err_msg = enc_data.get('err_msg')
        dialogs.show_err_msg(err_msg, 'Ошибка')
    except ValueError as value_error:
        dialogs.show_err_msg('Параметры шифрования не соответствуют требуемым!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось выполнить шифрование!', 'Ошибка')


def enc_proc_ms(form_data):
    proc_ms(form_data, ms.enc_magic_square)


def dec_proc_ms(form_data):
    proc_ms(form_data, ms.dec_magic_square)


def auto_ms(parent, form_data):
    try:
        msg = form_data['msg_input'].text().replace(' ', '')
        if not items.is_empty_table(form_data['key_tbl_widget']):
            result = dialogs.question_msg(parent, messages.OVERWRITE_PARAMETERS, 'Сгенерировать параметры')
            if not result:
                return
        len_msg = len(msg)
        if len_msg > 0:
            square = math.floor(math.sqrt(len_msg))
            if square * square == len_msg:
                if square < 3 or square > 6:
                    dialogs.show_err_msg(messages.MSG_OVER_LEN, 'Ошибка')
                    return
                form_data['rank_input'].setText(str(square))
                random_min = 3
                random_max = 9
                if square == 3:
                    random_min = 1
                    random_max = 3
                elif square == 5:
                    random_min = 10
                    random_max = 13
                elif square == 6:
                    random_min = 14
                    random_max = 15
                random_number = random.randint(random_min, random_max)
                table = enc.magic_squares.get(random_number)
                table_text = items.table_str_items(table)
                tables.table(table_text, enc_tables.table_row, form_data['key_tbl_widget'])
            else:
                dialogs.show_err_msg(messages.MSG_NOT_ROOT_LEN, 'Ошибка')
        else:
            dialogs.show_err_msg('Сообщение не заполнено!', 'Ошибка')
    except AttributeError as attribute_error:
        dialogs.show_err_msg('Не удалось сгенерировать параметры!', 'Ошибка')
