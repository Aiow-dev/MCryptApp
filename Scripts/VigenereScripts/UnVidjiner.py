import math


def UnVidjiner(shifr, key):    # "оыэкиы", "труд"  # вывод работа
    shifr = shifr.lower()
    table = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    big_table = []
    shifr_table = key * math.ceil(len(shifr) // len(key))
    shifr_table += key
    for i in range(0,33):
        big_table.append(table)
        table = table[1::] + table[0]
    message = ''
    counter = 0
    for i in range(0,len(shifr)):
        if shifr[i] not in table:
            message += shifr[i]
        else:
            position = big_table[table.find(shifr_table[counter])].find(shifr[i])
            message += table[position]
            counter += 1
    return message, big_table
