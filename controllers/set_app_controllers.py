from components import dialogs, setting, app
from controllers import messages


def confirm_quit_check(parent, check_obj):
    if check_obj.isChecked():
        result = dialogs.question_msg(parent, messages.DISABLE_CONFIRM_QUIT, 'Изменение настройки')
        if result:
            setting.set_confirm_quit(False)
        else:
            check_obj.setCheckState(0)
    else:
        setting.set_confirm_quit(True)


def init_confirm_quit(parent, ui):
    current_status = setting.is_confirm_quit()
    ui.confirm_quit_chk.setChecked(not current_status)
    ui.confirm_quit_chk.stateChanged.connect(lambda: confirm_quit_check(parent, ui.confirm_quit_chk))
    ui.btn_restart.clicked.connect(lambda: app.restart_confirm(parent))
    ui.btn_quit.clicked.connect(lambda: app.quit_confirm(parent))
