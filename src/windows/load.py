from PyQt5 import QtWidgets, QtGui

from src.components import dialogs, setting, visual
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


def start_load_page(form_ui):
    form_ui.load_wgt.setCurrentIndex(0)


def color_styles_page(form_ui):
    form_ui.load_wgt.setCurrentIndex(1)


def set_light_style(form_ui):
    form_ui.light_style_lbl.setText('Светлая (Выбрано)')
    form_ui.dark_style_lbl.setText('Темная')
    form_ui.system_style_lbl.setText('Системная')
    form_ui.time_style_lbl.setText('Временная')
    setting.set_parameter('theme', 'light')


def set_dark_style(form_ui):
    form_ui.light_style_lbl.setText('Светлая')
    form_ui.dark_style_lbl.setText('Темная (Выбрано)')
    form_ui.system_style_lbl.setText('Системная')
    form_ui.time_style_lbl.setText('Временная')
    setting.set_parameter('theme', 'dark')


def set_system_style(form_ui):
    form_ui.light_style_lbl.setText('Светлая')
    form_ui.dark_style_lbl.setText('Темная')
    form_ui.system_style_lbl.setText('Системная (Выбрано)')
    form_ui.time_style_lbl.setText('Временная')
    setting.set_parameter('theme', 'system')


def set_time_style(form_ui):
    form_ui.light_style_lbl.setText('Светлая')
    form_ui.dark_style_lbl.setText('Темная')
    form_ui.system_style_lbl.setText('Системная')
    form_ui.time_style_lbl.setText('Временная (Выбрано)')
    setting.set_parameter('theme', 'time')


def enable_visual_styles(form_ui):
    lock_movie = QtGui.QMovie('../resources/images/lock.gif')
    form_ui.lock_lbl.setMovie(lock_movie)
    lock_movie.start()
    roller_brush_movie = QtGui.QMovie('../resources/images/roller_brush.gif')
    form_ui.label_2.setMovie(roller_brush_movie)
    roller_brush_movie.start()
    visual.frame_compl_color_style_sys(form_ui.compl_light_win_color)
    visual.frame_compl_color_style_sys(form_ui.compl_dark_win_color)
    visual.frame_color_style_sys(form_ui.accent_light_win_color)
    visual.frame_color_style_sys(form_ui.accent_dark_win_color)


def init_load_pages(form, form_ui, main_form):
    form_ui.btn_skip_load.clicked.connect(lambda: complete_load(form, main_form))
    form_ui.btn_back_style.clicked.connect(lambda: start_load_page(form_ui))
    form_ui.btn_start_load.clicked.connect(lambda: color_styles_page(form_ui))
    form_ui.light_style_btn.clicked.connect(lambda: set_light_style(form_ui))
    form_ui.dark_style_btn.clicked.connect(lambda: set_dark_style(form_ui))
    form_ui.system_style_btn.clicked.connect(lambda: set_system_style(form_ui))
    form_ui.time_style_btn.clicked.connect(lambda: set_time_style(form_ui))


def show_load_window(main_form):
    load_window = LoadWindow()
    load_window.setFixedSize(1050, 650)
    ui = load_win.Ui_load_form()
    ui.setupUi(load_window)
    enable_visual_styles(ui)
    init_load_pages(load_window, ui, main_form)
    load_window.show()
