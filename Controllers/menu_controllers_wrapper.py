from typing import List

from PyQt5.QtWidgets import QAction

from View import main_window

from Utils import controllers_utils


class MenuControllersWrapper:
    def __init__(self, ui: main_window.Ui_main_window):
        self.ui = ui

    def menu_controller_binding(self) -> None:
        actions_list: List[QAction] = [
            self.ui.action_smp, self.ui.action_kpm,
            self.ui.action_5, self.ui.action_ms,
            self.ui.action_cs, self.ui.action_acs,
            self.ui.action_kcs, self.ui.action_ts,
            self.ui.action_vs, self.ui.action_ps,
        ]

        for action_index, action in enumerate(actions_list):
            action.triggered.connect(controllers_utils.switch_page(self.ui.enc_combo_box, action_index))
