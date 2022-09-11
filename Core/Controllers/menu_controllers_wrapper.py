from View import main_window


class MenuControllersWrapper:
    def __init__(self, ui: main_window.Ui_main_window):
        self.ui = ui

    def menu_controller_binding(self) -> None:
        self.ui.action_smp.triggered.connect(lambda: self.ui.enc_combo_box.setCurrentIndex(0))
        self.ui.action_kpm.triggered.connect(lambda: self.ui.enc_combo_box.setCurrentIndex(1))

        self.ui.action_cs.triggered.connect(lambda: self.ui.enc_combo_box.setCurrentIndex(3))
        self.ui.action_acs.triggered.connect(lambda: self.ui.enc_combo_box.setCurrentIndex(4))
        self.ui.action_kcs.triggered.connect(lambda: self.ui.enc_combo_box.setCurrentIndex(5))

        self.ui.action_ts.triggered.connect(lambda: self.ui.enc_combo_box.setCurrentIndex(6))

        self.ui.action_vs.triggered.connect(lambda: self.ui.enc_combo_box.setCurrentIndex(7))
