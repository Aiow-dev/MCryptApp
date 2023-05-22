from src.events import messages
from src.helpers import tables


def check_tbl_pos_num(tbl_item_obj, color_default, color_err):
    color = color_err
    msg = messages.TBL_POS_NUM_ERROR
    try:
        num = int(tbl_item_obj.text())
        if num > 0:
            color = color_default
            msg = ''
        tbl_item_obj.setBackground(color)
        tbl_item_obj.setToolTip(msg)
    except ValueError:
        tbl_item_obj.setBackground(color)
        tbl_item_obj.setToolTip(msg)


def check_tbl_char_unique(tbl_obj, tbl_item_obj, color_default, color_err):
    color = color_err
    msg = messages.TBL_CHAR_UNIQUE_ERROR
    tbl_item = tbl_item_obj.text().upper()
    tbl_items = ''.join(''.join(row) for row in tables.table_up_items(tbl_obj))
    item_count = tbl_items.count(tbl_item)
    if len(tbl_item) == 1 and item_count <= 1:
        color = color_default
        msg = ''
    tbl_item_obj.setBackground(color)
    tbl_item_obj.setToolTip(msg)
