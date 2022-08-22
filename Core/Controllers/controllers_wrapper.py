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

from Core.Controllers import table_permutation_generic
from Core.Controllers import caesar_generic


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
            caesar_classic_generic_handler(self.ui.message_text_sc, self.ui.key_text_sc,
                                           self.ui.encrypt_message_text_sc,
                                           self.ui.encryption_table_text_sc,
                                           Caesar_Classic.Caesar_Classic)

    def un_caesar_classic_encryption_handler(self):
        caesar_generic. \
            caesar_classic_generic_handler(self.ui.un_message_text_sc, self.ui.un_key_text_sc,
                                           self.ui.un_encrypt_message_text_sc,
                                           self.ui.un_encryption_table_text_sc,
                                           UnCaesar_Classic.UnCaesar_Classic)

    def caesar_affine_encryption_handler(self):
        caesar_generic. \
            caesar_affine_generic_handler(self.ui.message_text_sca, self.ui.key_a_text_sca,
                                          self.ui.key_b_text_sca, self.ui.encrypt_message_text_sca,
                                          self.ui.encryption_table_number_text_sca,
                                          self.ui.encryption_table_letter_text_sca,
                                          self.ui.encryption_table_number_sca,
                                          self.ui.encryption_table_letter_sca,
                                          Caesar_Afin.Caesar_Afin)

    def un_caesar_affine_encryption_handler(self):
        caesar_generic. \
            caesar_affine_generic_handler(self.ui.un_message_text_sca, self.ui.un_key_a_text_sca,
                                          self.ui.un_key_b_text_sca, self.ui.un_encrypt_message_text_sca,
                                          self.ui.un_encryption_table_number_text_sca,
                                          self.ui.un_encryption_table_letter_text_sca,
                                          self.ui.un_encryption_table_number_sca,
                                          self.ui.un_encryption_table_letter_sca,
                                          UnCaesar_Afin.UnCaesar_Afin)

    def caesar_key_encryption_handler(self):
        caesar_generic.caesar_key_generic_handler(self.ui.message_text_sck, self.ui.key_word_text_sck,
                                                          self.ui.key_k_text_sck, self.ui.encrypt_message_text_sck,
                                                          self.ui.encryption_table_text_sck,
                                                          self.ui.encryption_table_sck,
                                                          Caesar_with_key.Caesar_with_key)
