from datetime import datetime

from PyQt5 import QtCore


def get_current_hour():
    current_datetime = datetime.now()
    return current_datetime.hour


def block_element_time(ui_obj, time):
    ui_obj.setEnabled(False)
    QtCore.QTimer.singleShot(time, lambda: ui_obj.setDisabled(False))


class TimerDelay:
    def __init__(self, time, timeout_func):
        self.__time = time
        self.__timeout_func = timeout_func
        self.__executor_timer = QtCore.QTimer()
        self.__executor_timer.setSingleShot(True)
        self.__executor_timer.timeout.connect(lambda: self._timeout_execute())

    def update(self):
        self.__executor_timer.start(self.__time)

    def _timeout_execute(self):
        self.__timeout_func()
