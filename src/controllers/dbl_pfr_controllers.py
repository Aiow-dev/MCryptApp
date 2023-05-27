from src.handlers import dbl_pfr_handlers
from src.events import event_components
from src.components import scheme_colors, chars


def init_double_playfair(ui):
    enc_form = {'msg_input': ui.enc_dp_msg_txt, 'rows_input': ui.enc_dp_row_txt,
                'columns_input': ui.enc_dp_clm_txt, 'left_tbl_widget': ui.enc_dp_lt_table,
                'right_tbl_widget': ui.enc_dp_rt_table, 'enc_msg_input': ui.enc_dp_oc_txt,
                'enc_tbl_input': ui.enc_smp_ot_txt}
    dec_form = {'msg_input': ui.dec_dp_msg_txt, 'rows_input': ui.dec_dp_row_txt,
                'columns_input': ui.dec_dp_clm_txt, 'left_tbl_widget': ui.dec_dp_lt_table,
                'right_tbl_widget': ui.dec_dp_rt_table, 'enc_msg_input': ui.dec_dp_oc_txt,
                'enc_tbl_input': ui.dec_smp_ot_txt}
    enc_tbl_widgets = [ui.enc_dp_lt_table, ui.enc_dp_rt_table]
    dec_tbl_widgets = [ui.dec_dp_lt_table, ui.dec_dp_rt_table]
    max_tbl_size = 1000
    alphabet = chars.EXT_RU_ALPHABET
    ui.enc_dp_btn.clicked.connect(lambda: dbl_pfr_handlers.enc_proc_double_playfair(enc_form))
    ui.dec_dp_btn.clicked.connect(lambda: dbl_pfr_handlers.dec_proc_double_playfair(dec_form))
    ui.enc_dp_auto_btn.clicked.connect(lambda: dbl_pfr_handlers.auto_double_playfair(enc_form))
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
    color_default = scheme_colors.tbl_item_bg_default
    color_err = scheme_colors.tbl_item_bg_err
    event_components.tbl_char_unique_item_changed(ui.enc_dp_lt_table, color_default, color_err)
    event_components.tbl_char_unique_item_changed(ui.enc_dp_rt_table, color_default, color_err)
    event_components.tbl_char_unique_item_changed(ui.dec_dp_lt_table, color_default, color_err)
    event_components.tbl_char_unique_item_changed(ui.dec_dp_rt_table, color_default, color_err)
