import sys

from PyQt5 import QtWidgets

from views import main_win_dark, main_win_light
from controllers import page, menu
from components import setting
from helpers import win, time
from windows import main_window


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = main_window.MainWindowApp()
    theme = setting.get_parameter('theme')
    tab_style = setting.get_parameter('tab-style')
    if theme == 'system':
        is_light = win.is_light_win_theme()
        ui = main_win_dark.Ui_main_window()
        if is_light:
            ui = main_win_light.Ui_main_window()
        ui.setupUi(MainWindow)
        main_window.init_win_styles(is_light, ui)
        main_window.init_sys_tab_styles(is_light, tab_style, ui)
    elif theme == 'time':
        current_hour = time.get_current_hour()
        time_theme = 'dark'
        ui = main_win_dark.Ui_main_window()
        if 5 < current_hour < 18:
            time_theme = 'light'
            ui = main_win_light.Ui_main_window()
        ui.setupUi(MainWindow)
        main_window.init_styles(time_theme, ui)
        main_window.init_tab_styles(time_theme, tab_style, ui)
    else:
        ui = main_win_dark.Ui_main_window()
        if theme == 'light':
            ui = main_win_light.Ui_main_window()
        ui.setupUi(MainWindow)
        main_window.init_styles(theme, ui)
        main_window.init_tab_styles(theme, tab_style, ui)
    main_window.init_elements(ui)
    MainWindow.show()
    main_window.init_pages(ui)
    page.init_page(ui)
    menu.init_menu(MainWindow, ui)
    sys.exit(app.exec_())
