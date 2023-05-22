from src.helpers import encryption


def enc_magic_square(msg, key_tbl):
    if not encryption.check_magic_square(key_tbl):
        return {'err_msg': 'Ошибка. Таблица не является магическим квадратом!'}
    tbl = []
    enc_msg = ''
    for row in key_tbl:
        part_tbl = []
        for clm in row:
            part_tbl.append(msg[clm - 1])
            enc_msg += msg[clm - 1]
        tbl.append(part_tbl)
    return {'msg': enc_msg, 'enc_table': tbl}


def dec_magic_square(enc_msg, key_tbl):
    if not encryption.check_magic_square(key_tbl):
        return {'err_msg': 'Ошибка. Таблица не является магическим квадратом!'}
    tbl_rank = len(key_tbl)
    tbl = []
    msg = ['' for _ in range(tbl_rank ** 2)]
    letter_index = 0
    for row in key_tbl:
        part_tbl = []
        for clm in row:
            part_tbl.append(enc_msg[letter_index])
            msg[clm - 1] = enc_msg[letter_index]
            letter_index += 1
        tbl.append(part_tbl)
    return {'msg': ''.join(msg), 'enc_table': tbl}


if __name__ == '__main__':
    print(enc_magic_square('ПРИЛЕТАЮ ВОСЬМОГО', [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]))
    print(dec_magic_square('ОИРМЕОСЮВТАЬЛГОП', [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]))
