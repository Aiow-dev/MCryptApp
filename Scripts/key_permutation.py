def enc_key_permutation(msg, row, column, key):
    clear_msg = ''.join(msg.split(' ')).upper()
    k = row

    if len(clear_msg) != k * column:
        return 'Ошибка заполнения таблицы. Проверьте количество строк и столбцов'

    cipher = {}
    index_ch = 0
    for index, ch in enumerate(key.lower()):
        if ch in cipher:
            cipher[ch + str(index_ch)] = clear_msg[index * k:index * k + k]
            index_ch += 1
        else:
            cipher[ch] = clear_msg[index * k:index * k + k]

    sorted_cipher = sorted(cipher)

    enc_msg = ''.join(''.join([cipher[key][index] for key in sorted_cipher]) for index in range(k))

    table = {key: cipher[key] for key in sorted_cipher}

    return enc_msg, table


def dec_key_permutation(enc_msg, row, column, key):
    clear_enc_msg = ''.join(enc_msg.split(' ')).upper()
    if len(clear_enc_msg) != row * column:
        return 'Ошибка заполнения таблицы. Проверьте количество строк и столбцов'
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
    table = {key: ''.join(text[list(cipher.keys()).index(key)][0]) for key in cipher_list}
    return ''.join(''.join(index_text[0]) for index_text in text), table


if __name__ == '__main__':
    print(dec_key_permutation('ДВПЕМСЕПРТОЕНОИАГДЬЛЛЮОЬ', 4, 6, 'КОРОВА'))
