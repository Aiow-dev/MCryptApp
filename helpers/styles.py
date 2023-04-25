def set_style(ui_obj, ui_stylesheet):
    ui_obj.setStyleSheet(ui_stylesheet)


def add_style(ui_obj, ui_stylesheet):
    default_stylesheet = ui_obj.styleSheet()
    set_style(ui_obj, f'{default_stylesheet}{ui_stylesheet}')


def set_border_color(ui_obj, color):
    style = f'border: 1px solid {color.value};'
    stylesheet = f'\n{ui_obj.__class__.__name__} {{\n{style}\n}}'
    add_style(ui_obj, stylesheet)
