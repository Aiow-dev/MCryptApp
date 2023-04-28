from events import text, action, table, event_helpers
from components import colors
from helpers import time


def empty_text_changed(text_obj):
    text_obj.textChanged.connect(
        lambda: text.check_empty(text_obj, colors.Color.dark_charcoal, colors.Color.orange_red))


def positive_number_text_changed(text_obj):
    text_obj.textChanged.connect(
        lambda: text.check_positive_number(text_obj, colors.Color.dark_charcoal, colors.Color.orange_red))


def shortcut_return(ui_obj):
    action.set_shortcut(ui_obj, 'Return')


def digit_text_changed(text_obj):
    text_obj.textChanged.connect(
        lambda: text.check_digit(text_obj, colors.Color.dark_charcoal, colors.Color.orange_red))


def time_chars_ign_text_changed(text_obj, charset, delay):
    timer = time.TimerDelay(delay, lambda: text.check_chars_ign(text_obj, charset, colors.Color.dark_charcoal,
                                                                colors.Color.orange_red))
    text_obj.textChanged.connect(lambda: timer.update())


def tbl_rank_text_changed(text_obj, tbl_obj, max_limit):
    text_obj.textChanged.connect(lambda: action.set_tbl_rank(tbl_obj, text_obj, max_limit))


def tbl_pos_num_item_changed(tbl_obj):
    tbl_obj.itemChanged.connect(
        lambda item: table.check_tbl_pos_num(item, colors.ColorSet.eerie_black.value.to_rgb_q(),
                                             colors.ColorSet.orange_red.value.to_rgb_q()))


def tables_row_text_changed(tables, text_obj, max_limit):
    text_obj.textChanged.connect(lambda: event_helpers.set_tables_row_text_changed(tables, text_obj, max_limit))


def tables_clm_text_changed(tables, text_obj, max_limit):
    text_obj.textChanged.connect(lambda: event_helpers.set_tables_clm_text_changed(tables, text_obj, max_limit))


def tables_rand_state_changed(tables, check_obj, charset):
    check_obj.stateChanged.connect(lambda: event_helpers.set_tables_rand_state_changed(tables, check_obj, charset))


def table_size_charset_state_changed(tbl_obj, check_obj, charset):
    check_obj.stateChanged.connect(
        lambda: action.tbl_size_charset(check_obj, tbl_obj.rowCount(), tbl_obj.columnCount(), charset))


def tbl_char_unique_item_changed(tbl_obj):
    tbl_obj.itemChanged.connect(
        lambda item: table.check_tbl_char_unique(tbl_obj, item, colors.ColorSet.eerie_black.value.to_rgb_q(),
                                                 colors.ColorSet.orange_red.value.to_rgb_q()))
