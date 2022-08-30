from typing import Dict, List

from PyQt5.QtWidgets import QLineEdit

from View import main_window

from Core.Helpers.HelpersUI import style_helpers
from Core.Helpers.HelpersUI import styles

from Core.Controllers import controllers_utilities


class EventControllersWrapper:
    def __init__(self, ui: main_window.Ui_main_window, colors: Dict[str, styles.Color]):
        self.ui = ui
        self.colors = colors

    def number_text_handler(self, ui_obj):
        color: styles.Color = self.colors['default']
        tool_tip_text: str = ''

        if not ui_obj.text().isdigit():
            color = self.colors['error']
            tool_tip_text = 'Поле должно содержать только цифры'

        style_helpers.set_line_edit_border_color(ui_obj, color)
        ui_obj.setToolTip(tool_tip_text)

    def text_handler(self, ui_obj):
        color: styles.Color = self.colors['default']
        tool_tip_text: str = ''

        ui_obj_text = ui_obj.text()

        if ui_obj_text.isspace() or ui_obj_text == '':
            color = self.colors['error']
            tool_tip_text = 'Поле не может быть пустым или содержать только пробельные символы'

        style_helpers.set_line_edit_border_color(ui_obj, color)
        ui_obj.setToolTip(tool_tip_text)

    def event_number_text_binding(self) -> None:
        number_text_obj_list: List[QLineEdit] = [
            self.ui.enc_smp_row_txt, self.ui.enc_smp_clm_txt,
            self.ui.dec_smp_row_txt, self.ui.dec_smp_clm_txt,
            self.ui.enc_kpm_row_txt, self.ui.enc_kpm_clm_txt,
            self.ui.dec_kpm_row_txt, self.ui.dec_kpm_clm_txt,
            self.ui.enc_cs_key_txt, self.ui.dec_cs_key_txt,
            self.ui.enc_acs_key_a_txt, self.ui.enc_acs_key_b_txt,
            self.ui.dec_acs_key_a_txt, self.ui.dec_acs_key_b_txt,
            self.ui.enc_kcs_key_k_txt, self.ui.dec_kcs_key_k_txt,
            self.ui.enc_ts_row_txt, self.ui.enc_ts_clm_txt,
        ]

        controllers_utilities.number_text_handler_multi_connect(
            number_text_obj_list, self
        )

    def event_text_binding(self) -> None:
        text_obj_list: List[QLineEdit] = [
            self.ui.enc_smp_msg_txt, self.ui.dec_smp_msg_txt,
            self.ui.enc_kpm_msg_txt, self.ui.enc_kpm_key_txt,
            self.ui.dec_kpm_msg_txt, self.ui.dec_kpm_key_txt,
            self.ui.enc_cs_msg_txt, self.ui.enc_cs_key_txt,
            self.ui.dec_cs_msg_txt, self.ui.dec_cs_key_txt,
            self.ui.enc_acs_msg_txt, self.ui.dec_acs_msg_txt,
            self.ui.enc_kcs_msg_txt, self.ui.enc_kcs_key_txt,
            self.ui.dec_kcs_msg_txt, self.ui.dec_kcs_key_txt,
            self.ui.enc_ts_msg_txt, self.ui.enc_ts_key_txt,
        ]

        controllers_utilities.text_handler_multi_connect(
            text_obj_list, self
        )

    def event_controller_binding(self) -> None:
        self.event_number_text_binding()

        self.event_text_binding()
