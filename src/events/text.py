from src.events import messages
from src.helpers import styles


def check_empty(text_obj, color_default, color_err):
    color = color_default
    msg = ''
    text = text_obj.text()
    if text.isspace() or text == '':
        color = color_err
        msg = messages.EMPTY_ERR
    styles.set_border_color(text_obj, color)
    text_obj.setToolTip(msg)


def check_positive_number(text_obj, color_default, color_err):
    color = color_err
    msg = messages.POS_NUM_ERR
    try:
        num = int(text_obj.text())
        if num > 0:
            color = color_default
            msg = ''
        styles.set_border_color(text_obj, color)
        text_obj.setToolTip(msg)
    except ValueError:
        styles.set_border_color(text_obj, color)
        text_obj.setToolTip(msg)


def check_digit(text_obj, color_default, color_err):
    color = color_default
    msg = ''
    if not text_obj.text().isdigit():
        color = color_err
        msg = messages.DIGIT_ERROR
    styles.set_border_color(text_obj, color)
    text_obj.setToolTip(msg)


def check_chars_ign(text_obj, charset, color_default, color_err):
    text = text_obj.text().lower()
    check_chars = charset.lower()
    color = color_err
    msg = messages.CHARSET_ERROR.format(charset)
    is_charset = True
    if not text:
        styles.set_border_color(text_obj, color)
        text_obj.setToolTip(msg)
        return
    for symbol in text:
        if symbol not in check_chars:
            is_charset = False
            break
    if is_charset:
        color = color_default
        msg = ''
    styles.set_border_color(text_obj, color)
    text_obj.setToolTip(msg)
