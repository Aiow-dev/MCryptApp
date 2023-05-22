import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from src.components import dialogs, setting


def restart():
    QtCore.QCoreApplication.quit()
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv)


def quit_confirm(parent):
    if setting.get_parameter('confirm-quit'):
        if dialogs.question_msg(
                parent,
                'Вы уверены, что хотите выйти? Все несохраненные изменения будут утеряны!',
                'Подтверждение выхода...'
        ):
            QtWidgets.qApp.quit()
    else:
        QtWidgets.qApp.quit()


def restart_confirm(parent):
    if setting.get_parameter('confirm-quit'):
        if dialogs.question_msg(
                parent,
                'Вы уверены, что хотите выйти? Все несохраненные изменения будут утеряны!',
                'Подтверждение выхода...',
        ):
            restart()
    else:
        restart()
