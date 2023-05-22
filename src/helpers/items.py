import math

from src.helpers import tables


def remove_item(item_value, lst):
    if item_value in lst:
        lst.remove(item_value)


def range_to_str(range_obj):
    return ''.join(str(index) for index in range_obj)


def all_equal(items):
    len_items = len(items)
    return all(items[index] == items[index - 1] for index in range(len_items))


def is_serial(lst, step=1):
    len_lst = len(lst)
    return all(lst[index] - lst[index - 1] == step for index in range(1, len_lst))


def is_all_range(txt, range_obj):
    range_txt = range_to_str(range_obj)
    if len(txt) != len(range_txt) or len(set(txt)) != len(range_txt):
        return False
    return all(i in range_txt for i in txt)


def get_multipliers(number):
    multipliers = []
    multiplier = 2
    max_multiplier = math.floor(number / 2)
    while number > 1:
        if number % multiplier == 0:
            number = number // multiplier
            multipliers.append(multiplier)
            multiplier = 2
        elif multiplier > max_multiplier:
            break
        else:
            multiplier += 1
    return multipliers


def couple_multipliers(multipliers):
    part_len = math.ceil(len(multipliers) / 2)
    part_left = multipliers[:part_len]
    part_right = multipliers[part_len:]
    couple_left = 1
    for part in part_left:
        couple_left *= part
    couple_right = 1
    for part in part_right:
        couple_right *= part
    return couple_left, couple_right


def table_str_items(table):
    table_text = []
    for row in table:
        part_row = [str(column) for column in row]
        table_text.append(part_row)
    return table_text


def is_empty_table(tbl_wgt):
    size = tables.table_size(tbl_wgt)
    for row in range(size[0]):
        for column in range(size[1]):
            item_obj = tbl_wgt.item(row, column)
            if item_obj is not None:
                return False
    return True


if __name__ == '__main__':
    multipliers_couple = get_multipliers(20)
    print(couple_multipliers(multipliers_couple))
