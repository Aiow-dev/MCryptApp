from PyQt5.QtWidgets import qApp

from controllers import page
from components import windows, app


def init_menu_pages(ui):
    actions = [ui.action_smp, ui.action_kpm, ui.action_dpm, ui.action_ms,
               ui.action_cs, ui.action_acs, ui.action_kcs, ui.action_ts,
               ui.action_vs, ui.action_ps, ui.action_dp, ]
    for index, action in enumerate(actions):
        action.triggered.connect(page.switch_page(ui, index))


def init_menu(window, ui):
    ui.action_program_info.triggered.connect(windows.show_program_info)
    ui.action_settings_window.triggered.connect(lambda: windows.show_settings_window(window))
    ui.action_exit.triggered.connect(qApp.quit)
    ui.action_reboot.triggered.connect(app.restart)
    init_menu_pages(ui)
