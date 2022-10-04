def remove_item(item_value, list_obj):
    if item_value in list_obj:
        list_obj.remove(item_value)


def all_equal(items):
    len_items = len(items)

    for current_index in range(len_items):
        if items[current_index] != items[current_index - 1]:
            return False

    return True
