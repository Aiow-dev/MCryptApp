from controllers import page
from components import windows


def init_menu(ui):
    ui.action_program_info.triggered.connect(windows.show_program_info)
    actions = [ui.action_smp, ui.action_kpm, ui.action_dpm, ui.action_ms,
               ui.action_cs, ui.action_acs, ui.action_kcs, ui.action_ts,
               ui.action_vs, ui.action_ps, ui.action_dp, ]
    for index, action in enumerate(actions):
        action.triggered.connect(page.switch_page(ui, index))
