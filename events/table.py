from events import messages


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
