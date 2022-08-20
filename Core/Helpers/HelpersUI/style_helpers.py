def set_style(ui_obj, ui_stylesheet):
    ui_obj.setStyleSheet(ui_stylesheet)


def set_menu_bar_background(menu_bar_obj, color):
    menu_bar_stylesheet = f'background-color: {color.value};'

    set_style(menu_bar_obj, menu_bar_stylesheet)
