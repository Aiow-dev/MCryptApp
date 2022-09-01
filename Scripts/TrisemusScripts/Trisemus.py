def Trisemus(message, key_word, size_a = 4, size_b = 8):# «ПРИЛЕТАЮ ЗАВТРА», "работа"
    message = message.lower()                           # Вывод: ЩЕУЦНЙЖГ СЖКЙЕЖ
    table_alfabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    shifr_table = ''
    shifr_table = sum(key_word, shifr_table)
    shifr_table = sum(table_alfabet, shifr_table)
    table = [[0] * size_b for i in range(size_a)]
    counter = 0
    shifr = ''
    for i in range(0,size_a):
        for j in range(0, size_b):
            table[i][j] = shifr_table[counter % 32]
            counter += 1
    for i in message:
        if i not in table_alfabet:
            shifr += i
        else:
            first = find(table, i,size_a,size_b)
            shifr += table[(first[0] + 1) % len(table)][first[1]]
    return shifr, table


def sum(string, table):
    for i in string:
        if table.find(i) == -1:
            table += i
    return table


def find(table, el, size_a, size_b):
    for i in range(0, size_a):
        for j in range(0, size_b):
            if table[i][j] == el:
                return [i, j]


if __name__ == '__main__':
    print(Trisemus('ПРИЛЕТАЮ ЗАВТРА', 'работа', 4, 8))
