from src.handlers.handbook import handbook_prm
from src.events import animation


def write_table(ui):
    timer = animation.TableAnimation(ui.hdk_enc_row_smp_tbl, 500)
    timer.write_column_symbols(ui.hdk_enc_row_smp_msg_txt)


def init_handbook_smp(ui):
    row_form = {'msg_input': ui.hdk_enc_row_smp_msg_txt, 'rows_input': ui.hdk_enc_row_tr_smp_txt,
                'columns_input': ui.hdk_enc_row_tc_smp_txt, 'tbl_row_wgt': ui.hdk_enc_row_smp_tbl,
                'tbl_clm_wgt': ui.hdk_enc_clm_smp_tbl, 'btn_row_input': ui.hdk_enc_row_smp_btn,
                'btn_clm_input': ui.hdk_enc_clm_smp_btn}
    clm_form = {'msg_input': ui.hdk_enc_clm_smp_msg_txt, 'tbl_wgt': ui.hdk_enc_clm_smp_tbl,
                'btn_clm_input': ui.hdk_enc_clm_smp_btn, 'btn_row_input': ui.hdk_enc_row_smp_btn}
    ui.hdk_enc_row_smp_btn.clicked.connect(lambda: handbook_prm.proc_handbook_row_smp(row_form))
    ui.hdk_enc_clm_smp_btn.clicked.connect(lambda: handbook_prm.proc_handbook_clm_smp(clm_form))
