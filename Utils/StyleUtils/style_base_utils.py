def set_style(ui_obj, ui_stylesheet: str) -> None:
    ui_obj.setStyleSheet(ui_stylesheet)


def add_style(ui_obj, ui_stylesheet: str) -> None:
    default_stylesheet = ui_obj.styleSheet()

    set_style(ui_obj, f'{default_stylesheet}{ui_stylesheet}')
