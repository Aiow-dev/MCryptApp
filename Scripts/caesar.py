from Assets import constants

from Scripts import base_scripts


def enc_classic_caesar(msg, key):
    msg = msg.lower()
    table = constants.RU_ALPHABET
    enc_table = "".join(table[i % 33] for i in range(key, 33 + key))
    enc_msg = "".join(i if i not in table else enc_table[table.find(i)] for i in msg)

    return enc_msg, table, enc_table


def dec_classic_caesar(enc_msg, key):
    enc_msg = enc_msg.lower()
    table = constants.RU_ALPHABET
    enc_table = "".join(table[i % 33] for i in range(key, 33 + key))
    msg = "".join(i if i not in table else table[enc_table.find(i)] for i in enc_msg)

    return msg, table, enc_table


def enc_affine_caesar(msg, key_a, key_b):
    if key_a < key_b:
        return "Не выполнены условия шифрования (a<b)"
    msg = msg.lower()
    table = constants.RU_ALPHABET
    enc_table = ''.join(table[(key_a * i + key_b) % 33] for i in range(33))
    enc_msg = ''.join(i if i not in table else enc_table[table.find(i)] for i in msg)

    return enc_msg, table, enc_table


def dec_affine_caesar(enc_msg, key_a, key_b):
    if key_a < key_b:
        return "Не выполнены условия шифрования (a<b)"
    enc_msg = enc_msg.lower()
    table = constants.RU_ALPHABET
    enc_table = ''
    for i in range(33):
        rang = (key_a * i + key_b) % 33
        enc_table += table[rang]
    msg = ''.join(i if i not in table else table[enc_table.find(i)] for i in enc_msg)

    return msg, table, enc_table


def enc_key_caesar(msg, key_num, key_word):
    msg = msg.lower()
    table = constants.RU_ALPHABET
    enc_table = ''
    enc_table = base_scripts.sum_unique(key_word, enc_table)
    enc_table = base_scripts.sum_unique(table, enc_table)
    for _ in range(key_num):
        enc_table = enc_table[-1] + enc_table[:-1]
    enc_msg = "".join(i if i not in table else enc_table[table.find(i)] for i in msg)

    return enc_msg, enc_table


def dec_key_caesar(enc_msg, key_num, key_word):
    enc_msg = enc_msg.lower()
    table = constants.RU_ALPHABET
    enc_table = ''
    enc_table = base_scripts.sum_unique(key_word, enc_table)
    enc_table = base_scripts.sum_unique(table, enc_table)
    for _ in range(key_num):
        enc_table = enc_table[-1] + enc_table[:-1]
    msg = "".join(i if i not in table else table[enc_table.find(i)] for i in enc_msg)

    return msg, enc_table
