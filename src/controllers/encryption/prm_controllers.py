from src.handlers.encryption import prm_handlers
from src.events import event_components


def init_simple_permutation(ui):
    enc_form = {'msg_input': ui.enc_smp_msg_txt, 'rows_input': ui.enc_smp_row_txt,
                'columns_input': ui.enc_smp_clm_txt, 'enc_msg_input': ui.enc_smp_oc_txt,
                'enc_tbl_input': ui.enc_smp_ot_txt}
    dec_form = {'msg_input': ui.dec_smp_msg_txt, 'rows_input': ui.dec_smp_row_txt,
                'columns_input': ui.dec_smp_clm_txt, 'enc_msg_input': ui.dec_smp_oc_txt,
                'enc_tbl_input': ui.dec_smp_ot_txt}
    ui.enc_smp_btn.clicked.connect(lambda: prm_handlers.enc_proc_simple_prm(enc_form))
    ui.dec_smp_btn.clicked.connect(lambda: prm_handlers.dec_proc_simple_prm(dec_form))
    ui.enc_smp_auto_btn.clicked.connect(lambda: prm_handlers.auto_simple_prm(enc_form))
    event_components.empty_text_changed(ui.enc_smp_msg_txt)
    event_components.empty_text_changed(ui.dec_smp_msg_txt)
    event_components.positive_number_text_changed(ui.enc_smp_row_txt)
    event_components.positive_number_text_changed(ui.enc_smp_clm_txt)
    event_components.positive_number_text_changed(ui.dec_smp_row_txt)
    event_components.positive_number_text_changed(ui.dec_smp_clm_txt)


def init_key_permutation(ui):
    enc_form = {'msg_input': ui.enc_kpm_msg_txt, 'rows_input': ui.enc_kpm_row_txt,
                'columns_input': ui.enc_kpm_clm_txt, 'key_input': ui.enc_kpm_key_txt,
                'enc_msg_input': ui.enc_kpm_oc_txt, 'enc_tbl_input': ui.enc_kpm_ot_txt}
    dec_form = {'msg_input': ui.dec_kpm_msg_txt, 'rows_input': ui.dec_kpm_row_txt,
                'columns_input': ui.dec_kpm_clm_txt, 'key_input': ui.dec_kpm_key_txt,
                'enc_msg_input': ui.dec_kpm_oc_txt, 'enc_tbl_input': ui.dec_kpm_ot_txt}
    ui.enc_kpm_btn.clicked.connect(lambda: prm_handlers.enc_proc_key_prm(enc_form))
    ui.dec_kpm_btn.clicked.connect(lambda: prm_handlers.dec_proc_key_prm(dec_form))
    ui.enc_kpm_auto_btn.clicked.connect(lambda: prm_handlers.auto_key_prm(enc_form))
    event_components.empty_text_changed(ui.enc_kpm_msg_txt)
    event_components.empty_text_changed(ui.dec_kpm_msg_txt)
    event_components.empty_text_changed(ui.enc_kpm_key_txt)
    event_components.empty_text_changed(ui.dec_kpm_key_txt)
    event_components.positive_number_text_changed(ui.enc_kpm_row_txt)
    event_components.positive_number_text_changed(ui.enc_kpm_clm_txt)
    event_components.positive_number_text_changed(ui.dec_kpm_row_txt)
    event_components.positive_number_text_changed(ui.dec_kpm_clm_txt)


def init_double_permutation(ui):
    enc_form = {'msg_input': ui.enc_dpm_msg_txt, 'rows_input': ui.enc_dpm_row_txt,
                'columns_input': ui.enc_dpm_clm_txt, 'key_row_input': ui.enc_dpm_key_r_txt,
                'key_column_input': ui.enc_dpm_key_c_txt, 'enc_msg_input': ui.enc_dpm_oc_txt,
                'enc_tbl_input': ui.enc_dpm_ot_txt}
    dec_form = {'msg_input': ui.dec_dpm_msg_txt, 'rows_input': ui.dec_dpm_row_txt,
                'columns_input': ui.dec_dpm_clm_txt, 'key_row_input': ui.dec_dpm_key_r_txt,
                'key_column_input': ui.dec_dpm_key_c_txt, 'enc_msg_input': ui.dec_dpm_oc_txt,
                'enc_tbl_input': ui.dec_dpm_ot_txt}
    ui.enc_dpm_btn.clicked.connect(lambda: prm_handlers.enc_proc_double_prm(enc_form))
    ui.dec_dpm_btn.clicked.connect(lambda: prm_handlers.dec_proc_double_prm(dec_form))
    ui.enc_dpm_auto_btn.clicked.connect(lambda: prm_handlers.auto_double_prm(enc_form))
    event_components.empty_text_changed(ui.enc_dpm_msg_txt)
    event_components.empty_text_changed(ui.dec_dpm_msg_txt)
    event_components.empty_text_changed(ui.enc_dpm_key_r_txt)
    event_components.empty_text_changed(ui.enc_dpm_key_c_txt)
    event_components.empty_text_changed(ui.dec_dpm_key_r_txt)
    event_components.empty_text_changed(ui.dec_dpm_key_c_txt)
    event_components.positive_number_text_changed(ui.enc_dpm_row_txt)
    event_components.positive_number_text_changed(ui.enc_dpm_clm_txt)
    event_components.positive_number_text_changed(ui.dec_dpm_row_txt)
    event_components.positive_number_text_changed(ui.dec_dpm_clm_txt)
