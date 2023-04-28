from handlers import systems_handlers
from events import event_components


def init_playfair(ui):
    enc_form_data = {'msg_input': ui.enc_ps_msg_txt, 'rows_input': ui.enc_ps_row_txt,
                     'columns_input': ui.enc_ps_clm_txt, 'key_input': ui.enc_ps_key_txt,
                     'enc_msg_input': ui.enc_ps_oc_txt, 'enc_tbl_input': ui.enc_ps_ot_txt}
    dec_form_data = {'msg_input': ui.dec_ps_msg_txt, 'rows_input': ui.dec_ps_row_txt,
                     'columns_input': ui.dec_ps_clm_txt, 'key_input': ui.dec_ps_key_txt,
                     'enc_msg_input': ui.dec_ps_oc_txt, 'enc_tbl_input': ui.dec_ps_ot_txt}
    ui.enc_ps_btn.clicked.connect(lambda: systems_handlers.enc_proc_playfair(enc_form_data))
    ui.dec_ps_btn.clicked.connect(lambda: systems_handlers.dec_proc_playfair(dec_form_data))
    event_components.empty_text_changed(ui.enc_ps_msg_txt)
    event_components.empty_text_changed(ui.dec_ps_msg_txt)
    event_components.empty_text_changed(ui.enc_ps_key_txt)
    event_components.empty_text_changed(ui.dec_ps_key_txt)
    event_components.positive_number_text_changed(ui.enc_ps_row_txt)
    event_components.positive_number_text_changed(ui.enc_ps_clm_txt)
    event_components.positive_number_text_changed(ui.dec_ps_row_txt)
    event_components.positive_number_text_changed(ui.dec_ps_clm_txt)
    event_components.shortcut_return(ui.enc_ps_btn)
    event_components.shortcut_return(ui.dec_ps_btn)


def init_trisemus(ui):
    enc_form_data = {'msg_input': ui.enc_ts_msg_txt, 'rows_input': ui.enc_ts_row_txt,
                     'columns_input': ui.enc_ts_clm_txt, 'key_input': ui.enc_ts_key_txt,
                     'enc_msg_input': ui.enc_ts_oc_txt, 'enc_tbl_input': ui.enc_ts_ot_txt}
    dec_form_data = {'msg_input': ui.dec_ts_msg_txt, 'rows_input': ui.dec_ts_row_txt,
                     'columns_input': ui.dec_ts_clm_txt, 'key_input': ui.dec_ts_key_txt,
                     'enc_msg_input': ui.dec_ts_oc_txt, 'enc_tbl_input': ui.dec_ts_ot_txt}
    ui.enc_ts_btn.clicked.connect(lambda: systems_handlers.enc_proc_trisemus(enc_form_data))
    ui.dec_ts_btn.clicked.connect(lambda: systems_handlers.dec_proc_trisemus(dec_form_data))
    event_components.empty_text_changed(ui.enc_ts_msg_txt)
    event_components.empty_text_changed(ui.dec_ts_msg_txt)
    event_components.empty_text_changed(ui.enc_ts_key_txt)
    event_components.empty_text_changed(ui.dec_ts_key_txt)
    event_components.positive_number_text_changed(ui.enc_ts_row_txt)
    event_components.positive_number_text_changed(ui.enc_ts_clm_txt)
    event_components.positive_number_text_changed(ui.dec_ts_row_txt)
    event_components.positive_number_text_changed(ui.dec_ts_clm_txt)
    event_components.shortcut_return(ui.enc_ts_btn)
    event_components.shortcut_return(ui.dec_ts_btn)


def init_vigenere(ui):
    enc_form_data = {'msg_input': ui.enc_vs_msg_txt, 'key_input': ui.enc_vs_key_txt,
                     'enc_msg_input': ui.enc_vs_oc_txt, 'enc_tbl_input': ui.enc_vs_tsb_text,
                     'enc_tbl_widget': ui.enc_vs_wsb_table}
    dec_form_data = {'msg_input': ui.dec_vs_msg_txt, 'key_input': ui.dec_vs_key_txt,
                     'enc_msg_input': ui.dec_vs_oc_txt, 'enc_tbl_input': ui.dec_vs_tsb_text,
                     'enc_tbl_widget': ui.dec_vs_wsb_table}
    ui.enc_vs_btn.clicked.connect(lambda: systems_handlers.enc_proc_vigenere(enc_form_data))
    ui.dec_vs_btn.clicked.connect(lambda: systems_handlers.dec_proc_vigenere(dec_form_data))
    event_components.empty_text_changed(ui.enc_vs_msg_txt)
    event_components.empty_text_changed(ui.dec_vs_msg_txt)
    event_components.empty_text_changed(ui.enc_vs_key_txt)
    event_components.empty_text_changed(ui.dec_vs_key_txt)
    event_components.shortcut_return(ui.enc_vs_btn)
    event_components.shortcut_return(ui.dec_vs_btn)
