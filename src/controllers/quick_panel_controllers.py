from src.components import dialogs, setting
from src.controllers import messages


def quick_panel_check(check_obj):
    if check_obj.isChecked():
        dialogs.show_info_msg(messages.SET_QUICK_PANEL, 'Информация')
        setting.set_parameter('show-quick-panel', True)
    else:
        setting.set_parameter('show-quick-panel', False)


def init_quick_panel(ui):
    current_status = setting.get_parameter('show-quick-panel')
    ui.quick_panel_chk.setChecked(current_status)
    ui.quick_panel_chk.stateChanged.connect(lambda: quick_panel_check(ui.quick_panel_chk))
