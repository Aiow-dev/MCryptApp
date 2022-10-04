from Assets import constants

from Scripts import base_scripts


def enc_trisemus(msg, key_word, size_a=4, size_b=8):
    msg = msg.lower()
    table_alphabet = constants.CUT_RU_ALPHABET
    enc_table = ''
    enc_table = base_scripts.sum_unique(key_word, enc_table)
    enc_table = base_scripts.sum_unique(table_alphabet, enc_table)
    table = [[0] * size_b for _ in range(size_a)]
    counter = 0
    enc_msg = ''
    for i in range(size_a):
        for j in range(size_b):
            table[i][j] = enc_table[counter % 32]
            counter += 1
    for i in msg:
        if i not in table_alphabet:
            enc_msg += i
        elif first := base_scripts.find(table, i, size_a, size_b):
            enc_msg += table[(first[0] + 1) % len(table)][first[1]]
        else:
            return 'Ошибка. Возможно, не найдена буква сообщения в таблице подстановок'
    return enc_msg, table


def dec_trisemus(enc_msg, key_word, size_a=4, size_b=8):
    enc_msg = enc_msg.lower()
    table_alphabet = constants.CUT_RU_ALPHABET
    enc_table = ''
    enc_table = base_scripts.sum_unique(key_word, enc_table)
    enc_table = base_scripts.sum_unique(table_alphabet, enc_table)
    table = [[0] * size_b for _ in range(size_a)]
    counter = 0
    msg = ''
    for i in range(size_a):
        for j in range(size_b):
            table[i][j] = enc_table[counter % 32]
            counter += 1
    for i in enc_msg:
        if i not in table_alphabet:
            msg += i
        elif first := base_scripts.find(table, i, size_a, size_b):
            msg += table[first[0] - 1][first[1]]
        else:
            return 'Ошибка. Возможно, не найдена буква сообщения в таблице подстановок'
    return msg, table
