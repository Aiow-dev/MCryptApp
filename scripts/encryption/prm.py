def enc_simple_prm(msg, row, column):  # Шифруемая фраза "Прилетаю седьмого в полдень"
    msg = msg.replace(' ', '').upper()  # Строки - 4, Столбцы - 6 Результат - "ПЕСМВДРТЕОПЕИАДГОНЛЬЮОЛЬ"
    if len(msg) != row * column or row <= 0 or column <= 0:
        return {'err_msg': 'Ошибка заполнения таблицы. Проверьте количество строк и столбцов!'}
    mas = [[] for _ in range(row)]
    index = -1
    for j in range(column):
        for i in range(row):
            index += 1
            mas[i].insert(j, msg[index])
    enc_msg = ''
    for i in range(row):
        for j in range(column):
            enc_msg += mas[i][j]
    return {'msg': enc_msg, 'enc_table': mas}


def dec_simple_prm(enc_msg, row, column):  # Строка - "ПЕСМВДРТЕОПЕИАДГОНЛЮЬОЛЬ"
    enc_msg = enc_msg.replace(' ', '').upper()  # Строки - 4, Столбцы - 6 Результат - "ПРИЛЕТАЮСЕДЬМОГОВПОЛДЕНЬ"
    if len(enc_msg) != row * column or row <= 0 or column <= 0:
        return {'err_msg': 'Ошибка заполнения таблицы. Проверьте количество строк и столбцов!'}
    mas = [[] for _ in range(row)]
    index = -1
    for j in range(row):
        for i in range(column):
            index += 1
            mas[j].insert(i, enc_msg[index])
    msg = ''
    for i in range(column):
        for j in range(row):
            msg += mas[j][i]
    return {'msg': msg, 'enc_table': mas}


def enc_key_prm(msg, row, column, key):
    clear_msg = ''.join(msg.split(' ')).upper()
    k = row
    if len(clear_msg) != k * column or k <= 0 or column <= 0:
        return {'err_msg': 'Ошибка заполнения таблицы. Проверьте количество строк и столбцов!'}
    if len(key) != column:
        return {'err_msg': 'Ошибка заполнения таблицы. Число символов ключа не равно числу столбцов!'}
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
    return {'msg': enc_msg, 'enc_table': table}


def dec_key_prm(enc_msg, row, column, key):
    clear_enc_msg = ''.join(enc_msg.split(' ')).upper()
    if len(clear_enc_msg) != row * column:
        return {'err_msg': 'Ошибка заполнения таблицы. Проверьте количество строк и столбцов!'}
    if len(key) != column:
        return {'err_msg': 'Ошибка заполнения таблицы. Число символов ключа не равно числу столбцов!'}
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
    msg = ''.join(''.join(index_text[0]) for index_text in text)
    table = {key: ''.join(text[list(cipher.keys()).index(key)][0]) for key in cipher_list}
    return {'msg': msg, 'enc_table': table}


def enc_double_prm(msg, row, clm, key_row, key_clm):
    msg = msg.replace(' ', '').upper()
    clm_tbl = {}
    if len(msg) != row * clm or row <= 0 or clm <= 0:
        return {'err_msg': 'Ошибка заполнения таблицы. Проверьте количество строк и столбцов!'}
    for index_clm, num_clm in enumerate(key_clm):
        part_clm_tbl = []
        for index_row in range(row):
            offset = index_row * clm + index_clm
            part_clm_tbl.append(msg[offset])
        clm_tbl[str(num_clm) + str(index_clm)] = part_clm_tbl
    sort_clm_tbl = [clm_tbl[sort_key] for sort_key in sorted(clm_tbl)]
    row_tbl = {}
    for index_row, num_row in enumerate(key_row):
        part_row_tbl = [sort_clm_tbl[index_clm][index_row] for index_clm in range(clm)]
        row_tbl[num_row] = part_row_tbl
    sort_row_tbl = [row_tbl[sort_key] for sort_key in sorted(row_tbl)]
    return {'msg': ''.join(''.join(sort_row) for sort_row in sort_row_tbl),
            'enc_table': sort_row_tbl}


def dec_double_prm(enc_msg, row, clm, key_row, key_clm):
    enc_msg = enc_msg.replace(' ', '').upper()
    clm_tbl = {}
    if len(enc_msg) != row * clm or row <= 0 or clm <= 0:
        return {'err_msg': 'Ошибка заполнения таблицы. Проверьте количество строк и столбцов!'}
    for index_clm, num_clm in enumerate(key_clm):
        part_clm_tbl = []
        for index_row in range(row):
            offset = index_row * clm + index_clm
            part_clm_tbl.append(enc_msg[offset])
        clm_tbl[str(index_clm + 1)] = part_clm_tbl
    clm_tbl_key = [clm_tbl[key] for key in key_clm]
    row_tbl = {}
    for index_row, num_row in enumerate(key_row):
        part_row_tbl = [clm_tbl_key[index_clm][index_row] for index_clm in range(clm)]
        row_tbl[str(index_row + 1)] = part_row_tbl
    row_tbl_key = [row_tbl[key] for key in key_row]
    return {'msg': ''.join(''.join(part_row) for part_row in row_tbl_key),
            'enc_table': row_tbl_key}