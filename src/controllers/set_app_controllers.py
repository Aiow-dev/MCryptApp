from src.components import dialogs, setting, app
from src.controllers import messages


def confirm_quit_check(parent, check_obj):
    if check_obj.isChecked():
        setting.set_parameter('confirm-quit', True)
    elif dialogs.question_msg(parent, messages.DISABLE_CONFIRM_QUIT, 'Изменение настройки'):
        setting.set_parameter('confirm-quit', False)
    else:
        check_obj.setCheckState(2)


def init_confirm_quit(parent, ui):
    current_status = setting.get_parameter('confirm-quit')
    ui.confirm_quit_chk.setChecked(current_status)
    ui.confirm_quit_chk.stateChanged.connect(lambda: confirm_quit_check(parent, ui.confirm_quit_chk))
    ui.btn_restart.clicked.connect(lambda: app.restart_confirm(parent))
    ui.btn_quit.clicked.connect(lambda: app.quit_confirm(parent))
