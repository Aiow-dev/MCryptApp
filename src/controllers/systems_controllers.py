from src.handlers import systems_handlers
from src.events import event_components


def init_playfair(parent, ui):
    enc_form = {'msg_input': ui.enc_ps_msg_txt, 'rows_input': ui.enc_ps_row_txt,
                'columns_input': ui.enc_ps_clm_txt, 'key_input': ui.enc_ps_key_txt,
                'enc_msg_input': ui.enc_ps_oc_txt, 'enc_tbl_input': ui.enc_ps_ot_txt}
    dec_form = {'msg_input': ui.dec_ps_msg_txt, 'rows_input': ui.dec_ps_row_txt,
                'columns_input': ui.dec_ps_clm_txt, 'key_input': ui.dec_ps_key_txt,
                'enc_msg_input': ui.dec_ps_oc_txt, 'enc_tbl_input': ui.dec_ps_ot_txt}
    ui.enc_ps_btn.clicked.connect(lambda: systems_handlers.enc_proc_playfair(enc_form))
    ui.dec_ps_btn.clicked.connect(lambda: systems_handlers.dec_proc_playfair(dec_form))
    ui.enc_ps_auto_btn.clicked.connect(lambda: systems_handlers.auto_playfair_trisemus(parent, enc_form))
    event_components.empty_text_changed(ui.enc_ps_msg_txt)
    event_components.empty_text_changed(ui.dec_ps_msg_txt)
    event_components.empty_text_changed(ui.enc_ps_key_txt)
    event_components.empty_text_changed(ui.dec_ps_key_txt)
    event_components.positive_number_text_changed(ui.enc_ps_row_txt)
    event_components.positive_number_text_changed(ui.enc_ps_clm_txt)
    event_components.positive_number_text_changed(ui.dec_ps_row_txt)
    event_components.positive_number_text_changed(ui.dec_ps_clm_txt)


def init_trisemus(parent, ui):
    enc_form = {'msg_input': ui.enc_ts_msg_txt, 'rows_input': ui.enc_ts_row_txt,
                'columns_input': ui.enc_ts_clm_txt, 'key_input': ui.enc_ts_key_txt,
                'enc_msg_input': ui.enc_ts_oc_txt, 'enc_tbl_input': ui.enc_ts_ot_txt}
    dec_form = {'msg_input': ui.dec_ts_msg_txt, 'rows_input': ui.dec_ts_row_txt,
                'columns_input': ui.dec_ts_clm_txt, 'key_input': ui.dec_ts_key_txt,
                'enc_msg_input': ui.dec_ts_oc_txt, 'enc_tbl_input': ui.dec_ts_ot_txt}
    ui.enc_ts_btn.clicked.connect(lambda: systems_handlers.enc_proc_trisemus(enc_form))
    ui.dec_ts_btn.clicked.connect(lambda: systems_handlers.dec_proc_trisemus(dec_form))
    ui.enc_ts_auto_btn.clicked.connect(lambda: systems_handlers.auto_playfair_trisemus(parent, enc_form))
    event_components.empty_text_changed(ui.enc_ts_msg_txt)
    event_components.empty_text_changed(ui.dec_ts_msg_txt)
    event_components.empty_text_changed(ui.enc_ts_key_txt)
    event_components.empty_text_changed(ui.dec_ts_key_txt)
    event_components.positive_number_text_changed(ui.enc_ts_row_txt)
    event_components.positive_number_text_changed(ui.enc_ts_clm_txt)
    event_components.positive_number_text_changed(ui.dec_ts_row_txt)
    event_components.positive_number_text_changed(ui.dec_ts_clm_txt)


def init_vigenere(parent, ui):
    enc_form = {'msg_input': ui.enc_vs_msg_txt, 'key_input': ui.enc_vs_key_txt,
                'enc_msg_input': ui.enc_vs_oc_txt, 'enc_tbl_input': ui.enc_vs_tsb_text,
                'enc_tbl_widget': ui.enc_vs_wsb_table}
    dec_form = {'msg_input': ui.dec_vs_msg_txt, 'key_input': ui.dec_vs_key_txt,
                'enc_msg_input': ui.dec_vs_oc_txt, 'enc_tbl_input': ui.dec_vs_tsb_text,
                'enc_tbl_widget': ui.dec_vs_wsb_table}
    ui.enc_vs_btn.clicked.connect(lambda: systems_handlers.enc_proc_vigenere(enc_form))
    ui.dec_vs_btn.clicked.connect(lambda: systems_handlers.dec_proc_vigenere(dec_form))
    ui.enc_vs_auto_btn.clicked.connect(lambda: systems_handlers.auto_vigenere(parent, enc_form))
    event_components.empty_text_changed(ui.enc_vs_msg_txt)
    event_components.empty_text_changed(ui.dec_vs_msg_txt)
    event_components.empty_text_changed(ui.enc_vs_key_txt)
    event_components.empty_text_changed(ui.dec_vs_key_txt)
