import math

from Assets import constants


def enc_vigenere(msg, key):
    msg = msg.lower()
    table = constants.RU_ALPHABET
    big_table = []

    if not key:
        return 'Ключ не может быть пустым'

    enc_table = key * math.ceil(len(msg) // len(key))
    enc_table += key

    for _ in range(33):
        big_table.append(table)
        table = table[1:] + table[0]

    enc_msg = ''
    counter = 0

    for i in range(len(msg)):
        if msg[i] not in table:
            enc_msg += msg[i]
        else:
            enc_msg += big_table[table.find(msg[i])][table.find(enc_table[counter])]
            counter += 1
    return enc_msg, big_table


def dec_vigenere(enc_msg, key):
    enc_msg = enc_msg.lower()
    table = constants.RU_ALPHABET
    big_table = []

    if not key:
        return 'Ключ не может быть пустым'

    enc_table = key * math.ceil(len(enc_msg) // len(key))
    enc_table += key

    for _ in range(33):
        big_table.append(table)
        table = table[1:] + table[0]
    msg = ''
    counter = 0

    for i in range(len(enc_msg)):
        if enc_msg[i] not in table:
            msg += enc_msg[i]
        else:
            position = big_table[table.find(enc_table[counter])].find(enc_msg[i])
            msg += table[position]
            counter += 1
    return msg, big_table
