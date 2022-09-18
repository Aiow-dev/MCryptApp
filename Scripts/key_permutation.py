def enc_key_permutation(msg, row, column, key):
    clear_msg = ''.join(msg.split(' ')).upper()
    k = row

    if len(clear_msg) != k * column:
        return "Ошибка заполнения таблицы. Проверьте количество строк и столбцов"

    cipher = {}
    index_ch = 0
    for index, ch in enumerate(key.lower()):
        if ch in cipher:
            cipher[ch + str(index_ch)] = clear_msg[index * k:index * k + k]
            index_ch += 1
        else:
            cipher[ch] = clear_msg[index * k:index * k + k]
    return ''.join(''.join([cipher[key][index] for key in sorted(cipher.keys())]) for index in range(k))


def dec_key_permutation(enc_msg, row, column, key):
    clear_enc_msg = ''.join(enc_msg.split(' ')).upper()
    if len(clear_enc_msg) != row * column:
        return "Ошибка заполнения таблицы. Проверьте количество строк и столбцов"
    mas = [[] for _ in range(column)]
    for i in range(column):
        for k in range(row):
            mas[i].insert(k, clear_enc_msg[i + column * k])
    cipher = {}
    for index_ch, ch in enumerate(key.lower()):
        if ch in cipher:
            cipher[ch + str(index_ch)] = index_ch
        else:
            cipher[ch] = index_ch
    cipher_list = sorted(cipher)
    text = [[] for _ in range(column)]
    for temp, i in enumerate(cipher_list):
        text[cipher[i]].insert(0, mas[temp])
    return "".join(''.join(index_text[0]) for index_text in text)
