import math

from . import messages
from src.scripts import script_helpers


def enc_classic_cs(msg, key, alphabet):
    if not msg:
        return {'err_msg': messages.MSG_EMPTY_ERR}
    if key <= 0:
        return {'err_msg': messages.NOT_POS_KEY_ERR}
    if key > len(alphabet):
        return {'err_msg': messages.OVER_CHARS_KEY_ERR}
    enc_tbl = ''.join(alphabet[i % 33] for i in range(key, 33 + key))
    enc_msg = ''.join(i if i not in alphabet else enc_tbl[alphabet.find(i)] for i in msg)
    return {'msg': enc_msg, 'table': alphabet, 'enc_table': enc_tbl}


def dec_classic_cs(enc_msg, key, alphabet):
    if not enc_msg:
        return {'err_msg': messages.MSG_EMPTY_ERR}
    if key <= 0:
        return {'err_msg': messages.NOT_POS_KEY_ERR}
    if key > len(alphabet):
        return {'err_msg': messages.OVER_CHARS_KEY_ERR}
    enc_tbl = ''.join(alphabet[i % 33] for i in range(key, 33 + key))
    enc_msg = ''.join(i if i not in alphabet else alphabet[enc_tbl.find(i)] for i in enc_msg)
    return {'msg': enc_msg, 'table': alphabet, 'enc_table': enc_tbl}


def enc_affine_cs(msg, key_a, key_b, alphabet):
    if not msg:
        return {'err_msg': messages.MSG_EMPTY_ERR}
    if key_a <= 0:
        return {'err_msg': messages.NOT_POS_KEY_ERR}
    if math.gcd(key_a, len(alphabet)) != 1:
        return {'err_msg': messages.KEY_A_GCD_CHARS_ERR}
    enc_tbl = ''.join(alphabet[(key_a * i + key_b) % 33] for i in range(33))
    enc_msg = ''.join(i if i not in alphabet else enc_tbl[alphabet.find(i)] for i in msg)
    return {'msg': enc_msg, 'table': alphabet, 'enc_table': enc_tbl}


def dec_affine_cs(enc_msg, key_a, key_b, alphabet):
    if not enc_msg:
        return {'err_msg': messages.MSG_EMPTY_ERR}
    if key_a <= 0:
        return {'err_msg': messages.NOT_POS_KEY_ERR}
    if math.gcd(key_a, len(alphabet)) != 1:
        return {'err_msg': messages.KEY_A_GCD_CHARS_ERR}
    enc_tbl = ''
    for i in range(33):
        rang = (key_a * i + key_b) % 33
        enc_tbl += alphabet[rang]
    msg = ''.join(i if i not in alphabet else alphabet[enc_tbl.find(i)] for i in enc_msg)
    return {'msg': msg, 'table': alphabet, 'enc_table': enc_tbl}


def enc_key_cs(msg, key_num, key_word, alphabet):
    if not msg:
        return {'err_msg': messages.MSG_EMPTY_ERR}
    if key_num <= 0:
        return {'err_msg': messages.NOT_POS_KEY_K_ERR}
    if key_num >= len(alphabet):
        return {'err_msg': messages.KEY_K_CHARS_ERR}
    enc_tbl = script_helpers.sum_unique(key_word, '')
    enc_tbl = script_helpers.sum_unique(alphabet, enc_tbl)
    for _ in range(key_num):
        enc_tbl = enc_tbl[-1] + enc_tbl[:-1]
    enc_msg = ''.join(i if i not in alphabet else enc_tbl[alphabet.find(i)] for i in msg)
    return {'msg': enc_msg, 'enc_table': enc_tbl}


def dec_key_cs(enc_msg, key_num, key_word, alphabet):
    if not enc_msg:
        return {'err_msg': messages.MSG_EMPTY_ERR}
    if key_num <= 0:
        return {'err_msg': messages.NOT_POS_KEY_K_ERR}
    if key_num >= len(alphabet):
        return {'err_msg': messages.KEY_K_CHARS_ERR}
    enc_tbl = script_helpers.sum_unique(key_word, '')
    enc_tbl = script_helpers.sum_unique(alphabet, enc_tbl)
    for _ in range(key_num):
        enc_tbl = enc_tbl[-1] + enc_tbl[:-1]
    msg = ''.join(i if i not in alphabet else alphabet[enc_tbl.find(i)] for i in enc_msg)
    return {'msg': msg, 'enc_table': enc_tbl}
