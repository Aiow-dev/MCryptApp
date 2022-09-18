def enc_simple_permutation(msg, row, column):  # Шифруемая фраза "Прилетаю седьмого в полдень"
    msg = msg.replace(' ', '').upper()  # Строки - 4, Столбцы - 6 Результат - "ПЕСМВДРТЕОПЕИАДГОНЛЬЮОЛЬ"

    if len(msg) != row * column or row <= 0 or column <= 0:
        return "Ошибка заполнения таблицы. Проверьте количество строк и столбцов"

    mas = [[] for _ in range(row)]

    index = -1

    for j in range(column):
        for i in range(row):
            index += 1
            mas[i].insert(j, msg[index])

    enc_msg = ""

    for i in range(row):
        for j in range(column):
            enc_msg += mas[i][j]

    return enc_msg, mas


def dec_simple_permutation(enc_msg, row, column):  # Строка - "ПЕСМВДРТЕОПЕИАДГОНЛЮЬОЛЬ"
    enc_msg = enc_msg.replace(' ', '').upper()  # Строки - 4, Столбцы - 6 Результат - "ПРИЛЕТАЮСЕДЬМОГОВПОЛДЕНЬ"

    if len(enc_msg) != row * column or row <= 0 or column <= 0:
        return "Ошибка заполнения таблицы. Проверьте количество строк и столбцов"

    mas = [[] for _ in range(row)]

    index = -1

    for j in range(row):
        for i in range(column):
            index += 1
            mas[j].insert(i, enc_msg[index])

    msg = ""

    for i in range(column):
        for j in range(row):
            msg += mas[j][i]

    return msg, mas
