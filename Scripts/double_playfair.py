from Scripts.base_scripts import find


def enc_double_playfair(msg, left_tbl, right_tbl):
    len_msg = len(msg)

    left_size = len(left_tbl), len(left_tbl[0])
    right_size = len(right_tbl), len(right_tbl[0])

    if len_msg % 2 == 1:
        msg += 'Ъ'

    if left_size[0] != right_size[0] and left_size[1] != right_size[1]:
        return 'Ошибка. Возможно, размерности таблиц не равны'

    enc_msg = ''

    for i in range(0, len_msg, 2):
        first = find(left_tbl, msg[i], left_size[0], left_size[1])
        second = find(right_tbl, msg[i + 1], right_size[0], right_size[1])

        if not first or not second:
            return 'Ошибка. Возможно, не найдена буква сообщения в таблице подстановок'

        if first[0] == second[0]:
            enc_msg += right_tbl[first[0]][first[1]]
            enc_msg += left_tbl[second[0]][second[1]]
        else:
            enc_msg += right_tbl[first[0]][second[1]]
            enc_msg += left_tbl[second[0]][first[1]]

    return enc_msg


def dec_double_playfair(enc_msg, left_tbl, right_tbl):
    len_msg = len(enc_msg)

    left_size = len(left_tbl), len(left_tbl[0])
    right_size = len(right_tbl), len(right_tbl[0])

    if len_msg % 2 == 1:
        enc_msg += 'Ъ'

    if left_size[0] != right_size[1] and left_size[1] != right_size[1]:
        return 'Ошибка. Возможно, размерности таблиц не равны'

    msg = ''

    for i in range(0, len_msg, 2):
        first = find(right_tbl, enc_msg[i], left_size[0], left_size[1])
        second = find(left_tbl, enc_msg[i + 1], right_size[0], right_size[1])

        if not first or not second:
            return 'Ошибка. Возможно, не найдена буква сообщения в таблице подстановок'

        if first[0] == second[0]:
            msg += left_tbl[first[0]][first[1]]
            msg += right_tbl[second[0]][second[1]]
        else:
            msg += left_tbl[first[0]][second[1]]
            msg += right_tbl[second[0]][first[1]]

    return msg


if __name__ == '__main__':
    left_table = [['Ж', 'Щ', 'Н', 'Ю', 'Р'],
                  ['И', 'Т', 'Ь', 'Ц', 'Б'],
                  ['Я', 'М', 'Е', '.', 'С'],
                  ['В', 'Ы', 'П', 'Ч', ' '],
                  [':', 'Д', 'У', 'О', 'К'],
                  ['З', 'Э', 'Ф', 'Г', 'Ш'],
                  ['Х', 'А', ',', 'Л', 'Ъ']]

    right_table = [['И', 'Ч', 'Г', 'Я', 'Т'],
                   [',', 'Ж', 'Ь', 'М', 'О'],
                   ['З', 'Ю', 'Р', 'В', 'Щ'],
                   ['Ц', ':', 'П', 'Е', 'Л'],
                   ['Ъ', 'А', 'Н', '.', 'Х'],
                   ['Э', 'К', 'С', 'Ш', 'Д'],
                   ['Б', 'Ф', 'У', 'Ы', ' ']]

    encryption_message = enc_double_playfair('ПРИЛЕТАЮ ШЕСТОГО', left_table, right_table)
    print(f'{encryption_message=}')

    message = dec_double_playfair(encryption_message, left_table, right_table)
    print(f'{message}')
