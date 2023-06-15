from src.handlers.encryption import cs_handlers
from src.events import event_components
from src.components import chars


def init_classic_caesar(ui):
    enc_form = {'msg_input': ui.enc_cs_msg_txt, 'key_input': ui.enc_cs_key_txt,
                'enc_msg_input': ui.enc_cs_oc_txt, 'enc_tbl_input': ui.enc_cs_ot_txt}
    dec_form = {'msg_input': ui.dec_cs_msg_txt, 'key_input': ui.dec_cs_key_txt,
                'enc_msg_input': ui.dec_cs_oc_txt, 'enc_tbl_input': ui.dec_cs_ot_txt}
    ui.enc_cs_btn.clicked.connect(lambda: cs_handlers.enc_proc_classic_cs(enc_form))
    ui.dec_cs_btn.clicked.connect(lambda: cs_handlers.dec_proc_classic_cs(dec_form))
    ui.enc_cs_auto_btn.clicked.connect(lambda: cs_handlers.auto_classic_cs(enc_form))
    event_components.empty_text_changed(ui.enc_cs_msg_txt)
    event_components.empty_text_changed(ui.dec_cs_msg_txt)
    event_components.positive_number_text_changed(ui.enc_cs_key_txt)
    event_components.positive_number_text_changed(ui.dec_cs_key_txt)


def init_affine_caesar(ui):
    enc_form = {'msg_input': ui.enc_acs_msg_txt, 'key_a_input': ui.enc_acs_key_a_txt,
                'key_b_input': ui.enc_acs_key_b_txt, 'enc_tbl_num_widget': ui.enc_acs_twn_table,
                'enc_tbl_letter_widget': ui.enc_acs_twl_table, 'enc_msg_input': ui.enc_acs_oc_txt}
    dec_form = {'msg_input': ui.dec_acs_msg_txt, 'key_a_input': ui.dec_acs_key_a_txt,
                'key_b_input': ui.dec_acs_key_b_txt, 'enc_tbl_num_widget': ui.dec_acs_twn_table,
                'enc_tbl_letter_widget': ui.dec_acs_twl_table, 'enc_msg_input': ui.dec_acs_oc_txt}
    ui.enc_acs_btn.clicked.connect(lambda: cs_handlers.enc_proc_affine_cs(enc_form))
    ui.dec_acs_btn.clicked.connect(lambda: cs_handlers.dec_proc_affine_cs(dec_form))
    ui.enc_acs_auto_btn.clicked.connect(lambda: cs_handlers.auto_affine_cs(enc_form))
    event_components.empty_text_changed(ui.enc_acs_msg_txt)
    event_components.empty_text_changed(ui.dec_acs_msg_txt)
    event_components.positive_number_text_changed(ui.enc_acs_key_a_txt)
    event_components.positive_number_text_changed(ui.dec_acs_key_a_txt)
    event_components.number_text_changed(ui.enc_acs_key_b_txt)
    event_components.number_text_changed(ui.dec_acs_key_b_txt)


def init_key_caesar(ui):
    enc_form = {'msg_input': ui.enc_kcs_msg_txt, 'key_input': ui.enc_kcs_key_txt,
                'key_k_input': ui.enc_kcs_key_k_txt, 'enc_msg_input': ui.enc_kcs_oc_txt,
                'enc_tbl_input': ui.enc_kcs_tsb_text, 'enc_tbl_widget': ui.enc_kcs_wsb_table}
    dec_form = {'msg_input': ui.dec_kcs_msg_txt, 'key_input': ui.dec_kcs_key_txt,
                'key_k_input': ui.dec_kcs_key_k_txt, 'enc_msg_input': ui.dec_kcs_oc_txt,
                'enc_tbl_input': ui.dec_kcs_tsb_text, 'enc_tbl_widget': ui.dec_kcs_wsb_table}
    input_delay = 800
    ui.enc_kcs_btn.clicked.connect(lambda: cs_handlers.enc_proc_key_cs(enc_form))
    ui.dec_kcs_btn.clicked.connect(lambda: cs_handlers.dec_proc_key_cs(dec_form))
    ui.enc_kcs_auto_btn.clicked.connect(lambda: cs_handlers.auto_key_cs(enc_form))
    event_components.empty_text_changed(ui.enc_kcs_msg_txt)
    event_components.empty_text_changed(ui.dec_kcs_msg_txt)
    event_components.digit_text_changed(ui.enc_kcs_key_k_txt)
    event_components.digit_text_changed(ui.dec_kcs_key_k_txt)
    event_components.time_chars_ign_text_changed(ui.enc_kcs_key_txt, chars.RU_ALPHABET, input_delay)
    event_components.time_chars_ign_text_changed(ui.dec_kcs_key_txt, chars.RU_ALPHABET, input_delay)
