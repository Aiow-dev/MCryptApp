from components import colors, win_palette


def frame_sys(frame_obj):
    frame_stylesheet = f'''
    QFrame {{
        background-color: {win_palette.accent_color};
    }}
    '''
    frame_obj.setStyleSheet(frame_stylesheet)


def tab_wgt_light_sys(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}
    
    QTabBar::tab {{
        height: 25px;
        border: 1px solid {win_palette.accent_color};
        padding: 10 120px;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    
    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.gray.value.to_rgb_str()};
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}
    
    QTabBar::tab:hover {{
        border: 1px solid {win_palette.complementary_color};
        background-color: {win_palette.complementary_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def line_edit_light_sys(line_edit_obj):
    line_edit_stylesheet = f'''
    QLineEdit {{
        border: 1px solid {win_palette.accent_color};
        border-radius: 3px;
        margin: 0 0 0 18px;
        padding: 0 3px;
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}
    
    QLineEdit:focus {{
        border: 1px solid {win_palette.complementary_color};
    }}
    '''
    line_edit_obj.setStyleSheet(line_edit_stylesheet)


def text_edit_light_sys(text_edit_obj):
    text_edit_stylesheet = f'''
    QTextEdit {{
        border: 1px solid {win_palette.accent_color};
        border-radius: 3px;
        padding: 0 3px;
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}
    
    QTextEdit:focus {{
        border: 1px solid {win_palette.complementary_color};
    }}
    '''
    text_edit_obj.setStyleSheet(text_edit_stylesheet)


def menu_bar_dark(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
        background-color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QMenuBar::item:selected {{
        background-color: {colors.Palette.dark_liver.value.to_rgb_str()};
    }}

    QMenu {{
        background-color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QMenu::item:selected {{
        background-color: {colors.Palette.dark_liver.value.to_rgb_str()};
    }}
    '''
    menu_bar_obj.setStyleSheet(menu_bar_stylesheet)


def menu_bar_dark_sys(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
        border-bottom: 1px solid {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}

    QMenuBar::item:selected {{
        background-color: {win_palette.complementary_color};
    }}

    QMenu {{
        background-color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QMenu::item:selected {{
        background-color: {win_palette.complementary_color};
    }}
    '''
    menu_bar_obj.setStyleSheet(menu_bar_stylesheet)


def menu_bar_light(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        border-bottom: 1px solid {colors.Palette.dark_purple.value.to_rgb_str()};
    }}

    QMenuBar::item:selected {{
        background-color: {colors.Palette.light_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QMenu {{
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}

    QMenu::item:selected {{
        background-color: {colors.Palette.light_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    menu_bar_obj.setStyleSheet(menu_bar_stylesheet)


def menu_bar_light_sys(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        border-bottom: 1px solid {win_palette.accent_color};
    }}

    QMenuBar::item:selected {{
        background-color: {win_palette.complementary_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QMenu {{
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}

    QMenu::item:selected {{
        background-color: {win_palette.complementary_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    menu_bar_obj.setStyleSheet(menu_bar_stylesheet)


def combo_box_light_sys(combo_box_obj):
    combo_box_stylesheet = f'''
    QComboBox {{
        border: none;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    
    QComboBox:hover {{
        background-color: {win_palette.complementary_color};
    }}
    
    QComboBox QAbstractItemView {{
        outline: none;
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        selection-background-color: {win_palette.complementary_color};
    }}
    
    QComboBox::drop-down:button {{
        border: none;
    }}
    '''
    combo_box_obj.setStyleSheet(combo_box_stylesheet)


def combo_box_dark_sys(combo_box_obj):
    combo_box_stylesheet = f'''
    QComboBox {{
        border: none;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QComboBox:hover {{
        background-color: {win_palette.complementary_color};
    }}

    QComboBox QAbstractItemView {{
        outline: none;
        background-color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
        selection-background-color: {win_palette.complementary_color};
    }}

    QComboBox::drop-down:button {{
        border: none;
    }}
    '''
    combo_box_obj.setStyleSheet(combo_box_stylesheet)


def label_light_sys(label_obj):
    label_stylesheet = f'''
    QLabel {{
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}
    '''
    label_obj.setStyleSheet(label_stylesheet)


def push_btn_sys(push_btn_obj):
    push_btn_stylesheet = f'''
    QPushButton {{
        border: 1px solid {win_palette.accent_color};
        border-radius: 3px;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    
    QPushButton:hover {{
        border: 1px solid {win_palette.complementary_color};
        background-color: {win_palette.complementary_color};
    }}
    '''
    push_btn_obj.setStyleSheet(push_btn_stylesheet)


def tbl_wgt_light_sys(tbl_wgt_obj):
    table_stylesheet = f'''
    QTableWidget {{
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        gridline-color: {win_palette.complementary_color};
        selection-background-color: {win_palette.complementary_color};
        selection-color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    
    QHeaderView::section {{
        color: {colors.Palette.gray.value.to_rgb_str()};
        background-color: {win_palette.accent_color};
    }}
    
    QTableCornerButton::section {{
        background-color: {win_palette.accent_color};
    }}
    '''
    tbl_wgt_obj.setStyleSheet(table_stylesheet)


def check_box_light_sys(check_box_obj):
    check_box_stylesheet = f'''
    QCheckBox {{
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}
    
    QCheckBox::indicator:unchecked {{
        border: 1px solid {win_palette.accent_color};
        border-radius: 2px;
        background-color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    
    QCheckBox::indicator:checked {{
        border: 1px solid {win_palette.complementary_color};
        border-radius: 2px;
        background-color: {win_palette.complementary_color};
    }}
    '''
    check_box_obj.setStyleSheet(check_box_stylesheet)
