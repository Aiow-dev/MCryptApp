from src.components import dialogs, setting
from src.controllers import messages


def menu_line_check(parent, check_obj):
    if check_obj.isChecked():
        setting.set_parameter('show-menu', True)
    elif dialogs.question_msg(
        parent, messages.DISABLE_MENU_LINE, 'Изменение настройки'
    ):
        setting.set_parameter('show-menu', False)
    else:
        check_obj.setCheckState(2)


def menu_line_color_style():
    dialogs.show_info_msg(messages.ON_MENU_COLOR_STYLE, 'Информация')
    setting.set_parameter('menu-style', 'color-style')


def menu_line_transparent():
    dialogs.show_info_msg(messages.ON_MENU_TRANSPARENT, 'Информация')
    setting.set_parameter('menu-style', 'transparent')


def init_menu_line(parent, ui):
    current_status = setting.get_parameter('show-menu')
    ui.menu_line_chk.setChecked(current_status)
    ui.menu_line_chk.stateChanged.connect(lambda: menu_line_check(parent, ui.menu_line_chk))
    ui.menu_color_style_btn.clicked.connect(menu_line_color_style)
    ui.menu_style_btn.clicked.connect(menu_line_transparent)
