from src.events import event_helpers, action, text, table
from src.components import visual_colors
from src.helpers import time


def empty_text_changed(text_obj):
    text_obj.textChanged.connect(
        lambda: text.check_empty(text_obj, visual_colors.dark_charcoal, visual_colors.light_red))


def positive_number_text_changed(text_obj):
    text_obj.textChanged.connect(
        lambda: text.check_positive_number(text_obj, visual_colors.dark_charcoal, visual_colors.light_red))


def number_text_changed(text_obj):
    text_obj.textChanged.connect(
        lambda: text.check_number(text_obj, visual_colors.dark_charcoal, visual_colors.light_red))


def digit_text_changed(text_obj):
    text_obj.textChanged.connect(
        lambda: text.check_digit(text_obj, visual_colors.dark_charcoal, visual_colors.light_red))


def time_chars_ign_text_changed(text_obj, charset, delay):
    timer = time.TimerDelay(delay, lambda: text.check_chars_ign(text_obj, charset, visual_colors.dark_charcoal,
                                                                visual_colors.light_red))
    text_obj.textChanged.connect(lambda: timer.update())


def tbl_rank_text_changed(text_obj, tbl_obj, max_limit):
    text_obj.textChanged.connect(lambda: action.set_tbl_rank(tbl_obj, text_obj, max_limit))


def tbl_row_text_changed(text_obj, tbl_obj, max_limit):
    text_obj.textChanged.connect(lambda: action.set_tbl_row(tbl_obj, text_obj, max_limit))


def tbl_column_text_changed(text_obj, tbl_obj, max_limit):
    text_obj.textChanged.connect(lambda: action.set_tbl_clm(tbl_obj, text_obj, max_limit))


def tbl_pos_num_item_changed(tbl_obj, color_default, color_err):
    tbl_obj.itemChanged.connect(
        lambda item: table.check_tbl_pos_num(item, color_default, color_err))


def tables_row_text_changed(tables, text_obj, max_limit):
    text_obj.textChanged.connect(lambda: event_helpers.set_tables_row_text_changed(tables, text_obj, max_limit))


def tables_clm_text_changed(tables, text_obj, max_limit):
    text_obj.textChanged.connect(lambda: event_helpers.set_tables_clm_text_changed(tables, text_obj, max_limit))


def tables_rand_state_changed(tables, check_obj, charset):
    check_obj.stateChanged.connect(lambda: event_helpers.set_tables_rand_state_changed(tables, check_obj, charset))


def tbl_size_charset_state_changed(tbl_obj, check_obj, charset):
    check_obj.stateChanged.connect(
        lambda: action.tbl_size_charset(check_obj, tbl_obj.rowCount(), tbl_obj.columnCount(), charset))


def tbl_char_unique_item_changed(tbl_obj, color_default, color_err):
    tbl_obj.itemChanged.connect(
        lambda item: table.check_tbl_char_unique(tbl_obj, item, color_default, color_err))
