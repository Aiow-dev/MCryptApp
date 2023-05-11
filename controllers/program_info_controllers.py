from helpers import func
from windows import ext_info


def init_program_info(parent, ui):
    func_single = func.FuncSingleCall()
    ui.ext_info_btn.clicked.connect(lambda: ext_info.show_settings_window(func_single, parent))
