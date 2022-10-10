def remove_item(item_value, list_obj):
    if item_value in list_obj:
        list_obj.remove(item_value)


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
