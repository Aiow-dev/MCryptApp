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
    theme = setting.app_theme()
    if theme == 'system':
        is_light = win.is_light_win_theme()
        ui = main_win_dark.Ui_main_window()
        if is_light:
            ui = main_win_light.Ui_main_window()
        ui.setupUi(MainWindow)
        main_window.init_win_styles(is_light, ui)
    elif theme == 'time':
        current_hour = time.get_current_hour()
        time_theme = 'dark'
        ui = main_win_dark.Ui_main_window()
        if 5 < current_hour < 18:
            time_theme = 'light'
            ui = main_win_light.Ui_main_window()
        ui.setupUi(MainWindow)
        main_window.init_styles(time_theme, ui)
    else:
        ui = main_win_dark.Ui_main_window()
        if theme == 'light':
            ui = main_win_light.Ui_main_window()
        ui.setupUi(MainWindow)
        main_window.init_styles(theme, ui)
    MainWindow.show()
    main_window.init_pages(ui)
    page.init_page(ui)
    menu.init_menu(MainWindow, ui)
    sys.exit(app.exec_())
