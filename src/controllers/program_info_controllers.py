from src.helpers import func
from src.windows import ext_info


def init_program_info(parent, ui):
    func_single = func.FuncSingleCall()
    ui.ext_info_btn.clicked.connect(lambda: ext_info.show_settings_window(func_single, parent))
