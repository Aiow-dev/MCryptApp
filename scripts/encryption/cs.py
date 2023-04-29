import math

from scripts import script_helpers


def enc_classic_cs(msg, key, alphabet):
    if key <= 0:
        return {'err_msg': 'Ошибка. Число символов ключа не может быть отрицательно или равно 0!'}
    if key > len(alphabet):
        return {'err_msg': 'Ошибка. Число символов ключа превышает число символов алфавита!'}
    msg = msg.lower()
    tbl = alphabet
    enc_tbl = ''.join(tbl[i % 33] for i in range(key, 33 + key))
    enc_msg = ''.join(i if i not in tbl else enc_tbl[tbl.find(i)] for i in msg)
    return {'msg': enc_msg, 'table': tbl, 'enc_table': enc_tbl}


def dec_classic_cs(enc_msg, key, alphabet):
    if key <= 0:
        return {'err_msg': 'Ошибка. Число символов ключа не может быть отрицательно или равно 0!'}
    if key > len(alphabet):
        return {'err_msg': 'Ошибка. Число символов ключа превышает число символов алфавита!'}
    enc_msg = enc_msg.lower()
    tbl = alphabet
    enc_tbl = ''.join(tbl[i % 33] for i in range(key, 33 + key))
    enc_msg = ''.join(i if i not in tbl else tbl[enc_tbl.find(i)] for i in enc_msg)
    return {'msg': enc_msg, 'table': tbl, 'enc_table': enc_tbl}


def enc_affine_cs(msg, key_a, key_b, alphabet):
    if math.gcd(key_a, len(alphabet)) != 1 or key_a <= 0:
        return {'err_msg': 'Ошибка. Значение ключа a и число символов алфавита не являются взаимно простыми числами!'}
    msg = msg.lower()
    tbl = alphabet
    enc_tbl = ''.join(tbl[(key_a * i + key_b) % 33] for i in range(33))
    enc_msg = ''.join(i if i not in tbl else enc_tbl[tbl.find(i)] for i in msg)
    return {'msg': enc_msg, 'table': tbl, 'enc_table': enc_tbl}


def dec_affine_cs(enc_msg, key_a, key_b, alphabet):
    if math.gcd(key_a, len(alphabet)) != 1 or key_a <= 0:
        return {'err_msg': 'Ошибка. Значение ключа a и число символов алфавита не являются взаимно простыми числами!'}
    enc_msg = enc_msg.lower()
    tbl = alphabet
    enc_tbl = ''
    for i in range(33):
        rang = (key_a * i + key_b) % 33
        enc_tbl += tbl[rang]
    msg = ''.join(i if i not in tbl else tbl[enc_tbl.find(i)] for i in enc_msg)
    return {'msg': msg, 'table': tbl, 'enc_table': enc_tbl}


def enc_key_cs(msg, key_num, key_word, alphabet):
    if key_num <= 0:
        return {'err_msg': 'Ошибка. Число символов ключа k не может быть отрицательно или равно 0!'}
    if key_num >= len(alphabet):
        return {'err_msg': 'Ошибка. Число символов ключа k превышает или равно числу символов алфавита!'}
    msg = msg.lower()
    table = alphabet
    enc_tbl = script_helpers.sum_unique(key_word, '')
    enc_tbl = script_helpers.sum_unique(table, enc_tbl)
    for _ in range(key_num):
        enc_tbl = enc_tbl[-1] + enc_tbl[:-1]
    enc_msg = ''.join(i if i not in table else enc_tbl[table.find(i)] for i in msg)
    return {'msg': enc_msg, 'enc_table': enc_tbl}


def dec_key_cs(enc_msg, key_num, key_word, alphabet):
    if key_num <= 0:
        return {'err_msg': 'Ошибка. Число символов ключа k не может быть отрицательно или равно 0!'}
    if key_num >= len(alphabet):
        return {'err_msg': 'Ошибка. Число символов ключа k превышает или равно числу символов алфавита!'}
    enc_msg = enc_msg.lower()
    tbl = alphabet
    enc_tbl = script_helpers.sum_unique(key_word, '')
    enc_tbl = script_helpers.sum_unique(tbl, enc_tbl)
    for _ in range(key_num):
        enc_tbl = enc_tbl[-1] + enc_tbl[:-1]
    msg = ''.join(i if i not in tbl else tbl[enc_tbl.find(i)] for i in enc_msg)
    return {'msg': msg, 'enc_table': enc_tbl}
