from PyQt5 import QtWidgets

from src.controllers import menu, page
from src.windows import main_window


def init_window(window):
    ui = main_window.enable_visual_styles(window)
    main_window.init_pages(ui)
    page.init_page(ui)
    menu.init_menu_add(ui)


def show_addition_window(parent):
    form = QtWidgets.QMainWindow(parent)
    init_window(form)
    form.show()
