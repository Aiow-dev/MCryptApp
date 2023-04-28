def add_style(ui_obj, ui_stylesheet):
    default_stylesheet = ui_obj.styleSheet()
    ui_obj.setStyleSheet(default_stylesheet + ui_stylesheet)


def set_border_color(ui_obj, color):
    style = f'border: 1px solid {color};'
    stylesheet = f'\n{ui_obj.__class__.__name__} {{\n{style}\n}}'
    add_style(ui_obj, stylesheet)
