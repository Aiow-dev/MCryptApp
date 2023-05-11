from components import dialogs, setting
from controllers import messages


def corner_tab_style():
    dialogs.show_info_msg(messages.ON_CORNER_STYLE, 'Информация')
    setting.set_parameter('tab-style', 'corner')


def radius_tab_style():
    dialogs.show_info_msg(messages.ON_RADIUS_STYLE, 'Информация')
    setting.set_parameter('tab-style', 'radius')


def top_radius_tab_style():
    dialogs.show_info_msg(messages.ON_TOP_RADIUS_STYLE, 'Информация')
    setting.set_parameter('tab-style', 'top-radius')


def corner_radius_tab_style():
    dialogs.show_info_msg(messages.ON_CORNER_RADIUS_STYLE, 'Информация')
    setting.set_parameter('tab-style', 'corner-radius')


def init_tab_style(ui):
    ui.tab_corner_btn.clicked.connect(corner_tab_style)
    ui.tab_radius_btn.clicked.connect(radius_tab_style)
    ui.tab_top_radius_btn.clicked.connect(top_radius_tab_style)
    ui.tab_corner_radius_btn.clicked.connect(corner_radius_tab_style)
