from handlers import cs_handlers
from events import event_components
from components import chars


def init_classic_caesar(ui):
    enc_form_data = {'msg_input': ui.enc_cs_msg_txt, 'key_input': ui.enc_cs_key_txt,
                     'enc_msg_input': ui.enc_cs_oc_txt, 'enc_tbl_input': ui.enc_cs_ot_txt}
    dec_form_data = {'msg_input': ui.dec_cs_msg_txt, 'key_input': ui.dec_cs_key_txt,
                     'enc_msg_input': ui.dec_cs_oc_txt, 'enc_tbl_input': ui.dec_cs_ot_txt}
    ui.enc_cs_btn.clicked.connect(lambda: cs_handlers.enc_proc_classic_cs(enc_form_data))
    ui.dec_cs_btn.clicked.connect(lambda: cs_handlers.dec_proc_classic_cs(dec_form_data))
    event_components.empty_text_changed(ui.enc_cs_msg_txt)
    event_components.empty_text_changed(ui.dec_cs_msg_txt)
    event_components.positive_number_text_changed(ui.enc_cs_key_txt)
    event_components.positive_number_text_changed(ui.dec_cs_key_txt)
    event_components.shortcut_return(ui.enc_cs_btn)
    event_components.shortcut_return(ui.dec_cs_btn)


def init_key_caesar(ui):
    enc_form_data = {'msg_input': ui.enc_kcs_msg_txt, 'key_input': ui.enc_kcs_key_txt,
                     'key_k_input': ui.enc_kcs_key_k_txt, 'enc_msg_input': ui.enc_kcs_oc_txt,
                     'enc_tbl_input': ui.enc_kcs_tsb_text, 'enc_tbl_widget': ui.enc_kcs_wsb_table}
    dec_form_data = {'msg_input': ui.dec_kcs_msg_txt, 'key_input': ui.dec_kcs_key_txt,
                     'key_k_input': ui.dec_kcs_key_k_txt, 'enc_msg_input': ui.dec_kcs_oc_txt,
                     'enc_tbl_input': ui.dec_kcs_tsb_text, 'enc_tbl_widget': ui.dec_kcs_wsb_table}
    input_delay = 800
    ui.enc_cs_btn.clicked.connect(lambda: cs_handlers.enc_proc_key_cs(enc_form_data))
    ui.dec_cs_btn.clicked.connect(lambda: cs_handlers.dec_proc_key_cs(dec_form_data))
    event_components.empty_text_changed(ui.enc_kcs_msg_txt)
    event_components.empty_text_changed(ui.dec_kcs_msg_txt)
    event_components.digit_text_changed(ui.enc_kcs_key_k_txt)
    event_components.digit_text_changed(ui.dec_kcs_key_k_txt)
    event_components.time_chars_ign_text_changed(ui.enc_kcs_key_txt, chars.RU_ALPHABET, input_delay)
    event_components.time_chars_ign_text_changed(ui.dec_kcs_key_txt, chars.RU_ALPHABET, input_delay)
    event_components.shortcut_return(ui.enc_kcs_btn)
    event_components.shortcut_return(ui.dec_kcs_btn)
