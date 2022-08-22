from View import main_window

from Scripts.TablePermutationScripts import SimplePermutation
from Scripts.TablePermutationScripts import UnSimplePermutation
from Scripts.TablePermutationScripts import KeyPermutation
from Scripts.TablePermutationScripts import UnKeyPermutation

from Scripts.CaesarScripts import Caesar_Classic
from Scripts.CaesarScripts import UnCaesar_Classic
from Scripts.CaesarScripts import Caesar_Afin
from Scripts.CaesarScripts import UnCaesar_Afin
from Scripts.CaesarScripts import Caesar_with_key
from Scripts.CaesarScripts import UnCaesar_with_key

from Core.Controllers import table_permutation_generic
from Core.Controllers import caesar_generic
from Core.Controllers import controllers_utilities


class ControllersWrapper:
    def __init__(self, ui: main_window.Ui_main_window):
        self.ui = ui

    def simple_permutation_encryption_handler(self):
        table_permutation_generic. \
            table_permutation_generic_handler(self.ui.enc_smp_msg_txt, self.ui.enc_smp_row_txt, self.ui.enc_smp_clm_txt,
                                              self.ui.enc_smp_oc_txt, self.ui.enc_smp_ot_txt,
                                              SimplePermutation.SimplePermutation)

    def un_simple_permutation_encryption_handler(self):
        table_permutation_generic. \
            table_permutation_generic_handler(self.ui.dec_smp_msg_txt, self.ui.dec_smp_row_txt,
                                              self.ui.dec_smp_clm_txt, self.ui.dec_smp_oc_txt,
                                              self.ui.dec_smp_ot_txt,
                                              UnSimplePermutation.UnSimplePermutation)

    def key_permutation_encryption_handler(self):
        table_permutation_generic. \
            table_key_permutation_generic_handler(self.ui.enc_kpm_msg_txt, self.ui.enc_kpm_row_txt,
                                                  self.ui.enc_kpm_clm_txt, self.ui.enc_kpm_key_txt,
                                                  self.ui.enc_kpm_oc_txt, KeyPermutation.KeyPermutation)

    def un_key_permutation_encryption_handler(self):
        table_permutation_generic. \
            table_key_permutation_generic_handler(self.ui.dec_kpm_msg_txt, self.ui.dec_kpm_row_txt,
                                                  self.ui.dec_kpm_clm_txt, self.ui.dec_kpm_key_txt,
                                                  self.ui.dec_kpm_oc_txt, UnKeyPermutation.UnKeyPermutation)

    def caesar_classic_encryption_handler(self):
        caesar_generic. \
            caesar_classic_generic_handler(self.ui.enc_cs_msg_txt, self.ui.enc_cs_key_txt,
                                           self.ui.enc_cs_oc_txt, self.ui.enc_cs_ot_txt,
                                           Caesar_Classic.Caesar_Classic)

    def un_caesar_classic_encryption_handler(self):
        caesar_generic. \
            caesar_classic_generic_handler(self.ui.dec_cs_msg_txt, self.ui.dec_cs_key_txt,
                                           self.ui.dec_cs_oc_txt, self.ui.dec_cs_ot_txt,
                                           UnCaesar_Classic.UnCaesar_Classic)

    def caesar_affine_encryption_handler(self):
        caesar_generic. \
            caesar_affine_generic_handler(self.ui.enc_acs_msg_txt, self.ui.enc_acs_key_a_txt,
                                          self.ui.enc_acs_key_b_txt, self.ui.enc_acs_oc_txt,
                                          self.ui.enc_acs_twn_table, self.ui.enc_acs_twl_table,
                                          Caesar_Afin.Caesar_Afin)

    def un_caesar_affine_encryption_handler(self):
        caesar_generic. \
            caesar_affine_generic_handler(self.ui.dec_acs_msg_txt, self.ui.dec_acs_key_a_txt,
                                          self.ui.dec_acs_key_b_txt, self.ui.dec_acs_oc_txt,
                                          self.ui.dec_acs_twn_table, self.ui.dec_acs_twl_table,
                                          UnCaesar_Afin.UnCaesar_Afin)

    def caesar_key_encryption_handler(self):
        caesar_generic.caesar_key_generic_handler(self.ui.enc_kcs_msg_txt, self.ui.enc_kcs_key_txt,
                                                  self.ui.enc_kcs_key_k_txt, self.ui.enc_kcs_oc_txt,
                                                  self.ui.enc_kcs_tsb_text,
                                                  self.ui.enc_kcs_wsb_table,
                                                  Caesar_with_key.Caesar_with_key)

    def un_caesar_key_encryption_handler(self):
        caesar_generic.caesar_key_generic_handler(self.ui.dec_kcs_msg_txt, self.ui.dec_kcs_key_txt,
                                                  self.ui.dec_kcs_key_k_txt, self.ui.dec_kcs_oc_txt,
                                                  self.ui.dec_kcs_tsb_text,
                                                  self.ui.dec_kcs_wsb_table,
                                                  UnCaesar_with_key.UnCaesar_with_key)

    def controller_binding(self) -> None:
        self.ui.enc_combo_box.activated.connect(
            lambda: controllers_utilities.page_combo_box(self.ui.enc_combo_box, self.ui.enc_widget)
        )

        self.ui.enc_smp_btn.clicked.connect(self.simple_permutation_encryption_handler)
        self.ui.dec_smp_btn.clicked.connect(self.un_simple_permutation_encryption_handler)

        self.ui.enc_kpm_btn.clicked.connect(self.key_permutation_encryption_handler)
        self.ui.dec_kpm_btn.clicked.connect(self.un_key_permutation_encryption_handler)

        self.ui.enc_cs_btn.clicked.connect(self.caesar_classic_encryption_handler)
        self.ui.dec_cs_btn.clicked.connect(self.un_caesar_classic_encryption_handler)

        self.ui.enc_acs_btn.clicked.connect(self.caesar_affine_encryption_handler)
        self.ui.dec_acs_btn.clicked.connect(self.un_caesar_affine_encryption_handler)

        self.ui.enc_kcs_btn.clicked.connect(self.caesar_key_encryption_handler)
        self.ui.dec_kcs_btn.clicked.connect(self.un_caesar_key_encryption_handler)
