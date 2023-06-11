from . import messages
from src.scripts import script_helpers


def enc_double_playfair(msg, left_tbl, right_tbl, charset):
    if not msg:
        return {'err_msg': messages.MSG_EMPTY_ERR}
    left_size = len(left_tbl), len(left_tbl[0])
    right_size = len(right_tbl), len(right_tbl[0])
    if left_size[0] != right_size[0] and left_size[1] != right_size[1]:
        return {'err_msg': messages.TABLES_RANKS_ERR}
    if left_size[0] * left_size[1] > len(charset):
        return {'err_msg': messages.OVER_TABLES_SIZE_ERR}
    msg = msg.upper()
    len_msg = len(msg)
    if len_msg % 2 == 1:
        msg += 'Ъ'
    enc_msg = ''
    for i in range(0, len_msg, 2):
        first = script_helpers.find(left_tbl, msg[i], left_size[0], left_size[1])
        second = script_helpers.find(right_tbl, msg[i + 1], right_size[0], right_size[1])
        if not first or not second:
            return {'err_msg': messages.NOT_FOUND_LETTER_ERR}
        if first[0] == second[0]:
            enc_msg += right_tbl[first[0]][first[1]]
            enc_msg += left_tbl[second[0]][second[1]]
        else:
            enc_msg += right_tbl[first[0]][second[1]]
            enc_msg += left_tbl[second[0]][first[1]]
    return {'msg': enc_msg}


def dec_double_playfair(enc_msg, left_tbl, right_tbl, charset):
    if not enc_msg:
        return {'err_msg': messages.MSG_EMPTY_ERR}
    left_size = len(left_tbl), len(left_tbl[0])
    right_size = len(right_tbl), len(right_tbl[0])
    if left_size[0] != right_size[0] and left_size[1] != right_size[1]:
        return {'err_msg': messages.TABLES_RANKS_ERR}
    if left_size[0] * left_size[1] > len(charset):
        return {'err_msg': messages.OVER_TABLES_SIZE_ERR}
    enc_msg = enc_msg.upper()
    len_msg = len(enc_msg)
    if len_msg % 2 == 1:
        enc_msg += 'Ъ'
    msg = ''
    for i in range(0, len_msg, 2):
        first = script_helpers.find(right_tbl, enc_msg[i], left_size[0], left_size[1])
        second = script_helpers.find(left_tbl, enc_msg[i + 1], right_size[0], right_size[1])
        if not first or not second:
            return {'err_msg': messages.NOT_FOUND_LETTER_ERR}
        if first[0] == second[0]:
            msg += left_tbl[first[0]][first[1]]
            msg += right_tbl[second[0]][second[1]]
        else:
            msg += left_tbl[first[0]][second[1]]
            msg += right_tbl[second[0]][first[1]]
    return {'msg': msg}


if __name__ == '__main__':
    left_table = [['Ж', 'Щ', 'Н', 'Ю', 'Р'],
                  ['И', 'Т', 'Ь', 'Ц', 'Б'],
                  ['Я', 'М', 'Е', '.', 'С'],
                  ['В', 'Ы', 'П', 'Ч', ' '],
                  [':', 'Д', 'У', 'О', 'К'],
                  ['З', 'Э', 'Ф', 'Г', 'Ш'],
                  ['Х', 'А', ',', 'Л', 'Ъ']]

    right_table = [['И', 'Ч', 'Г', 'Я', 'Т'],
                   [',', 'Ж', 'Ь', 'М', 'О'],
                   ['З', 'Ю', 'Р', 'В', 'Щ'],
                   ['Ц', ':', 'П', 'Е', 'Л'],
                   ['Ъ', 'А', 'Н', '.', 'Х'],
                   ['Э', 'К', 'С', 'Ш', 'Д'],
                   ['Б', 'Ф', 'У', 'Ы', ' ']]

    chars = 'абвгдежзиклмнопрстуфхцчшщъыьэюя .:,'
    encryption_message = enc_double_playfair('ПРИЛЕТАЮ ШЕСТОГО', left_table, right_table, chars)
    print(f'{encryption_message=}')

    message = dec_double_playfair(encryption_message.get('msg'), left_table, right_table, chars)
    print(f'{message}')
