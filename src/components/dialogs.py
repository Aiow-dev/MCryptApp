from PyQt5 import QtWidgets

from . import visual, setting, dialogs_styles
from src.helpers import win, time


def init_visual_dialogs():
    theme = setting.get_parameter('theme')
    style = visual.msg_box_dark()
    if theme == 'system':
        is_light = win.is_light_win_theme()
        style = visual.msg_box_dark_sys()
        if is_light:
            style = visual.msg_box_light_sys()
    elif theme == 'time':
        current_hour = time.get_current_hour()
        if 5 < current_hour < 18:
            style = visual.msg_box_light()
    else:
        if theme == 'light':
            style = visual.msg_box_light()
    dialogs_styles.msg_box_style = style


def show_err_msg(txt, title):
    msg = QtWidgets.QMessageBox()
    msg.setText(txt)
    msg.setWindowTitle(title)
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setStyleSheet(dialogs_styles.msg_box_style)
    msg.exec()


def show_info_msg(txt, title):
    msg = QtWidgets.QMessageBox()
    msg.setText(txt)
    msg.setWindowTitle(title)
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setStyleSheet(dialogs_styles.msg_box_style)
    msg.exec()


def question_msg_result(txt, title):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setIcon(QtWidgets.QMessageBox.Question)
    msg_box.setWindowTitle(title)
    msg_box.setText(txt)
    msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
    msg_box.setStyleSheet(dialogs_styles.msg_box_style)
    msg_box.exec_()
    return msg_box.clickedButton().text() == '&Да'
