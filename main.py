import sys

from PyQt5.QtWidgets import QApplication

from View import main_window

from Core.Helpers.HelpersUI import style_helpers
from Core.Helpers.HelpersUI import styles
from Core.Helpers.HelpersUI import widgets

from Core.Controllers import controllers_wrapper
from Core.Controllers import event_controllers_wrapper
from Core.Controllers import controllers_utilities


def styles_binding(ui):
    style_helpers.set_menu_bar_background(ui.menu_bar, styles.Color.dark_charcoal)


def controller_binding(ui, controllers_wrapper_obj):
    ui.enc_smp_btn.clicked.connect(controllers_wrapper_obj.simple_permutation_encryption_handler)
    ui.dec_smp_btn.clicked.connect(controllers_wrapper_obj.un_simple_permutation_encryption_handler)

    ui.enc_combo_box.activated.connect(
        lambda: controllers_utilities.page_combo_box(ui.enc_combo_box, ui.enc_widget)
    )


def event_controller_binding(ui, event_controllers_wrapper_obj):
    text_obj_list = [
        ui.enc_smp_row_txt, ui.enc_smp_clm_txt,
        ui.dec_smp_row_txt, ui.dec_smp_clm_txt,
    ]

    controllers_utilities.number_text_handler_multi_connect(
        text_obj_list, event_controllers_wrapper_obj
    )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = main_window.Ui_main_window()
    MainWindow = widgets.Window(ui)
    ui.setupUi(MainWindow)
    MainWindow.show()

    styles_binding(ui)

    controllers_wrapper_obj = controllers_wrapper.ControllersWrapper(ui)

    controller_binding(ui, controllers_wrapper_obj)

    colors = {'default': styles.Color.dark_charcoal, 'error': styles.Color.orange_red}

    event_controllers_wrapper_obj = event_controllers_wrapper.EventControllersWrapper(colors)

    event_controller_binding(ui, event_controllers_wrapper_obj)

    sys.exit(app.exec_())
