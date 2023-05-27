import sys

from PyQt5 import QtCore, QtWidgets

from src.components import dialogs, setting, win_palette


def enable_visual_styles():
    accent = win_palette.win_accent_converted()
    complementary = win_palette.win_complementary_converted(accent)
    win_palette.accent_color = accent.to_rgb_str()
    win_palette.complementary_color = complementary.to_rgb_str()
    dialogs.init_visual_dialogs()


def restart():
    QtCore.QCoreApplication.quit()
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv)


def quit_confirm(parent):
    if setting.get_parameter('confirm-quit'):
        if dialogs.question_msg_result(
                'Вы уверены, что хотите выйти? Все несохраненные изменения будут утеряны!',
                'Подтверждение выхода...'
        ):
            QtWidgets.qApp.quit()
    else:
        QtWidgets.qApp.quit()


def restart_confirm(parent):
    if setting.get_parameter('confirm-quit'):
        if dialogs.question_msg_result(
                'Вы уверены, что хотите выйти? Все несохраненные изменения будут утеряны!',
                'Подтверждение выхода...',
        ):
            restart()
    else:
        restart()
