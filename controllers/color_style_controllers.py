from components import dialogs, setting
from controllers import messages


def light_color_style():
    dialogs.show_info_msg(messages.ON_LIGHT_THEME, 'Информация')
    setting.set_parameter('theme', 'light')


def dark_color_style():
    dialogs.show_info_msg(messages.ON_DARK_THEME, 'Информация')
    setting.set_parameter('theme', 'dark')


def system_color_style():
    dialogs.show_info_msg(messages.ON_SYSTEM_THEME, 'Информация')
    setting.set_parameter('theme', 'system')


def time_color_style():
    dialogs.show_info_msg(messages.ON_TIME_THEME, 'Информация')
    setting.set_parameter('theme', 'time')


def init_color_styles(ui):
    ui.light_btn.clicked.connect(light_color_style)
    ui.dark_btn.clicked.connect(dark_color_style)
    ui.win_btn.clicked.connect(system_color_style)
    ui.time_color_btn.clicked.connect(time_color_style)
