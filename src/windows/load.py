from PyQt5 import QtWidgets, QtGui

from src.components import dialogs
from . import messages, main_window
from src.views import load_win


class LoadWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.__is_complete = False

    def set_is_complete(self, is_complete):
        self.__is_complete = is_complete

    def closeEvent(self, event):
        if not self.__is_complete:
            result = dialogs.question_msg_result(messages.CONFIRM_QUIT_LOAD, 'Подтверждение выхода')
            event.ignore()
            if result:
                event.accept()
        else:
            event.accept()


def complete_load(form, main_form):
    form.set_is_complete(True)
    form.close()
    main_window.show_main_window(main_form)


def to_load_page(form_ui, page_index):
    form_ui.load_wgt.setCurrentIndex(page_index)


def enable_visual_styles(form_ui):
    movie = QtGui.QMovie('../resources/images/lock.gif')
    form_ui.lock_lbl.setMovie(movie)
    movie.start()


def init_load_pages(form, form_ui, main_form):
    form_ui.btn_skip_load.clicked.connect(lambda: complete_load(form, main_form))
    form_ui.btn_start_load.clicked.connect(lambda: to_load_page(form_ui, 1))


def show_load_window(main_form):
    load_window = LoadWindow()
    load_window.setFixedSize(1050, 650)
    ui = load_win.Ui_load_form()
    ui.setupUi(load_window)
    enable_visual_styles(ui)
    init_load_pages(load_window, ui, main_form)
    load_window.show()
