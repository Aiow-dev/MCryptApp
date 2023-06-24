from src.handlers.handbook import handbook_prm
from src.events import event_components


def init_handbook_smp(ui):
    write_enc_form = {'in_input': ui.hdk_enc_smp_in_txt, 'rows_input': ui.hdk_enc_smp_row_txt,
                      'columns_input': ui.hdk_enc_smp_clm_txt, 'tbl_write_wgt': ui.hdk_enc_smp_tbl,
                      'tbl_read_wgt': ui.hdk_enc_smp_tbl_2, 'btn_write': ui.hdk_enc_smp_btn,
                      'btn_read': ui.hdk_enc_smp_btn_2}
    read_enc_form = {'out_input': ui.hdk_enc_smp_out_txt, 'tbl_write_wgt': ui.hdk_enc_smp_tbl,
                     'tbl_read_wgt': ui.hdk_enc_smp_tbl_2, 'btn_write': ui.hdk_enc_smp_btn,
                     'btn_read': ui.hdk_enc_smp_btn_2, 'dec_in_input': ui.hdk_dec_smp_in_txt,
                     'rows_input': ui.hdk_enc_smp_row_txt, 'columns_input': ui.hdk_enc_smp_clm_txt,
                     'dec_rows_input': ui.hdk_dec_smp_row_txt, 'dec_columns_input': ui.hdk_dec_smp_clm_txt}
    write_dec_form = {'in_input': ui.hdk_dec_smp_in_txt, 'rows_input': ui.hdk_dec_smp_row_txt,
                      'columns_input': ui.hdk_dec_smp_clm_txt, 'tbl_write_wgt': ui.hdk_dec_smp_tbl,
                      'tbl_read_wgt': ui.hdk_dec_smp_tbl_2, 'btn_write': ui.hdk_dec_smp_btn,
                      'btn_read': ui.hdk_dec_smp_btn_2}
    read_dec_form = {'out_input': ui.hdk_dec_smp_out_txt, 'tbl_read_wgt': ui.hdk_dec_smp_tbl_2,
                     'btn_write': ui.hdk_dec_smp_btn, 'btn_read': ui.hdk_dec_smp_btn_2}
    ui.hdk_enc_smp_btn.clicked.connect(lambda: handbook_prm.proc_handbook_enc_write_smp(write_enc_form))
    ui.hdk_enc_smp_btn_2.clicked.connect(lambda: handbook_prm.proc_handbook_enc_read_smp(read_enc_form))
    ui.hdk_dec_smp_btn.clicked.connect(lambda: handbook_prm.proc_handbook_dec_write_smp(write_dec_form))
    ui.hdk_dec_smp_btn_2.clicked.connect(lambda: handbook_prm.proc_handbook_dec_read_smp(read_dec_form))
    event_components.empty_text_changed(ui.hdk_enc_smp_in_txt)
    event_components.empty_text_changed(ui.hdk_dec_smp_in_txt)
    event_components.positive_number_text_changed(ui.hdk_enc_smp_row_txt)
    event_components.positive_number_text_changed(ui.hdk_enc_smp_clm_txt)
    event_components.positive_number_text_changed(ui.hdk_dec_smp_row_txt)
    event_components.positive_number_text_changed(ui.hdk_dec_smp_clm_txt)
