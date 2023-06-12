import itertools
import math

from src.scripts.encryption import messages
from src.scripts import script_helpers


def enc_playfair(msg, key, alphabet, size_a=4, size_b=8):
    if len(alphabet) != size_a * size_b or size_a <= 0 or size_b <= 0:
        return {'err_msg': messages.TABLE_CHARS_ERR}
    if not key:
        return {'err_msg': messages.EMPTY_KEY_ERR}
    enc_tbl = script_helpers.sum_unique(key, '')
    enc_tbl = script_helpers.sum_unique(alphabet, enc_tbl)
    tbl = [[0] * size_b for _ in range(size_a)]
    enc_msg = ''
    for counter, (i, j) in enumerate(itertools.product(range(size_a), range(size_b))):
        tbl[i][j] = enc_tbl[counter % 32]
    msg_parts = []
    for i in range(0, len(msg), 2):
        first = script_helpers.find(tbl, msg[i], size_a, size_b)
        second = script_helpers.find(tbl, msg[i + 1], size_a, size_b)
        if not first or not second:
            return {'err_msg': messages.NOT_FOUND_LETTER_ERR}
        if first[0] == second[0] and first[1] == second[1]:
            third = script_helpers.find(tbl, 'ъ', size_a, size_b)
            msg_part = script_helpers.enc_playfair_check(first, third, tbl)
            enc_msg += msg_part
            msg_parts.append(msg_part)
            msg_part = script_helpers.enc_playfair_check(second, third, tbl)
        else:
            msg_part = script_helpers.enc_playfair_check(first, second, tbl)
        enc_msg += msg_part
        msg_parts.append(msg_part)
    return {'msg': enc_msg, 'enc_table': tbl, 'parts': msg_parts}


def dec_playfair(enc_msg, key, alphabet, size_a=4, size_b=8):
    if len(alphabet) != size_a * size_b or size_a <= 0 or size_b <= 0:
        return {'err_msg': messages.TABLE_CHARS_ERR}
    if not key:
        return {'err_msg': messages.EMPTY_KEY_ERR}
    enc_tbl = script_helpers.sum_unique(key, '')
    enc_tbl = script_helpers.sum_unique(alphabet, enc_tbl)
    tbl = [[0] * size_b for _ in range(size_a)]
    msg = ''
    for counter, (i, j) in enumerate(itertools.product(range(size_a), range(size_b))):
        tbl[i][j] = enc_tbl[counter % 32]
    msg_parts = []
    for i in range(0, len(enc_msg), 2):
        first = script_helpers.find(tbl, enc_msg[i], size_a, size_b)
        second = script_helpers.find(tbl, enc_msg[i + 1], size_a, size_b)
        if not first or not second:
            return {'err_msg': messages.NOT_FOUND_LETTER_ERR}
        msg_part = script_helpers.dec_playfair_check(first, second, tbl)
        msg += msg_part
        msg_parts.append(msg_part)
    return {'msg': msg, 'enc_table': tbl, 'parts': msg_parts}


def enc_trisemus(msg, key, alphabet, size_a=4, size_b=8):
    if len(alphabet) != size_a * size_b or size_a <= 0 or size_b <= 0:
        return {'err_msg': messages.TABLE_CHARS_ERR}
    if not key:
        return {'err_msg': messages.EMPTY_KEY_ERR}
    enc_tbl = script_helpers.sum_unique(key, '')
    enc_tbl = script_helpers.sum_unique(alphabet, enc_tbl)
    tbl = [[0] * size_b for _ in range(size_a)]
    enc_msg = ''
    for counter, (i, j) in enumerate(itertools.product(range(size_a), range(size_b))):
        tbl[i][j] = enc_tbl[counter % 32]
    msg_parts = []
    for i in msg:
        if i not in alphabet:
            enc_msg += i
            msg_parts.append(i)
        elif first := script_helpers.find(tbl, i, size_a, size_b):
            msg_part = tbl[(first[0] + 1) % len(tbl)][first[1]]
            enc_msg += msg_part
            msg_parts.append(msg_part)
        else:
            return {'err_msg': messages.NOT_FOUND_LETTER_ERR}
    return {'msg': enc_msg, 'enc_table': tbl, 'parts': msg_parts}


def dec_trisemus(enc_msg, key, alphabet, size_a=4, size_b=8):
    if len(alphabet) != size_a * size_b or size_a <= 0 or size_b <= 0:
        return {'err_msg': messages.TABLE_CHARS_ERR}
    if not key:
        return {'err_msg': messages.EMPTY_KEY_ERR}
    enc_tbl = script_helpers.sum_unique(key, '')
    enc_tbl = script_helpers.sum_unique(alphabet, enc_tbl)
    tbl = [[0] * size_b for _ in range(size_a)]
    msg = ''
    for counter, (i, j) in enumerate(itertools.product(range(size_a), range(size_b))):
        tbl[i][j] = enc_tbl[counter % 32]
    msg_parts = []
    for i in enc_msg:
        if i not in alphabet:
            msg += i
            msg_parts.append(i)
        elif first := script_helpers.find(tbl, i, size_a, size_b):
            msg_part = tbl[first[0] - 1][first[1]]
            msg += msg_part
            msg_parts.append(msg_part)
        else:
            return {'err_msg': messages.NOT_FOUND_LETTER_ERR}
    return {'msg': msg, 'enc_table': tbl, 'parts': msg_parts}


def enc_vigenere(msg, key, alphabet):
    if not msg:
        return {'err_msg': messages.MSG_EMPTY_ERR}
    if not key.replace(' ', ''):
        return {'err_msg': messages.EMPTY_KEY_ERR}
    msg = msg.lower()
    key = key.lower()
    tbl = alphabet
    big_tbl = []
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
    if not enc_msg:
        return {'err_msg': messages.MSG_EMPTY_ERR}
    if not key.replace(' ', ''):
        return {'err_msg': messages.EMPTY_KEY_ERR}
    enc_msg = enc_msg.lower()
    key = key.lower()
    tbl = alphabet
    big_tbl = []
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


if __name__ == '__main__':
    data = enc_playfair('Прилетаю десятого в полдень', 'пчела', 'абвгдежзийклмнопрстуфхцчшщъыьэюя')
    print(data)
