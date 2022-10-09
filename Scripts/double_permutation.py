def enc_double_permutation(msg, row, clm, key_row, key_clm):
    msg = msg.replace(' ', '').upper()

    if len(msg) != row * clm:
        return 'Ошибка заполнения таблицы. Проверьте количество строк и столбцов'

    table = []
    index_letter = 0

    for _ in range(row):
        part_letter_table = []

        for _ in range(clm):
            part_letter_table.append(msg[index_letter])
            index_letter += 1

        table.append(part_letter_table)

    clm_table = {}

    for index_clm, num_clm in enumerate(key_clm):
        part_clm_table = [table[index_row][index_clm] for index_row in range(row)]

        clm_table[num_clm] = part_clm_table

    sort_key_clm = sorted(clm_table)
    sort_clm_table = list({sort_key: clm_table[sort_key] for sort_key in sort_key_clm}.values())

    row_table = {}

    for index_row, num_row in enumerate(key_row):
        part_row_table = [sort_clm_table[index_clm][index_row] for index_clm in range(clm)]

        row_table[num_row] = part_row_table

    sort_key_row = sorted(row_table)
    sort_row_table = list({sort_key: row_table[sort_key] for sort_key in sort_key_row}.values())

    return ''.join(''.join(sort_row) for sort_row in sort_row_table)


def test_enc_double_permutation(msg, row, clm, key_row, key_clm):
    msg = msg.replace(' ', '').upper()

    if len(msg) != row * clm:
        return 'Ошибка заполнения таблицы. Проверьте количество строк и столбцов'

    clm_table = {}

    for index_clm, num_clm in enumerate(key_clm):
        part_clm_table = []

        for index_row in range(row):
            offset = index_row * clm + index_clm
            part_clm_table.append(msg[offset])

        clm_table[num_clm] = part_clm_table

    sort_clm_table = [clm_table[sort_key] for sort_key in sorted(clm_table)]

    row_table = {}

    for index_row, num_row in enumerate(key_row):
        part_row_table = [sort_clm_table[index_clm][index_row] for index_clm in range(clm)]

        row_table[num_row] = part_row_table

    sort_row_table = [row_table[sort_key] for sort_key in sorted(row_table)]

    return ''.join(''.join(sort_row) for sort_row in sort_row_table)


def dec_double_permutation(enc_msg, row, clm, key_row, key_clm):
    enc_msg = enc_msg.replace(' ', '').upper()

    if len(enc_msg) != row * clm:
        return 'Ошибка заполнения таблицы. Проверьте количество строк и столбцов'

    clm_table = {}

    for index_clm, num_clm in enumerate(key_clm):
        part_clm_table = []

        for index_row in range(row):
            offset = index_row * clm + index_clm
            part_clm_table.append(enc_msg[offset])

        clm_table[str(index_clm + 1)] = part_clm_table

    clm_table_key = [clm_table[key] for key in key_clm]

    row_table = {}

    for index_row, num_row in enumerate(key_row):
        part_row_table = [clm_table_key[index_clm][index_row] for index_clm in range(clm)]

        row_table[str(index_row + 1)] = part_row_table

    row_table_key = [row_table[key] for key in key_row]

    return ''.join(''.join(part_row) for part_row in row_table_key)


if __name__ == '__main__':
    print(test_enc_double_permutation('ПРИЛЕТАЮ СЕДЬМОГО', 4, 4, '3142', '4132'))
    print(test_enc_double_permutation('ВРЕМЕНАЪМЕНЯЮТСЯ', 4, 4, '2341', '4321'))
    print(dec_double_permutation('ТЮАЕООГМРЛИПЕЬДС', 4, 4, '3142', '4132'))
    print(dec_double_permutation('ЯСТЮМЕРВЪАНЕЯНЕМ', 4, 4, '2341', '4321'))
    print(dec_double_permutation('КВЯААСАЪЪВЪДЪАВЧ', 4, 4, '1342', '3214'))
