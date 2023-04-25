from events import text, action
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
