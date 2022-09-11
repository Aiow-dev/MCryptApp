import math


def Vidjiner(message, key):       #"Работа", "труд"
    message = message.lower()     # вывод грфтер
    table = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    big_table = []

    if not key:
        return 'Ключ не может быть пустым'

    shifr_table = key * math.ceil(len(message) // len(key))
    shifr_table += key
    for i in range(0,33):
        big_table.append(table)
        table = table[1::] + table[0]
    shifr = ''
    counter = 0
    for i in range(0,len(message)):
        if message[i] not in table:
            shifr += message[i]
        else:
            shifr += big_table[table.find(message[i])][table.find(shifr_table[counter])]
            counter += 1
    return shifr, big_table


if __name__ == '__main__':
    print(Vidjiner('прилетаю десятого', ''))

