def remove_item(item_value, list_obj):
    if item_value in list_obj:
        list_obj.remove(item_value)


def all_equal(items):
    len_items = len(items)

    return all(items[index] == items[index - 1] for index in range(len_items))
