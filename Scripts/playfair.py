import itertools

from Assets import constants

from Scripts import base_scripts


def enc_playfair(msg, key_word, size_a=4, size_b=8):
    msg = msg.replace(' ', '').lower()
    if len(msg) % 2 == 1:
        msg += "ъ"
    table_alphabet = constants.CUT_RU_ALPHABET
    enc_table = ''
    enc_table = base_scripts.sum_unique(key_word, enc_table)
    enc_table = base_scripts.sum_unique(table_alphabet, enc_table)
    table = [[0] * size_b for _ in range(size_a)]
    enc_msg = ''
    for counter, (i, j) in enumerate(itertools.product(range(size_a), range(size_b))):
        table[i][j] = enc_table[counter % 32]
    for i in range(0, len(msg), 2):
        first = base_scripts.find(table, msg[i], size_a, size_b)
        second = base_scripts.find(table, msg[i + 1], size_a, size_b)

        if not first or not second:
            return 'Ошибка. Возможно, не найдена буква сообщения в таблице подстановок'

        if first[0] == second[0] and first[1] == second[1]:
            third = base_scripts.find(table, "ъ", size_a, size_b)
            enc_msg += base_scripts.enc_playfair_check(first, third, table)
            enc_msg += base_scripts.enc_playfair_check(second, third, table)
        else:
            enc_msg += base_scripts.enc_playfair_check(first, second, table)
    return enc_msg, table


def dec_playfair(enc_msg, key_word, size_a=4, size_b=8):
    enc_msg = enc_msg.replace(' ', '').lower()
    if len(enc_msg) % 2 == 1:
        enc_msg += "ъ"
    table_alphabet = constants.CUT_RU_ALPHABET
    enc_table = ''
    enc_table = base_scripts.sum_unique(key_word, enc_table)
    enc_table = base_scripts.sum_unique(table_alphabet, enc_table)
    table = [[0] * size_b for _ in range(size_a)]
    msg = ''
    for counter, (i, j) in enumerate(itertools.product(range(size_a), range(size_b))):
        table[i][j] = enc_table[counter % 32]
    for i in range(0, len(enc_msg), 2):
        first = base_scripts.find(table, enc_msg[i], size_a, size_b)
        second = base_scripts.find(table, enc_msg[i + 1], size_a, size_b)

        if not first or not second:
            return 'Ошибка. Возможно, не найдена буква сообщения в таблице подстановок'

        msg += base_scripts.dec_playfair_check(first, second, table)
    return msg, table
