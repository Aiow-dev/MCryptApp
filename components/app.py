import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets

from components import dialogs, setting


def restart():
    QtCore.QCoreApplication.quit()
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv)


def quit_confirm(parent):
    is_confirm_quit = setting.is_confirm_quit()
    if is_confirm_quit:
        result = dialogs.question_msg(parent,
                                      'Вы уверены, что хотите выйти? Все несохраненные изменения будут утеряны!',
                                      'Подтверждение выхода...')
        if result:
            QtWidgets.qApp.quit()
    else:
        QtWidgets.qApp.quit()


def restart_confirm(parent):
    is_confirm_quit = setting.is_confirm_quit()
    if is_confirm_quit:
        result = dialogs.question_msg(parent,
                                      'Вы уверены, что хотите выйти? Все несохраненные изменения будут утеряны!',
                                      'Подтверждение выхода...')
        if result:
            restart()
    else:
        restart()
