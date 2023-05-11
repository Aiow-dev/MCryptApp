from controllers import page, messages
from components import windows, app, dialogs
from windows import settings, main_window_add
from helpers import func


def init_menu_pages(ui):
    actions = [ui.action_smp, ui.action_kpm, ui.action_dpm, ui.action_ms,
               ui.action_cs, ui.action_acs, ui.action_kcs, ui.action_ts,
               ui.action_vs, ui.action_ps, ui.action_dp, ]
    for index, action in enumerate(actions):
        action.triggered.connect(page.switch_page(ui, index))


def init_menu(window, ui):
    func_single = func.FuncSingleCall()
    ui.action_program_info.triggered.connect(windows.show_program_info)
    ui.action_settings_win.triggered.connect(lambda: settings.show_settings_window(func_single, window))
    ui.action_new_win.triggered.connect(lambda: main_window_add.show_addition_window(window))
    ui.action_exit.triggered.connect(lambda: app.quit_confirm(window))
    ui.action_restart.triggered.connect(lambda: app.restart_confirm(window))
    init_menu_pages(ui)


def settings_menu():
    dialogs.show_info_msg(messages.NOT_ALLOW_SETTINGS, 'Информация')


def new_window_menu():
    dialogs.show_info_msg(messages.NOT_ALLOW_NEW_WIN, 'Информация')


def quit_menu_add():
    dialogs.show_info_msg(messages.NOT_ALLOW_QUIT, 'Информация')


def restart_menu_add():
    dialogs.show_info_msg(messages.NOT_ALLOW_RESTART, 'Информация')


def program_info_menu_add():
    dialogs.show_info_msg(messages.NOT_ALLOW_PROGRAM_INFO, 'Информация')


def help_menu_add():
    dialogs.show_info_msg(messages.NOT_ALLOW_HELP, 'Информация')


def init_menu_add(ui):
    ui.action_program_info.triggered.connect(program_info_menu_add)
    ui.action_settings_win.triggered.connect(settings_menu)
    ui.action_new_win.triggered.connect(new_window_menu)
    ui.action_help.triggered.connect(help_menu_add)
    ui.action_exit.triggered.connect(quit_menu_add)
    ui.action_restart.triggered.connect(restart_menu_add)
    init_menu_pages(ui)
