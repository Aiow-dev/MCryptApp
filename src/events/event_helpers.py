from src.events import action


def set_tables_row_text_changed(tables, text_obj, max_limit):
    for table in tables:
        action.set_tbl_row(table, text_obj, max_limit)


def set_tables_clm_text_changed(tables, text_obj, max_limit):
    for table in tables:
        action.set_tbl_clm(table, text_obj, max_limit)


def set_tables_rand_state_changed(tables, check_obj, charset):
    for table in tables:
        action.set_rand_tbl(table, check_obj, charset)
