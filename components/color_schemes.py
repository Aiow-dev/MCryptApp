from components import widgets


def light_scheme(ui):
    widgets.central_widget_light(ui.central_widget)
    widgets.menu_bar_light(ui.menu_bar)
    widgets.combo_box_light(ui.enc_combo_box)
    widgets.frame_light(ui.status_frame)
    widgets.tab_widget_light(ui.smp_types_tab)
    widgets.line_edit_light(ui.enc_smp_msg_txt)
    widgets.line_edit_light(ui.enc_smp_row_txt)
    widgets.line_edit_light(ui.enc_smp_clm_txt)
    widgets.line_edit_light(ui.enc_smp_oc_txt)
    widgets.text_edit_light(ui.enc_smp_ot_txt)
    widgets.label_light(ui.enc_smp_msg_lbl)
    widgets.label_light(ui.enc_smp_row_lbl)
    widgets.label_light(ui.enc_smp_clm_lbl)
    widgets.label_light(ui.enc_smp_oc_lbl)
    widgets.label_light(ui.enc_smp_ot_lbl)
    widgets.push_button_light(ui.enc_smp_btn)
