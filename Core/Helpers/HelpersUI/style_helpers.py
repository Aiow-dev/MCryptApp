def set_style(ui_obj, ui_stylesheet):
    ui_obj.setStyleSheet(ui_stylesheet)


def add_style(ui_obj, ui_stylesheet):
    default_stylesheet = ui_obj.styleSheet()

    set_style(ui_obj, f'{default_stylesheet}{ui_stylesheet}')


def set_menu_bar_background(menu_bar_obj, color):
    menu_bar_stylesheet = f'background-color: {color.value};'

    set_style(menu_bar_obj, menu_bar_stylesheet)


def set_tab_padding(tab_widget_obj, padding):
    tab_stylesheet = f'\nQTabBar::tab {{\npadding: {padding};\n}}'

    add_style(tab_widget_obj, tab_stylesheet)
