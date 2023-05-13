from components import widgets, scheme_colors, colors, win_palette


def line_edits_light(line_edits):
    for line_edit in line_edits:
        widgets.line_edit_light_sys(line_edit)


def labels_light(labels):
    for label in labels:
        widgets.label_light_sys(label)


def smp_light_sys_scheme(ui):
    line_edits = [ui.enc_smp_msg_txt, ui.enc_smp_row_txt, ui.enc_smp_clm_txt,
                  ui.enc_smp_oc_txt, ui.dec_smp_msg_txt, ui.dec_smp_row_txt,
                  ui.dec_smp_clm_txt, ui.dec_smp_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light_sys(ui.enc_smp_ot_txt)
    widgets.text_edit_light_sys(ui.dec_smp_ot_txt)
    labels = [ui.enc_smp_msg_lbl, ui.enc_smp_row_lbl, ui.enc_smp_clm_lbl,
              ui.enc_smp_oc_lbl, ui.enc_smp_ot_lbl, ui.dec_smp_msg_lbl,
              ui.dec_smp_row_lbl, ui.dec_smp_clm_lbl, ui.dec_smp_oc_lbl,
              ui.dec_smp_ot_lbl]
    labels_light(labels)
    widgets.push_btn_sys(ui.enc_smp_btn)
    widgets.push_btn_sys(ui.dec_smp_btn)
    widgets.push_btn_sys(ui.enc_smp_auto_btn)


def kpm_light_sys_scheme(ui):
    line_edits = [ui.enc_kpm_msg_txt, ui.enc_kpm_row_txt, ui.enc_kpm_clm_txt,
                  ui.enc_kpm_key_txt, ui.enc_kpm_oc_txt, ui.dec_kpm_msg_txt,
                  ui.dec_kpm_row_txt, ui.dec_kpm_clm_txt, ui.dec_kpm_key_txt,
                  ui.dec_kpm_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light_sys(ui.enc_kpm_ot_txt)
    widgets.text_edit_light_sys(ui.dec_kpm_ot_txt)
    labels = [ui.enc_kpm_msg_lbl, ui.enc_kpm_row_lbl, ui.enc_kpm_clm_lbl,
              ui.enc_kpm_key_lbl, ui.enc_kpm_oc_lbl, ui.enc_kpm_ot_lbl,
              ui.dec_kpm_msg_lbl, ui.dec_kpm_row_lbl, ui.dec_kpm_clm_lbl,
              ui.dec_kpm_key_lbl, ui.dec_kpm_oc_lbl, ui.dec_kpm_ot_lbl]
    labels_light(labels)
    widgets.push_btn_sys(ui.enc_kpm_btn)
    widgets.push_btn_sys(ui.dec_kpm_btn)


def dpm_light_sys_scheme(ui):
    line_edits = [ui.enc_dpm_msg_txt, ui.enc_dpm_row_txt, ui.enc_dpm_clm_txt,
                  ui.enc_dpm_key_r_txt, ui.enc_dpm_key_c_txt, ui.enc_dpm_oc_txt,
                  ui.dec_dpm_msg_txt, ui.dec_dpm_row_txt, ui.dec_dpm_clm_txt,
                  ui.dec_dpm_key_r_txt, ui.dec_dpm_key_c_txt, ui.dec_dpm_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light_sys(ui.enc_dpm_ot_txt)
    widgets.text_edit_light_sys(ui.dec_dpm_ot_txt)
    labels = [ui.enc_dpm_msg_lbl, ui.enc_dpm_row_lbl, ui.enc_dpm_clm_lbl,
              ui.enc_dpm_key_r_lbl, ui.enc_dpm_key_c_lbl, ui.enc_dpm_oc_lbl,
              ui.enc_dpm_ot_lbl, ui.dec_dpm_msg_lbl, ui.dec_dpm_row_lbl,
              ui.dec_dpm_clm_lbl, ui.dec_dpm_key_r_lbl, ui.dec_dpm_key_c_lbl,
              ui.dec_dpm_oc_lbl, ui.dec_dpm_ot_lbl]
    labels_light(labels)
    widgets.push_btn_sys(ui.enc_dpm_btn)
    widgets.push_btn_sys(ui.dec_dpm_btn)


def ms_light_sys_scheme(ui):
    line_edits = [ui.enc_ms_msg_txt, ui.enc_ms_rank_txt, ui.enc_dpm_clm_txt,
                  ui.enc_ms_oc_txt, ui.dec_ms_msg_txt, ui.dec_ms_rank_txt,
                  ui.dec_ms_oc_txt]
    line_edits_light(line_edits)
    widgets.tbl_wgt_light_sys(ui.enc_ms_tms_table)
    widgets.tbl_wgt_light_sys(ui.enc_ms_ot_table)
    widgets.tbl_wgt_light_sys(ui.dec_ms_tms_table)
    widgets.tbl_wgt_light_sys(ui.dec_ms_ot_table)
    labels = [ui.enc_ms_msg_lbl, ui.enc_ms_rank_lbl, ui.enc_ms_oc_lbl,
              ui.dec_ms_msg_lbl, ui.dec_ms_rank_lbl, ui.dec_ms_oc_lbl]
    labels_light(labels)
    widgets.push_btn_sys(ui.enc_ms_btn)
    widgets.push_btn_sys(ui.dec_ms_btn)


def cs_light_sys_scheme(ui):
    line_edits = [ui.enc_cs_msg_txt, ui.enc_cs_key_txt, ui.enc_cs_oc_txt,
                  ui.dec_cs_msg_txt, ui.dec_cs_key_txt, ui.dec_cs_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light_sys(ui.enc_cs_ot_txt)
    widgets.text_edit_light_sys(ui.dec_cs_ot_txt)
    labels = [ui.enc_cs_msg_lbl, ui.enc_cs_key_lbl, ui.enc_cs_oc_lbl,
              ui.enc_cs_ot_lbl, ui.dec_cs_msg_lbl, ui.dec_cs_key_lbl,
              ui.dec_cs_oc_lbl]
    labels_light(labels)
    widgets.push_btn_sys(ui.enc_cs_btn)
    widgets.push_btn_sys(ui.dec_cs_btn)


def acs_light_sys_scheme(ui):
    line_edits = [ui.enc_acs_msg_txt, ui.enc_acs_key_a_txt, ui.enc_acs_key_b_txt,
                  ui.enc_acs_oc_txt, ui.dec_acs_msg_txt, ui.dec_acs_key_a_txt,
                  ui.dec_acs_key_b_txt, ui.dec_acs_oc_txt]
    line_edits_light(line_edits)
    widgets.tbl_wgt_light_sys(ui.enc_acs_twn_table)
    widgets.tbl_wgt_light_sys(ui.enc_acs_twl_table)
    widgets.tbl_wgt_light_sys(ui.dec_acs_twn_table)
    widgets.tbl_wgt_light_sys(ui.dec_acs_twl_table)
    labels = [ui.enc_acs_msg_lbl, ui.enc_acs_key_a_lbl, ui.enc_acs_key_b_lbl,
              ui.enc_acs_oc_lbl, ui.dec_acs_msg_lbl, ui.dec_acs_key_a_lbl,
              ui.dec_acs_key_b_lbl, ui.dec_acs_oc_lbl]
    labels_light(labels)
    widgets.push_btn_sys(ui.enc_acs_btn)
    widgets.push_btn_sys(ui.dec_acs_btn)


def kcs_light_sys_scheme(ui):
    line_edits = [ui.enc_kcs_msg_txt, ui.enc_kcs_key_txt, ui.enc_kcs_key_k_txt,
                  ui.enc_kcs_oc_txt, ui.dec_kcs_msg_txt, ui.dec_kcs_key_txt,
                  ui.dec_kcs_key_k_txt, ui.dec_kcs_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light_sys(ui.enc_kcs_tsb_text)
    widgets.text_edit_light_sys(ui.dec_kcs_tsb_text)
    widgets.tbl_wgt_light_sys(ui.enc_kcs_wsb_table)
    widgets.tbl_wgt_light_sys(ui.dec_kcs_wsb_table)
    labels = [ui.enc_kcs_msg_lbl, ui.enc_kcs_key_lbl, ui.enc_kcs_key_k_lbl,
              ui.enc_kcs_oc_lbl, ui.dec_kcs_msg_lbl, ui.dec_kcs_key_lbl,
              ui.dec_kcs_key_k_lbl, ui.dec_kcs_oc_lbl]
    labels_light(labels)
    widgets.push_btn_sys(ui.enc_kcs_btn)
    widgets.push_btn_sys(ui.dec_kcs_btn)


def ts_light_sys_scheme(ui):
    line_edits = [ui.enc_ts_msg_txt, ui.enc_ts_row_txt, ui.enc_ts_clm_txt,
                  ui.enc_ts_key_txt, ui.enc_ts_oc_txt, ui.dec_ts_msg_txt,
                  ui.dec_ts_row_txt, ui.dec_ts_clm_txt, ui.dec_ts_key_txt,
                  ui.dec_ts_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light_sys(ui.enc_ts_ot_txt)
    widgets.text_edit_light_sys(ui.dec_ts_ot_txt)
    labels = [ui.enc_ts_msg_lbl, ui.enc_ts_row_lbl, ui.enc_ts_clm_lbl,
              ui.enc_ts_key_lbl, ui.enc_ts_oc_lbl, ui.enc_ts_ot_lbl,
              ui.dec_ts_msg_lbl, ui.dec_ts_row_lbl, ui.dec_ts_clm_lbl,
              ui.dec_ts_key_lbl, ui.dec_ts_oc_lbl, ui.dec_ts_ot_lbl]
    labels_light(labels)
    widgets.push_btn_sys(ui.enc_ts_btn)
    widgets.push_btn_sys(ui.dec_ts_btn)


def vs_light_sys_scheme(ui):
    line_edits = [ui.enc_vs_msg_txt, ui.enc_vs_key_txt, ui.enc_vs_oc_txt,
                  ui.dec_vs_msg_txt, ui.dec_vs_key_txt, ui.dec_vs_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light_sys(ui.enc_vs_tsb_text)
    widgets.text_edit_light_sys(ui.dec_vs_tsb_text)
    widgets.tbl_wgt_light_sys(ui.enc_vs_wsb_table)
    widgets.tbl_wgt_light_sys(ui.dec_vs_wsb_table)
    labels = [ui.enc_vs_msg_lbl, ui.enc_vs_key_lbl, ui.enc_vs_oc_lbl,
              ui.dec_vs_msg_lbl, ui.dec_vs_key_lbl, ui.dec_vs_oc_lbl]
    labels_light(labels)
    widgets.push_btn_sys(ui.enc_vs_btn)
    widgets.push_btn_sys(ui.dec_vs_btn)


def ps_light_sys_scheme(ui):
    line_edits = [ui.enc_ps_msg_txt, ui.enc_ps_row_txt, ui.enc_ps_clm_txt,
                  ui.enc_ps_key_txt, ui.enc_ps_oc_txt, ui.dec_ps_msg_txt,
                  ui.dec_ps_row_txt, ui.dec_ps_clm_txt, ui.dec_ps_key_txt,
                  ui.dec_ps_oc_txt]
    line_edits_light(line_edits)
    widgets.text_edit_light_sys(ui.enc_ps_ot_txt)
    widgets.text_edit_light_sys(ui.dec_ps_ot_txt)
    labels = [ui.enc_ps_msg_lbl, ui.enc_ps_row_lbl, ui.enc_ps_clm_lbl,
              ui.enc_ps_key_lbl, ui.enc_ps_oc_lbl, ui.enc_ps_ot_lbl,
              ui.dec_ps_msg_lbl, ui.dec_ps_row_lbl, ui.dec_ps_clm_lbl,
              ui.dec_ps_key_lbl, ui.dec_ps_oc_lbl, ui.dec_ps_ot_lbl]
    labels_light(labels)
    widgets.push_btn_sys(ui.enc_ps_btn)
    widgets.push_btn_sys(ui.dec_ps_btn)


def dp_light_sys_scheme(ui):
    line_edits = [ui.enc_dp_msg_txt, ui.enc_dp_row_txt, ui.enc_dp_clm_txt,
                  ui.enc_dp_oc_txt, ui.dec_dp_msg_txt, ui.dec_dp_row_txt,
                  ui.dec_dp_clm_txt, ui.dec_dp_oc_txt]
    line_edits_light(line_edits)
    widgets.check_box_light_sys(ui.enc_dp_chk)
    widgets.check_box_light_sys(ui.dec_dp_chk)
    widgets.tbl_wgt_light_sys(ui.enc_dp_lt_table)
    widgets.tbl_wgt_light_sys(ui.enc_dp_rt_table)
    widgets.tbl_wgt_light_sys(ui.dec_dp_lt_table)
    widgets.tbl_wgt_light_sys(ui.dec_dp_rt_table)
    labels = [ui.enc_dp_msg_lbl, ui.enc_dp_row_lbl, ui.enc_dp_clm_lbl,
              ui.enc_dp_oc_lbl, ui.dec_dp_msg_lbl, ui.dec_dp_row_lbl,
              ui.dec_dp_clm_lbl, ui.dec_dp_oc_lbl]
    labels_light(labels)
    widgets.push_btn_sys(ui.enc_dp_btn)
    widgets.push_btn_sys(ui.dec_dp_btn)


def light_scheme(ui):
    scheme_colors.tbl_item_bg_default = colors.Palette.gray.value.to_rgb_q()
    scheme_colors.tbl_item_fg_default = colors.Palette.dark_charcoal.value.to_rgb_q()
    widgets.menu_bar_light(ui.menu_bar)


def light_sys_scheme(ui):
    scheme_colors.tbl_item_bg_default = colors.Palette.gray.value.to_rgb_q()
    scheme_colors.tbl_item_fg_default = colors.Palette.dark_charcoal.value.to_rgb_q()
    widgets.frame_sys(ui.status_frame)
    widgets.combo_box_light_sys(ui.enc_combo_box)
    widgets.menu_bar_light_sys(ui.menu_bar)
    smp_light_sys_scheme(ui)
    kpm_light_sys_scheme(ui)
    dpm_light_sys_scheme(ui)
    ms_light_sys_scheme(ui)
    cs_light_sys_scheme(ui)
    acs_light_sys_scheme(ui)
    kcs_light_sys_scheme(ui)
    ts_light_sys_scheme(ui)
    vs_light_sys_scheme(ui)
    ps_light_sys_scheme(ui)
    dp_light_sys_scheme(ui)


def dark_scheme(ui):
    widgets.menu_bar_dark(ui.menu_bar)


def dark_sys_scheme(ui):
    widgets.menu_bar_dark_sys(ui.menu_bar)
    widgets.frame_sys(ui.status_frame)
    widgets.combo_box_dark_sys(ui.enc_combo_box)
    btn_list = [ui.enc_smp_btn, ui.dec_smp_btn, ui.enc_kpm_btn, ui.dec_kpm_btn,
                ui.enc_dpm_btn, ui.dec_dpm_btn, ui.enc_ms_btn, ui.dec_ms_btn,
                ui.enc_cs_btn, ui.dec_cs_btn, ui.enc_acs_btn, ui.dec_acs_btn,
                ui.enc_kcs_btn, ui.dec_kcs_btn, ui.enc_ts_btn, ui.dec_ts_btn,
                ui.enc_vs_btn, ui.dec_vs_btn, ui.enc_ps_btn, ui.dec_ps_btn,
                ui.enc_dp_btn, ui.dec_dp_btn, ui.enc_smp_auto_btn]
    for btn in btn_list:
        widgets.push_btn_sys(btn)


def light_tab_corn_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_light(tab)


def light_tab_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_light_rad(tab)


def light_tab_top_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_light_top_rad(tab)


def light_tab_corn_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_light_corn_rad(tab)


def light_sys_tab_corn_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_light_sys(tab)


def light_sys_tab_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_light_sys_rad(tab)


def light_sys_tab_top_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_light_sys_top_rad(tab)


def light_sys_tab_corn_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_light_sys_corn_rad(tab)


def dark_tab_corn_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_dark(tab)


def dark_tab_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_dark_rad(tab)


def dark_tab_top_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_dark_top_rad(tab)


def dark_tab_corn_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_dark_corn_rad(tab)


def dark_sys_tab_corn_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_dark_sys(tab)


def dark_sys_tab_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_dark_sys_rad(tab)


def dark_sys_tab_top_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_dark_sys_top_rad(tab)


def dark_sys_tab_corn_rad_scheme(ui):
    tab_list = [ui.smp_types_tab, ui.kpm_types_tab, ui.dpm_types_tab, ui.ms_types_tab,
                ui.cs_types_tab, ui.acs_types_tab, ui.kcs_types_tab, ui.ts_types_tab,
                ui.vs_types_tab, ui.ps_types_tab, ui.dp_types_tab]
    for tab in tab_list:
        widgets.tab_wgt_dark_sys_corn_rad(tab)


def system_scheme(ui, is_light):
    accent = win_palette.win_accent_converted()
    complementary = win_palette.win_complementary_converted(accent)
    win_palette.accent_color = accent.to_rgb_str()
    win_palette.complementary_color = complementary.to_rgb_str()
    if is_light:
        light_sys_scheme(ui)
    else:
        dark_sys_scheme(ui)
