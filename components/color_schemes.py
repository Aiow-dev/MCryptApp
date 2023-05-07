from components import widgets
from views.main_window import Ui_main_window


def line_edits_light(line_edits):
    for line_edit in line_edits:
        widgets.line_edit_light(line_edit)


def labels_light(labels):
    for label in labels:
        widgets.label_light(label)


def smp_light_scheme(ui: Ui_main_window):
    widgets.tab_widget_light(ui.smp_types_tab)
    line_edits = [ui.enc_smp_msg_txt, ui.enc_smp_row_txt, ui.enc_smp_clm_txt,
                  ui.enc_smp_oc_txt, ui.dec_smp_msg_txt, ui.dec_smp_row_txt,
                  ui.dec_smp_clm_txt, ui.dec_smp_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light(ui.enc_smp_ot_txt)
    widgets.text_edit_light(ui.dec_smp_ot_txt)
    labels = [ui.enc_smp_msg_lbl, ui.enc_smp_row_lbl, ui.enc_smp_clm_lbl,
              ui.enc_smp_oc_lbl, ui.enc_smp_ot_lbl, ui.dec_smp_msg_lbl,
              ui.dec_smp_row_lbl, ui.dec_smp_clm_lbl, ui.dec_smp_oc_lbl,
              ui.dec_smp_ot_lbl]
    labels_light(labels)
    widgets.push_button_light(ui.enc_smp_btn)
    widgets.push_button_light(ui.dec_smp_btn)


def kpm_light_scheme(ui: Ui_main_window):
    widgets.tab_widget_light(ui.kpm_types_tab)
    line_edits = [ui.enc_kpm_msg_txt, ui.enc_kpm_row_txt, ui.enc_kpm_clm_txt,
                  ui.enc_kpm_key_txt, ui.enc_kpm_oc_txt, ui.dec_kpm_msg_txt,
                  ui.dec_kpm_row_txt, ui.dec_kpm_clm_txt, ui.dec_kpm_key_txt,
                  ui.dec_kpm_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light(ui.enc_kpm_ot_txt)
    widgets.text_edit_light(ui.dec_kpm_ot_txt)
    labels = [ui.enc_kpm_msg_lbl, ui.enc_kpm_row_lbl, ui.enc_kpm_clm_lbl,
              ui.enc_kpm_key_lbl, ui.enc_kpm_oc_lbl, ui.enc_kpm_ot_lbl,
              ui.dec_kpm_msg_lbl, ui.dec_kpm_row_lbl, ui.dec_kpm_clm_lbl,
              ui.dec_kpm_key_lbl, ui.dec_kpm_oc_lbl, ui.dec_kpm_ot_lbl]
    labels_light(labels)
    widgets.push_button_light(ui.enc_kpm_btn)
    widgets.push_button_light(ui.dec_kpm_btn)


def dpm_light_scheme(ui: Ui_main_window):
    widgets.tab_widget_light(ui.dpm_types_tab)
    line_edits = [ui.enc_dpm_msg_txt, ui.enc_dpm_row_txt, ui.enc_dpm_clm_txt,
                  ui.enc_dpm_key_r_txt, ui.enc_dpm_key_c_txt, ui.enc_dpm_oc_txt,
                  ui.dec_dpm_msg_txt, ui.dec_dpm_row_txt, ui.dec_dpm_clm_txt,
                  ui.dec_dpm_key_r_txt, ui.dec_dpm_key_c_txt, ui.dec_dpm_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light(ui.enc_dpm_ot_txt)
    widgets.text_edit_light(ui.dec_dpm_ot_txt)
    labels = [ui.enc_dpm_msg_lbl, ui.enc_dpm_row_lbl, ui.enc_dpm_clm_lbl,
              ui.enc_dpm_key_r_lbl, ui.enc_dpm_key_c_lbl, ui.enc_dpm_oc_lbl,
              ui.enc_dpm_ot_lbl, ui.dec_dpm_msg_lbl, ui.dec_dpm_row_lbl,
              ui.dec_dpm_clm_lbl, ui.dec_dpm_key_r_lbl, ui.dec_dpm_key_c_lbl,
              ui.dec_dpm_oc_lbl, ui.dec_dpm_ot_lbl]
    labels_light(labels)
    widgets.push_button_light(ui.enc_dpm_btn)
    widgets.push_button_light(ui.dec_dpm_btn)


def ms_light_scheme(ui: Ui_main_window):
    widgets.tab_widget_light(ui.ms_types_tab)
    line_edits = [ui.enc_ms_msg_txt, ui.enc_ms_rank_txt, ui.enc_dpm_clm_txt,
                  ui.enc_ms_oc_txt, ui.dec_ms_msg_txt, ui.dec_ms_rank_txt,
                  ui.dec_ms_oc_txt]
    line_edits_light(line_edits)
    widgets.table_widget_light(ui.enc_ms_tms_table)
    widgets.table_widget_light(ui.enc_ms_ot_table)
    widgets.table_widget_light(ui.dec_ms_tms_table)
    widgets.table_widget_light(ui.dec_ms_ot_table)
    labels = [ui.enc_ms_msg_lbl, ui.enc_ms_rank_lbl, ui.enc_ms_oc_lbl,
              ui.dec_ms_msg_lbl, ui.dec_ms_rank_lbl, ui.dec_ms_oc_lbl]
    labels_light(labels)
    widgets.push_button_light(ui.enc_ms_btn)
    widgets.push_button_light(ui.dec_ms_btn)


def cs_light_scheme(ui: Ui_main_window):
    widgets.tab_widget_light(ui.cs_types_tab)
    line_edits = [ui.enc_cs_msg_txt, ui.enc_cs_key_txt, ui.enc_cs_oc_txt,
                  ui.dec_cs_msg_txt, ui.dec_cs_key_txt, ui.dec_cs_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light(ui.enc_cs_ot_txt)
    widgets.text_edit_light(ui.dec_cs_ot_txt)
    labels = [ui.enc_cs_msg_lbl, ui.enc_cs_key_lbl, ui.enc_cs_oc_lbl,
              ui.enc_cs_ot_lbl, ui.dec_cs_msg_lbl, ui.dec_cs_key_lbl,
              ui.dec_cs_oc_lbl]
    labels_light(labels)
    widgets.push_button_light(ui.enc_cs_btn)
    widgets.push_button_light(ui.dec_cs_btn)


def acs_light_scheme(ui: Ui_main_window):
    widgets.tab_widget_light(ui.acs_types_tab)
    line_edits = [ui.enc_acs_msg_txt, ui.enc_acs_key_a_txt, ui.enc_acs_key_b_txt,
                  ui.enc_acs_oc_txt, ui.dec_acs_msg_txt, ui.dec_acs_key_a_txt,
                  ui.dec_acs_key_b_txt, ui.dec_acs_oc_txt]
    line_edits_light(line_edits)
    widgets.table_widget_light(ui.enc_acs_twn_table)
    widgets.table_widget_light(ui.enc_acs_twl_table)
    widgets.table_widget_light(ui.dec_acs_twn_table)
    widgets.table_widget_light(ui.dec_acs_twl_table)
    labels = [ui.enc_acs_msg_lbl, ui.enc_acs_key_a_lbl, ui.enc_acs_key_b_lbl,
              ui.enc_acs_oc_lbl, ui.dec_acs_msg_lbl, ui.dec_acs_key_a_lbl,
              ui.dec_acs_key_b_lbl, ui.dec_acs_oc_lbl]
    labels_light(labels)
    widgets.push_button_light(ui.enc_acs_btn)
    widgets.push_button_light(ui.dec_acs_btn)


def kcs_light_scheme(ui: Ui_main_window):
    widgets.tab_widget_light(ui.kcs_types_tab)
    line_edits = [ui.enc_kcs_msg_txt, ui.enc_kcs_key_txt, ui.enc_kcs_key_k_txt,
                  ui.enc_kcs_oc_txt, ui.dec_kcs_msg_txt, ui.dec_kcs_key_txt,
                  ui.dec_kcs_key_k_txt, ui.dec_kcs_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light(ui.enc_kcs_tsb_text)
    widgets.text_edit_light(ui.dec_kcs_tsb_text)
    widgets.table_widget_light(ui.enc_kcs_wsb_table)
    widgets.table_widget_light(ui.dec_kcs_wsb_table)
    labels = [ui.enc_kcs_msg_lbl, ui.enc_kcs_key_lbl, ui.enc_kcs_key_k_lbl,
              ui.enc_kcs_oc_lbl, ui.dec_kcs_msg_lbl, ui.dec_kcs_key_lbl,
              ui.dec_kcs_key_k_lbl, ui.dec_kcs_oc_lbl]
    labels_light(labels)
    widgets.push_button_light(ui.enc_kcs_btn)
    widgets.push_button_light(ui.dec_kcs_btn)


def ts_light_scheme(ui: Ui_main_window):
    widgets.tab_widget_light(ui.ts_types_tab)
    line_edits = [ui.enc_ts_msg_txt, ui.enc_ts_row_txt, ui.enc_ts_clm_txt,
                  ui.enc_ts_key_txt, ui.enc_ts_oc_txt, ui.dec_ts_msg_txt,
                  ui.dec_ts_row_txt, ui.dec_ts_clm_txt, ui.dec_ts_key_txt,
                  ui.dec_ts_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light(ui.enc_ts_ot_txt)
    widgets.text_edit_light(ui.dec_ts_ot_txt)
    labels = [ui.enc_ts_msg_lbl, ui.enc_ts_row_lbl, ui.enc_ts_clm_lbl,
              ui.enc_ts_key_lbl, ui.enc_ts_oc_lbl, ui.enc_ts_ot_lbl,
              ui.dec_ts_msg_lbl, ui.dec_ts_row_lbl, ui.dec_ts_clm_lbl,
              ui.dec_ts_key_lbl, ui.dec_ts_oc_lbl, ui.dec_ts_ot_lbl]
    labels_light(labels)
    widgets.push_button_light(ui.enc_ts_btn)
    widgets.push_button_light(ui.dec_ts_btn)


def vs_light_scheme(ui: Ui_main_window):
    widgets.tab_widget_light(ui.vs_types_tab)
    line_edits = [ui.enc_vs_msg_txt, ui.enc_vs_key_txt, ui.enc_vs_oc_txt,
                  ui.dec_vs_msg_txt, ui.dec_vs_key_txt, ui.dec_vs_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light(ui.enc_vs_tsb_text)
    widgets.text_edit_light(ui.dec_vs_tsb_text)
    widgets.table_widget_light(ui.enc_vs_wsb_table)
    widgets.table_widget_light(ui.dec_vs_wsb_table)
    labels = [ui.enc_vs_msg_lbl, ui.enc_vs_key_lbl, ui.enc_vs_oc_lbl,
              ui.dec_vs_msg_lbl, ui.dec_vs_key_lbl, ui.dec_vs_oc_lbl]
    labels_light(labels)
    widgets.push_button_light(ui.enc_vs_btn)
    widgets.push_button_light(ui.dec_vs_btn)


def ps_light_scheme(ui: Ui_main_window):
    widgets.tab_widget_light(ui.ps_types_tab)
    line_edits = [ui.enc_ps_msg_txt, ui.enc_ps_row_txt, ui.enc_ps_clm_txt,
                  ui.enc_ps_key_txt, ui.enc_ps_oc_txt, ui.dec_ps_msg_txt,
                  ui.dec_ps_row_txt, ui.dec_ps_clm_txt, ui.dec_ps_key_txt,
                  ui.dec_ps_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light(ui.enc_ps_ot_txt)
    widgets.text_edit_light(ui.dec_ps_ot_txt)
    labels = [ui.enc_ps_msg_lbl, ui.enc_ps_row_lbl, ui.enc_ps_clm_lbl,
              ui.enc_ps_key_lbl, ui.enc_ps_oc_lbl, ui.enc_ps_ot_lbl,
              ui.dec_ps_msg_lbl, ui.dec_ps_row_lbl, ui.dec_ps_clm_lbl,
              ui.dec_ps_key_lbl, ui.dec_ps_oc_lbl, ui.dec_ps_ot_lbl]
    labels_light(labels)
    widgets.push_button_light(ui.enc_ps_btn)
    widgets.push_button_light(ui.dec_ps_btn)


def dp_light_scheme(ui: Ui_main_window):
    widgets.tab_widget_light(ui.dp_types_tab)
    line_edits = [ui.enc_dp_msg_txt, ui.enc_dp_row_txt, ui.enc_dp_clm_txt,
                  ui.enc_dp_oc_txt, ui.dec_dp_msg_txt, ui.dec_dp_row_txt,
                  ui.dec_dp_clm_txt, ui.dec_dp_oc_txt]
    line_edits_light(line_edits)
    widgets.check_box_light(ui.enc_dp_chk)
    widgets.check_box_light(ui.dec_dp_chk)
    widgets.table_widget_light(ui.enc_dp_lt_table)
    widgets.table_widget_light(ui.enc_dp_rt_table)
    widgets.table_widget_light(ui.dec_dp_lt_table)
    widgets.table_widget_light(ui.dec_dp_rt_table)
    labels = [ui.enc_dp_msg_lbl, ui.enc_dp_row_lbl, ui.enc_dp_clm_lbl,
              ui.enc_dp_oc_lbl, ui.dec_dp_msg_lbl, ui.dec_dp_row_lbl,
              ui.dec_dp_clm_lbl, ui.dec_dp_oc_lbl]
    labels_light(labels)
    widgets.push_button_light(ui.enc_dp_btn)
    widgets.push_button_light(ui.dec_dp_btn)


def light_scheme(ui: Ui_main_window):
    widgets.central_widget_light(ui.central_widget)
    widgets.menu_bar_light(ui.menu_bar)
    widgets.combo_box_light(ui.enc_combo_box)
    widgets.frame_light(ui.status_frame)
    smp_light_scheme(ui)
    kpm_light_scheme(ui)
    dpm_light_scheme(ui)
    ms_light_scheme(ui)
    cs_light_scheme(ui)
    acs_light_scheme(ui)
    kcs_light_scheme(ui)
    ts_light_scheme(ui)
    vs_light_scheme(ui)
    ps_light_scheme(ui)
    dp_light_scheme(ui)
