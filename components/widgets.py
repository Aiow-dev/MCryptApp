from components import colors, palette


def central_widget_light(central_wgt_obj):
    central_wgt_stylesheet = f'''
    QWidget {{
        background-color: {colors.ColorSet.gray.value.to_rgb_str()};
    }}
    '''
    central_wgt_obj.setStyleSheet(central_wgt_stylesheet)


def frame_light(frame_obj):
    frame_stylesheet = f'''
    QFrame {{
        background-color: {colors.ColorSet.dark_purple.value.to_rgb_str()};
    }}
    '''
    frame_obj.setStyleSheet(frame_stylesheet)


def tab_widget_light(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.ColorSet.gray.value.to_rgb_str()};
    }}
    
    QTabBar::tab {{
        height: 25px;
        border: 1px solid {colors.ColorSet.dark_purple.value.to_rgb_str()};
        padding: 10 120px;
        background-color: {colors.ColorSet.dark_purple.value.to_rgb_str()};
        color: {colors.ColorSet.snow.value.to_rgb_str()};
    }}
    
    QTabBar::tab:selected {{
        border: 1px solid {colors.ColorSet.gray.value.to_rgb_str()};
        background-color: {colors.ColorSet.gray.value.to_rgb_str()};
        color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
    }}
    
    QTabBar::tab:hover {{
        border: 1px solid {colors.ColorSet.light_purple.value.to_rgb_str()};
        background-color: {colors.ColorSet.light_purple.value.to_rgb_str()};
        color: {colors.ColorSet.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def line_edit_light(line_edit_obj):
    line_edit_stylesheet = f'''
    QLineEdit {{
        border: 1px solid {colors.ColorSet.dark_purple.value.to_rgb_str()};
        border-radius: 3px;
        margin: 0 0 0 18px;
        padding: 0 3px;
        color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
    }}
    
    QLineEdit:focus {{
        border: 1px solid {colors.ColorSet.light_purple.value.to_rgb_str()};
    }}
    '''
    line_edit_obj.setStyleSheet(line_edit_stylesheet)


def text_edit_light(text_edit_obj):
    text_edit_stylesheet = f'''
    QTextEdit {{
        border: 1px solid {colors.ColorSet.dark_purple.value.to_rgb_str()};
        border-radius: 3px;
        padding: 0 3px;
        color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
    }}
    
    QTextEdit:focus {{
        border: 1px solid {colors.ColorSet.light_purple.value.to_rgb_str()};
    }}
    '''
    text_edit_obj.setStyleSheet(text_edit_stylesheet)


def menu_bar_dark(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
        background-color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
        color: {colors.ColorSet.white.value.to_rgb_str()};
    }}

    QMenuBar::item:selected {{
        background-color: {palette.windows_accent_color()};
    }}

    QMenu {{
        background-color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
        color: {colors.ColorSet.white.value.to_rgb_str()};
    }}

    QMenu::item:selected {{
        background-color: {palette.windows_accent_color()};
    }}
    '''
    menu_bar_obj.setStyleSheet(menu_bar_stylesheet)


def menu_bar_light(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
        background-color: {colors.ColorSet.gray.value.to_rgb_str()};
        color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
        border-bottom: 1px solid {colors.ColorSet.dark_purple.value.to_rgb_str()};
    }}

    QMenuBar::item:selected {{
        background-color: {colors.ColorSet.light_purple.value.to_rgb_str()};
        color: {colors.ColorSet.gray.value.to_rgb_str()};
    }}

    QMenu {{
        background-color: {colors.ColorSet.gray.value.to_rgb_str()};
        color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
    }}

    QMenu::item:selected {{
        background-color: {colors.ColorSet.light_purple.value.to_rgb_str()};
        color: {colors.ColorSet.gray.value.to_rgb_str()};
    }}
    '''
    menu_bar_obj.setStyleSheet(menu_bar_stylesheet)


def combo_box_light(combo_box_obj):
    combo_box_stylesheet = f'''
    QComboBox {{
        border: none;
        background-color: {colors.ColorSet.dark_purple.value.to_rgb_str()};
        color: {colors.ColorSet.snow.value.to_rgb_str()};
    }}
    
    QComboBox:hover {{
        background-color: {colors.ColorSet.light_purple.value.to_rgb_str()};
    }}
    
    QComboBox QAbstractItemView {{
        outline: none;
        background-color: {colors.ColorSet.snow.value.to_rgb_str()};
        color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
        selection-background-color: {colors.ColorSet.light_purple.value.to_rgb_str()};
    }}
    
    QComboBox::drop-down:button {{
        border: none;
    }}
    '''
    combo_box_obj.setStyleSheet(combo_box_stylesheet)


def label_light(label_obj):
    label_stylesheet = f'''
    QLabel {{
        color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
    }}
    '''
    label_obj.setStyleSheet(label_stylesheet)


def push_button_light(push_btn_obj):
    push_btn_stylesheet = f'''
    QPushButton {{
        border: 1px solid {colors.ColorSet.dark_purple.value.to_rgb_str()};
        border-radius: 3px;
        background-color: {colors.ColorSet.dark_purple.value.to_rgb_str()};
        color: {colors.ColorSet.snow.value.to_rgb_str()};
    }}
    
    QPushButton:hover {{
        border: 1px solid {colors.ColorSet.light_purple.value.to_rgb_str()};
        background-color: {colors.ColorSet.light_purple.value.to_rgb_str()};
    }}
    '''
    push_btn_obj.setStyleSheet(push_btn_stylesheet)


def table_widget_light(tbl_wgt_obj):
    table_stylesheet = f'''
    QTableWidget {{
        color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
        gridline-color: {colors.ColorSet.light_purple.value.to_rgb_str()};
        selection-background-color: {colors.ColorSet.logan.value.to_rgb_str()};
        selection-color: {colors.ColorSet.gray.value.to_rgb_str()};
    }}
    
    QHeaderView::section {{
        color: {colors.ColorSet.gray.value.to_rgb_str()};
        background-color: {colors.ColorSet.dark_purple.value.to_rgb_str()};
    }}
    
    QTableCornerButton::section {{
        background-color: {colors.ColorSet.dark_purple.value.to_rgb_str()};
    }}
    '''
    tbl_wgt_obj.setStyleSheet(table_stylesheet)


def check_box_light(check_box_obj):
    check_box_stylesheet = f'''
    QCheckBox {{
        color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
    }}
    
    QCheckBox::indicator:unchecked {{
        border: 1px solid {colors.ColorSet.dark_purple.value.to_rgb_str()};
        border-radius: 2px;
        background-color: {colors.ColorSet.gray.value.to_rgb_str()};
    }}
    
    QCheckBox::indicator:checked {{
        border: 1px solid {colors.ColorSet.light_purple.value.to_rgb_str()};
        border-radius: 2px;
        background-color: {colors.ColorSet.light_purple.value.to_rgb_str()};
    }}
    '''
    check_box_obj.setStyleSheet(check_box_stylesheet)
