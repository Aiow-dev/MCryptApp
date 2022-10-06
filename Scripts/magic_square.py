from typing import List

from Utils.item_utils import all_equal


def check_magic_square(magic_square):
    row_len = len(magic_square)
    clm_len = len(magic_square[0])

    if row_len != clm_len:
        return False

    sums_row = []
    sums_clm = []

    sum_left_diagonal = 0
    sum_right_diagonal = 0

    for row_index in range(row_len):
        sum_row = 0
        sum_clm = 0

        for clm_index in range(clm_len):
            if not magic_square[row_index][clm_index]:
                return False

            sum_row += magic_square[row_index][clm_index]
            sum_clm += magic_square[clm_index][row_index]

            if row_index == clm_index:
                sum_left_diagonal += magic_square[row_index][clm_index]

            if row_index + clm_index == clm_len - 1:
                sum_right_diagonal += magic_square[row_index][clm_index]

        sums_row.append(sum_row)
        sums_clm.append(sum_clm)

    if not all_equal(sums_row) and not all_equal(sums_clm):
        return False

    return sum_left_diagonal == sum_right_diagonal


def enc_magic_square(msg: str, key_table: List[List[int]]) -> str | tuple[str, list[list[str]]]:
    if not check_magic_square(key_table):
        return 'Ошибка. Таблица не является магическим квадратом'

    table: List[List[str]] = []

    enc_msg: str = ''

    for row in key_table:
        part_table: List[str] = []

        for clm in row:
            part_table.append(msg[clm - 1])
            enc_msg += msg[clm - 1]

        table.append(part_table)

    return enc_msg, table


def dec_magic_square(enc_msg: str, key_table: List[List[int]]):
    if not check_magic_square(key_table):
        return 'Ошибка. Таблица не является магическим квадратом'

    table_rank = len(key_table)

    table: List[List[str]] = []

    msg = ['' for _ in range(table_rank ** 2)]

    letter_index = 0

    for row in key_table:
        part_table: List[str] = []

        for clm in row:
            part_table.append(enc_msg[letter_index])
            msg[clm - 1] = enc_msg[letter_index]

            letter_index += 1

        table.append(part_table)

    return ''.join(msg), table


if __name__ == '__main__':
    print(enc_magic_square('ПРИЛЕТАЮ ВОСЬМОГО', [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]))
    print(dec_magic_square('ОИРМЕОСЮВТАЬЛГОП', [[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12], [4, 15, 14, 1]]))
