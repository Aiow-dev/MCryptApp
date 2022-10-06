from View import main_window

from Scripts import simple_permutation
from Scripts import key_permutation

from Scripts import caesar

from Scripts import trisemus

from Scripts import vigenere

from Scripts import playfair

from Scripts.magic_square import enc_magic_square, dec_magic_square

from Controllers import trisemus_generic, table_permutation_generic, caesar_generic, vigenere_generic
from Controllers.magic_square_generic import magic_square_generic_handler

from Utils import controllers_utils


class ControllersWrapper:
    def __init__(self, ui: main_window.Ui_main_window):
        self.ui = ui

    def simple_permutation_encryption_handler(self):
        table_permutation_generic. \
            table_permutation_generic_handler(self.ui.enc_smp_msg_txt, self.ui.enc_smp_row_txt, self.ui.enc_smp_clm_txt,
                                              self.ui.enc_smp_oc_txt, self.ui.enc_smp_ot_txt,
                                              simple_permutation.enc_simple_permutation)

    def un_simple_permutation_encryption_handler(self):
        table_permutation_generic. \
            table_permutation_generic_handler(self.ui.dec_smp_msg_txt, self.ui.dec_smp_row_txt,
                                              self.ui.dec_smp_clm_txt, self.ui.dec_smp_oc_txt,
                                              self.ui.dec_smp_ot_txt,
                                              simple_permutation.dec_simple_permutation)

    def key_permutation_encryption_handler(self):
        table_permutation_generic. \
            table_key_permutation_generic_handler(self.ui.enc_kpm_msg_txt, self.ui.enc_kpm_row_txt,
                                                  self.ui.enc_kpm_clm_txt, self.ui.enc_kpm_key_txt,
                                                  self.ui.enc_kpm_oc_txt, self.ui.enc_kpm_ot_txt,
                                                  key_permutation.enc_key_permutation)

    def un_key_permutation_encryption_handler(self):
        table_permutation_generic. \
            table_key_permutation_generic_handler(self.ui.dec_kpm_msg_txt, self.ui.dec_kpm_row_txt,
                                                  self.ui.dec_kpm_clm_txt, self.ui.dec_kpm_key_txt,
                                                  self.ui.dec_kpm_oc_txt, self.ui.dec_kpm_ot_txt,
                                                  key_permutation.dec_key_permutation)

    def caesar_classic_encryption_handler(self):
        caesar_generic. \
            caesar_classic_generic_handler(self.ui.enc_cs_msg_txt, self.ui.enc_cs_key_txt,
                                           self.ui.enc_cs_oc_txt, self.ui.enc_cs_ot_txt,
                                           caesar.enc_classic_caesar)

    def un_caesar_classic_encryption_handler(self):
        caesar_generic. \
            caesar_classic_generic_handler(self.ui.dec_cs_msg_txt, self.ui.dec_cs_key_txt,
                                           self.ui.dec_cs_oc_txt, self.ui.dec_cs_ot_txt,
                                           caesar.dec_classic_caesar)

    def caesar_affine_encryption_handler(self):
        caesar_generic. \
            caesar_affine_generic_handler(self.ui.enc_acs_msg_txt, self.ui.enc_acs_key_a_txt,
                                          self.ui.enc_acs_key_b_txt, self.ui.enc_acs_oc_txt,
                                          self.ui.enc_acs_twn_table, self.ui.enc_acs_twl_table,
                                          caesar.enc_affine_caesar)

    def un_caesar_affine_encryption_handler(self):
        caesar_generic. \
            caesar_affine_generic_handler(self.ui.dec_acs_msg_txt, self.ui.dec_acs_key_a_txt,
                                          self.ui.dec_acs_key_b_txt, self.ui.dec_acs_oc_txt,
                                          self.ui.dec_acs_twn_table, self.ui.dec_acs_twl_table,
                                          caesar.dec_affine_caesar)

    def caesar_key_encryption_handler(self):
        caesar_generic.caesar_key_generic_handler(self.ui.enc_kcs_msg_txt, self.ui.enc_kcs_key_txt,
                                                  self.ui.enc_kcs_key_k_txt, self.ui.enc_kcs_oc_txt,
                                                  self.ui.enc_kcs_tsb_text, self.ui.enc_kcs_wsb_table,
                                                  caesar.enc_key_caesar)

    def un_caesar_key_encryption_handler(self):
        caesar_generic.caesar_key_generic_handler(self.ui.dec_kcs_msg_txt, self.ui.dec_kcs_key_txt,
                                                  self.ui.dec_kcs_key_k_txt, self.ui.dec_kcs_oc_txt,
                                                  self.ui.dec_kcs_tsb_text, self.ui.dec_kcs_wsb_table,
                                                  caesar.dec_key_caesar)

    def trisemus_enc_handler(self):
        trisemus_generic.trisemus_generic_handler(self.ui.enc_ts_msg_txt, self.ui.enc_ts_row_txt,
                                                  self.ui.enc_ts_clm_txt, self.ui.enc_ts_key_txt,
                                                  self.ui.enc_ts_oc_txt, self.ui.enc_ts_ot_txt,
                                                  trisemus.enc_trisemus)

    def un_trisemus_enc_handler(self):
        trisemus_generic.trisemus_generic_handler(self.ui.dec_ts_msg_txt, self.ui.dec_ts_row_txt,
                                                  self.ui.dec_ts_clm_txt, self.ui.dec_ts_key_txt,
                                                  self.ui.dec_ts_oc_txt, self.ui.dec_ts_ot_txt,
                                                  trisemus.dec_trisemus)

    def vigenere_enc_handler(self):
        vigenere_generic.vigenere_generic_handler(self.ui.enc_vs_msg_txt, self.ui.enc_vs_key_txt,
                                                  self.ui.enc_vs_oc_txt, self.ui.enc_vs_tsb_text,
                                                  self.ui.enc_vs_wsb_table, vigenere.enc_vigenere)

    def un_vigenere_enc_handler(self):
        vigenere_generic.vigenere_generic_handler(self.ui.dec_vs_msg_txt, self.ui.dec_vs_key_txt,
                                                  self.ui.dec_vs_oc_txt, self.ui.dec_vs_tsb_text,
                                                  self.ui.dec_vs_wsb_table, vigenere.dec_vigenere)
    
    def playfair_enc_handler(self):
        trisemus_generic.trisemus_generic_handler(self.ui.enc_ps_msg_txt, self.ui.enc_ps_row_txt,
                                                  self.ui.enc_ps_clm_txt, self.ui.enc_ps_key_txt,
                                                  self.ui.enc_ps_oc_txt, self.ui.enc_ps_ot_txt,
                                                  playfair.enc_playfair)

    def un_playfair_enc_handler(self):
        trisemus_generic.trisemus_generic_handler(self.ui.dec_ps_msg_txt, self.ui.dec_ps_row_txt,
                                                  self.ui.dec_ps_clm_txt, self.ui.dec_ps_key_txt,
                                                  self.ui.dec_ps_oc_txt, self.ui.dec_ps_ot_txt,
                                                  playfair.dec_playfair)

    def magic_square_enc_handler(self):
        magic_square_generic_handler(self.ui.enc_ms_msg_txt, self.ui.enc_ms_rank_txt,
                                     self.ui.enc_ms_tms_table, self.ui.enc_ms_oc_txt,
                                     self.ui.enc_ms_ot_table, enc_magic_square)

    def un_magic_square_enc_handler(self):
        magic_square_generic_handler(self.ui.dec_ms_msg_txt, self.ui.dec_ms_rank_txt,
                                     self.ui.dec_ms_tms_table, self.ui.dec_ms_oc_txt,
                                     self.ui.dec_ms_ot_table, dec_magic_square)

    def controller_binding(self) -> None:
        self.ui.enc_combo_box.currentIndexChanged.connect(
            lambda: controllers_utils.page_combo_box(self.ui.enc_combo_box, self.ui.enc_widget)
        )

        btn_functions = {
            self.ui.enc_smp_btn: self.simple_permutation_encryption_handler,
            self.ui.dec_smp_btn: self.un_simple_permutation_encryption_handler,
            self.ui.enc_kpm_btn: self.key_permutation_encryption_handler,
            self.ui.dec_kpm_btn: self.un_key_permutation_encryption_handler,
            self.ui.enc_cs_btn: self.caesar_key_encryption_handler,
            self.ui.dec_cs_btn: self.un_caesar_key_encryption_handler,
            self.ui.enc_acs_btn: self.caesar_affine_encryption_handler,
            self.ui.dec_acs_btn: self.un_caesar_affine_encryption_handler,
            self.ui.enc_kcs_btn: self.caesar_key_encryption_handler,
            self.ui.dec_kcs_btn: self.un_caesar_key_encryption_handler,
            self.ui.enc_ts_btn: self.trisemus_enc_handler,
            self.ui.dec_ts_btn: self.un_trisemus_enc_handler,
            self.ui.enc_vs_btn: self.vigenere_enc_handler,
            self.ui.dec_vs_btn: self.un_vigenere_enc_handler,
            self.ui.enc_ps_btn: self.playfair_enc_handler,
            self.ui.dec_ps_btn: self.un_playfair_enc_handler,
            self.ui.enc_ms_btn: self.magic_square_enc_handler,
            self.ui.dec_ms_btn: self.un_magic_square_enc_handler,
        }

        for btn, function in btn_functions.items():
            btn.clicked.connect(function)
