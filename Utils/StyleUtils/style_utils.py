from Assets import styles

from Utils.StyleUtils import style_base_utils

from View import main_window


def set_menu_bar_dark_style(menu_bar_obj) -> None:
    menu_bar_stylesheet = f'''
    QMenuBar {{
    background-color: {styles.Color.dark_charcoal.value};
    color: {styles.Color.white.value};
    }}
    
    QMenuBar::item:selected {{
    background-color: {styles.Color.dark_liver.value};
    }}
    
    QMenu {{
    background-color: {styles.Color.dark_charcoal.value};
    color: {styles.Color.white.value};
    }}
    
    QMenu::item:selected {{
    background-color: {styles.Color.dark_liver.value};
    }}'''

    style_base_utils.set_style(menu_bar_obj, menu_bar_stylesheet)


def set_table_color(table_obj, color: styles.Color) -> None:
    table_stylesheet = f'''
    QTableWidget {{
    gridline-color: {color.value};
    }}
    
    QHeaderView::section {{
    background-color: {color.value};
    }}
    
    QTableCornerButton::section {{
    background-color: {color.value};
    }}
    '''

    style_base_utils.add_style(table_obj, table_stylesheet)


def set_tab_padding(tab_widget_obj, padding: str) -> None:
    tab_stylesheet = f'\nQTabBar::tab {{\npadding: {padding};\n}}'

    style_base_utils.add_style(tab_widget_obj, tab_stylesheet)


def set_line_edit_border_color(line_edit_obj, color: styles.Color) -> None:
    line_edit_border_stylesheet = f'\nQLineEdit {{\nborder: 1px solid {color.value};\n}}'

    style_base_utils.add_style(line_edit_obj, line_edit_border_stylesheet)


def set_tool_tip(ui_obj, tool_tip: str) -> None:
    ui_obj.setToolTip(tool_tip)


def styles_binding(ui: main_window.Ui_main_window) -> None:
    set_menu_bar_dark_style(ui.menu_bar)
