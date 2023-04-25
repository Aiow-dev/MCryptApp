import itertools
import math

from scripts import script_helpers


def enc_playfair(msg, key_word, alphabet, size_a=4, size_b=8):
    msg = msg.replace(' ', '').lower()

    if len(msg) % 2 == 1:
        msg += 'ъ'

    enc_tbl = script_helpers.sum_unique(key_word, '')
    enc_tbl = script_helpers.sum_unique(alphabet, enc_tbl)
    tbl = [[0] * size_b for _ in range(size_a)]
    enc_msg = ''

    for counter, (i, j) in enumerate(itertools.product(range(size_a), range(size_b))):
        tbl[i][j] = enc_tbl[counter % 32]

    for i in range(0, len(msg), 2):
        first = script_helpers.find(tbl, msg[i], size_a, size_b)
        second = script_helpers.find(tbl, msg[i + 1], size_a, size_b)

        if not first or not second:
            return {'err_msg': 'Ошибка. Не найдена буква сообщения в таблице подстановок!'}

        if first[0] == second[0] and first[1] == second[1]:
            third = script_helpers.find(tbl, 'ъ', size_a, size_b)
            enc_msg += script_helpers.enc_playfair_check(first, third, tbl)
            enc_msg += script_helpers.enc_playfair_check(second, third, tbl)
        else:
            enc_msg += script_helpers.enc_playfair_check(first, second, tbl)
    return {'msg': enc_msg, 'enc_table': tbl}


def dec_playfair(enc_msg, key_word, alphabet, size_a=4, size_b=8):
    enc_msg = enc_msg.replace(' ', '').lower()

    if len(enc_msg) % 2 == 1:
        enc_msg += 'ъ'

    enc_tbl = script_helpers.sum_unique(key_word, '')
    enc_tbl = script_helpers.sum_unique(alphabet, enc_tbl)
    tbl = [[0] * size_b for _ in range(size_a)]
    msg = ''

    for counter, (i, j) in enumerate(itertools.product(range(size_a), range(size_b))):
        tbl[i][j] = enc_tbl[counter % 32]

    for i in range(0, len(enc_msg), 2):
        first = script_helpers.find(tbl, enc_msg[i], size_a, size_b)
        second = script_helpers.find(tbl, enc_msg[i + 1], size_a, size_b)

        if not first or not second:
            return {'err_msg': 'Ошибка. Не найдена буква сообщения в таблице подстановок!'}

        msg += script_helpers.dec_playfair_check(first, second, tbl)
    return {'msg': msg, 'enc_table': tbl}


def enc_trisemus(msg, key_word, alphabet, size_a=4, size_b=8):
    msg = msg.lower()
    enc_tbl = script_helpers.sum_unique(key_word, '')
    enc_tbl = script_helpers.sum_unique(alphabet, enc_tbl)
    tbl = [[0] * size_b for _ in range(size_a)]
    counter = 0
    enc_msg = ''

    for i in range(size_a):
        for j in range(size_b):
            tbl[i][j] = enc_tbl[counter % 32]
            counter += 1

    for i in msg:
        if i not in alphabet:
            enc_msg += i
        elif first := script_helpers.find(tbl, i, size_a, size_b):
            enc_msg += tbl[(first[0] + 1) % len(tbl)][first[1]]
        else:
            return {'err_msg': 'Ошибка. Не найдена буква сообщения в таблице подстановок!'}
    return {'msg': enc_msg, 'enc_table': tbl}


def dec_trisemus(enc_msg, key_word, alphabet, size_a=4, size_b=8):
    enc_msg = enc_msg.lower()
    enc_tbl = script_helpers.sum_unique(key_word, '')
    enc_tbl = script_helpers.sum_unique(alphabet, enc_tbl)
    tbl = [[0] * size_b for _ in range(size_a)]
    counter = 0
    msg = ''

    for i in range(size_a):
        for j in range(size_b):
            tbl[i][j] = enc_tbl[counter % 32]
            counter += 1

    for i in enc_msg:
        if i not in alphabet:
            msg += i
        elif first := script_helpers.find(tbl, i, size_a, size_b):
            msg += tbl[first[0] - 1][first[1]]
        else:
            return {'err_msg': 'Ошибка. Не найдена буква сообщения в таблице подстановок!'}
    return {'msg': msg, 'enc_table': tbl}


def enc_vigenere(msg, key, alphabet):
    msg = msg.lower()
    tbl = alphabet
    big_tbl = []

    if not key:
        return 'Ошибка. Ключ не может быть пустым!'

    enc_tbl = key * math.ceil(len(msg) // len(key)) + key

    for _ in range(33):
        big_tbl.append(tbl)
        tbl = tbl[1:] + tbl[0]

    enc_msg = ''
    counter = 0

    for i in range(len(msg)):
        if msg[i] not in tbl:
            enc_msg += msg[i]
        else:
            enc_msg += big_tbl[tbl.find(msg[i])][tbl.find(enc_tbl[counter])]
            counter += 1
    return {'msg': enc_msg, 'enc_table': big_tbl}


def dec_vigenere(enc_msg, key, alphabet):
    enc_msg = enc_msg.lower()
    tbl = alphabet
    big_tbl = []

    if not key:
        return 'Ошибка. Ключ не может быть пустым!'

    enc_table = key * math.ceil(len(enc_msg) // len(key)) + key

    for _ in range(33):
        big_tbl.append(tbl)
        tbl = tbl[1:] + tbl[0]
    msg = ''
    counter = 0

    for i in range(len(enc_msg)):
        if enc_msg[i] not in tbl:
            msg += enc_msg[i]
        else:
            position = big_tbl[tbl.find(enc_table[counter])].find(enc_msg[i])
            msg += tbl[position]
            counter += 1
    return {'msg': msg, 'enc_table': big_tbl}
