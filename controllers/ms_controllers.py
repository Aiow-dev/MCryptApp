from handlers import ms_handlers
from events import event_components
from components import scheme_colors


def init_magic_square(ui):
    enc_form_data = {'msg_input': ui.enc_ms_msg_txt, 'rank_input': ui.enc_ms_rank_txt,
                     'key_tbl_widget': ui.enc_ms_tms_table, 'enc_msg_input': ui.enc_ms_oc_txt,
                     'enc_tbl_widget': ui.enc_ms_ot_table}
    dec_form_data = {'msg_input': ui.dec_ms_msg_txt, 'rank_input': ui.dec_ms_rank_txt,
                     'key_tbl_widget': ui.dec_ms_tms_table, 'enc_msg_input': ui.dec_ms_oc_txt,
                     'enc_tbl_widget': ui.dec_ms_ot_table}
    tbl_rank_limit = 1000
    ui.enc_ms_btn.clicked.connect(lambda: ms_handlers.enc_proc_ms(enc_form_data))
    ui.dec_ms_btn.clicked.connect(lambda: ms_handlers.dec_proc_ms(dec_form_data))
    event_components.empty_text_changed(ui.enc_ms_msg_txt)
    event_components.empty_text_changed(ui.dec_ms_msg_txt)
    event_components.positive_number_text_changed(ui.enc_ms_rank_txt)
    event_components.positive_number_text_changed(ui.dec_ms_rank_txt)
    event_components.tbl_rank_text_changed(ui.enc_ms_rank_txt, ui.enc_ms_tms_table, tbl_rank_limit)
    event_components.tbl_rank_text_changed(ui.enc_ms_rank_txt, ui.enc_ms_ot_table, tbl_rank_limit)
    event_components.tbl_rank_text_changed(ui.dec_ms_rank_txt, ui.dec_ms_tms_table, tbl_rank_limit)
    event_components.tbl_rank_text_changed(ui.dec_ms_rank_txt, ui.dec_ms_ot_table, tbl_rank_limit)
    color_default = scheme_colors.tbl_item_bg_default
    color_err = scheme_colors.tbl_item_bg_err
    event_components.tbl_pos_num_item_changed(ui.enc_ms_tms_table, color_default, color_err)
    event_components.tbl_pos_num_item_changed(ui.dec_ms_tms_table, color_default, color_err)
    event_components.shortcut_return(ui.enc_ms_btn)
    event_components.shortcut_return(ui.dec_ms_btn)
