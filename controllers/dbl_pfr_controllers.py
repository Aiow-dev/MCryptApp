from handlers import dbl_pfr_handlers
from events import event_components
from components import chars


def init_double_playfair(ui):
    enc_form_data = {'msg_input': ui.enc_dp_msg_txt, 'left_tbl_widget': ui.enc_dp_lt_table,
                     'right_tbl_widget': ui.enc_dp_rt_table, 'enc_msg_input': ui.enc_dp_oc_txt,
                     'enc_tbl_input': ui.enc_smp_ot_txt}
    dec_form_data = {'msg_input': ui.dec_dp_msg_txt, 'left_tbl_widget': ui.dec_dp_lt_table,
                     'right_tbl_widget': ui.dec_dp_rt_table, 'enc_msg_input': ui.dec_dp_oc_txt,
                     'enc_tbl_input': ui.dec_smp_ot_txt}
    enc_tbl_widgets = [ui.enc_dp_lt_table, ui.enc_dp_rt_table]
    dec_tbl_widgets = [ui.dec_dp_lt_table, ui.dec_dp_rt_table]
    max_tbl_size = 1000
    alphabet = chars.EXT_RU_ALPHABET
    ui.enc_dp_btn.clicked.connect(lambda: dbl_pfr_handlers.enc_proc_double_playfair(enc_form_data))
    ui.dec_dp_btn.clicked.connect(lambda: dbl_pfr_handlers.dec_proc_double_playfair(dec_form_data))
    event_components.empty_text_changed(ui.enc_dp_msg_txt)
    event_components.empty_text_changed(ui.dec_dp_msg_txt)
    event_components.positive_number_text_changed(ui.enc_dp_row_txt)
    event_components.positive_number_text_changed(ui.dec_dp_row_txt)
    event_components.positive_number_text_changed(ui.enc_dp_clm_txt)
    event_components.positive_number_text_changed(ui.dec_dp_clm_txt)
    event_components.tables_row_text_changed(enc_tbl_widgets, ui.enc_dp_row_txt, max_tbl_size)
    event_components.tables_clm_text_changed(enc_tbl_widgets, ui.enc_dp_clm_txt, max_tbl_size)
    event_components.tables_row_text_changed(dec_tbl_widgets, ui.dec_dp_row_txt, max_tbl_size)
    event_components.tables_clm_text_changed(dec_tbl_widgets, ui.dec_dp_clm_txt, max_tbl_size)
    event_components.tables_rand_state_changed(enc_tbl_widgets, ui.enc_dp_chk, alphabet)
    event_components.tables_rand_state_changed(dec_tbl_widgets, ui.dec_dp_chk, alphabet)
    event_components.table_size_charset_state_changed(ui.enc_dp_lt_table, ui.enc_dp_chk, alphabet)
    event_components.table_size_charset_state_changed(ui.dec_dp_lt_table, ui.dec_dp_chk, alphabet)
    event_components.tbl_char_unique_item_changed(ui.enc_dp_lt_table)
    event_components.tbl_char_unique_item_changed(ui.enc_dp_rt_table)
    event_components.tbl_char_unique_item_changed(ui.dec_dp_lt_table)
    event_components.tbl_char_unique_item_changed(ui.dec_dp_rt_table)
    event_components.shortcut_return(ui.enc_dp_btn)
    event_components.shortcut_return(ui.dec_dp_btn)
