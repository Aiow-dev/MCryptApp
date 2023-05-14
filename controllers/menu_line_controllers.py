from components import dialogs, setting
from controllers import messages


def menu_line_check(parent, check_obj):
    if not check_obj.isChecked():
        result = dialogs.question_msg(parent, messages.DISABLE_MENU_LINE, 'Изменение настройки')
        if result:
            setting.set_parameter('show-menu', False)
        else:
            check_obj.setCheckState(2)
    else:
        setting.set_parameter('show-menu', True)


def init_menu_line(parent, ui):
    current_status = setting.get_parameter('show-menu')
    ui.menu_line_chk.setChecked(current_status)
    ui.menu_line_chk.stateChanged.connect(lambda: menu_line_check(parent, ui.menu_line_chk))
