from typing import List

from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtGui

from View import main_window

from Utils.StyleUtils import style_utils

from Assets import styles


class EventControllersWrapper:
    def __init__(self, ui: main_window.Ui_main_window):
        self.ui = ui
        self.colors = styles.DEFAULT_COLORS

    def event_num(self, ui_obj):
        color: styles.Color = self.colors['default']
        tool_tip_text: str = ''

        if not ui_obj.text().isdigit():
            color = self.colors['error']
            tool_tip_text = 'Поле должно содержать только цифры'

        style_utils.set_line_edit_border_color(ui_obj, color)
        ui_obj.setToolTip(tool_tip_text)

    def event_text(self, ui_obj):
        color: styles.Color = self.colors['default']
        tool_tip_text: str = ''

        ui_obj_text = ui_obj.text()

        if ui_obj_text.isspace() or ui_obj_text == '':
            color = self.colors['error']
            tool_tip_text = 'Поле не может быть пустым или содержать только пробельные символы'

        style_utils.set_line_edit_border_color(ui_obj, color)
        ui_obj.setToolTip(tool_tip_text)

    def text_changed_connect(self, text_obj, f_event) -> None:
        text_obj.textChanged.connect(
            lambda: f_event(text_obj)
        )

    def event_shortcut(self, ui_obj, shortcut):
        ui_obj.setShortcut(QtGui.QKeySequence(shortcut))

    def event_tables_rank(self, tables, text_obj):
        try:
            number = int(text_obj.text())

            for table in tables:
                table.setRowCount(number)
                table.setColumnCount(number)
        except ValueError as value_error:
            print(value_error)

    def event_tables_rank_connect(self, tables, text_obj, f_tables_size):
        text_obj.textChanged.connect(lambda: f_tables_size(tables, text_obj))

    def text_changed_multi_connect(self, text_obj_list, f_event) -> None:
        for text_obj in text_obj_list:
            self.text_changed_connect(text_obj, f_event)

    def event_shortcut_multi_connect(self, ui_obj_list, shortcut):
        for ui_obj in ui_obj_list:
            self.event_shortcut(ui_obj, shortcut)

    def event_num_text_binding(self) -> None:
        num_text_obj_list: List[QLineEdit] = [
            self.ui.enc_smp_row_txt, self.ui.enc_smp_clm_txt,
            self.ui.dec_smp_row_txt, self.ui.dec_smp_clm_txt,
            self.ui.enc_kpm_row_txt, self.ui.enc_kpm_clm_txt,
            self.ui.dec_kpm_row_txt, self.ui.dec_kpm_clm_txt,
            self.ui.enc_cs_key_txt, self.ui.dec_cs_key_txt,
            self.ui.enc_acs_key_a_txt, self.ui.enc_acs_key_b_txt,
            self.ui.dec_acs_key_a_txt, self.ui.dec_acs_key_b_txt,
            self.ui.enc_kcs_key_k_txt, self.ui.dec_kcs_key_k_txt,
            self.ui.enc_ts_row_txt, self.ui.enc_ts_clm_txt,
            self.ui.dec_ts_row_txt, self.ui.dec_ts_clm_txt,
            self.ui.enc_ps_row_txt, self.ui.enc_ps_clm_txt,
            self.ui.dec_ps_row_txt, self.ui.dec_ps_clm_txt,
            self.ui.enc_ms_rank_txt,
        ]

        self.text_changed_multi_connect(
            num_text_obj_list, self.event_num
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
            self.ui.dec_ts_msg_txt, self.ui.dec_ts_key_txt,
            self.ui.enc_vs_msg_txt, self.ui.enc_vs_key_txt,
            self.ui.dec_vs_msg_txt, self.ui.dec_vs_key_txt,
            self.ui.enc_ps_msg_txt, self.ui.enc_ps_key_txt,
            self.ui.dec_ps_msg_txt, self.ui.dec_ps_key_txt,
            self.ui.enc_ms_msg_txt,
        ]

        self.text_changed_multi_connect(
            text_obj_list, self.event_text
        )

    def event_shortcut_binding(self) -> None:
        ui_obj_list = [
            self.ui.enc_smp_btn, self.ui.dec_smp_btn,
            self.ui.enc_kpm_btn, self.ui.dec_kpm_btn,
            self.ui.enc_cs_btn, self.ui.dec_cs_btn,
            self.ui.enc_acs_btn, self.ui.dec_acs_btn,
            self.ui.enc_kcs_btn, self.ui.dec_kcs_btn,
            self.ui.enc_ts_btn, self.ui.dec_ts_btn,
            self.ui.enc_vs_btn, self.ui.dec_vs_btn,
            self.ui.enc_ps_btn, self.ui.dec_ps_btn
        ]

        self.event_shortcut_multi_connect(ui_obj_list, 'Return')

    def event_table_size_binding(self) -> None:
        table_rank_numbers = {
            self.ui.enc_ms_rank_txt: [self.ui.enc_ms_tms_table, self.ui.enc_ms_ot_table],
        }

        for table_rank_obj, tables in table_rank_numbers.items():
            self.event_tables_rank_connect(tables, table_rank_obj, self.event_tables_rank)

    def event_controller_binding(self) -> None:
        self.event_num_text_binding()

        self.event_text_binding()

        self.event_shortcut_binding()

        self.event_table_size_binding()
