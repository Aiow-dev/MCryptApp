from src.components import colors, win_palette


def frame_sys(frame_obj):
    frame_stylesheet = f'''
    QFrame {{
        background-color: {win_palette.accent_color};
    }}
    '''
    frame_obj.setStyleSheet(frame_stylesheet)


def frame_color_style_sys(frame_obj):
    frame_stylesheet = f'''
    QFrame {{
        border-radius: 3px;
        border: none;
        background-color: {win_palette.accent_color};
    }}
    '''
    frame_obj.setStyleSheet(frame_stylesheet)


def frame_compl_color_style_sys(frame_obj):
    frame_stylesheet = f'''
    QFrame {{
        border-radius: 3px;
        border: none;
        background-color: {win_palette.complementary_color};
    }}
    '''
    frame_obj.setStyleSheet(frame_stylesheet)


def tab_wgt_light(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {colors.Palette.dark_purple.value.to_rgb_str()};
        padding: 10 120px;
        background-color: {colors.Palette.dark_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.gray.value.to_rgb_str()};
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        border: 1px solid {colors.Palette.light_purple.value.to_rgb_str()};
        background-color: {colors.Palette.light_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_wgt_light_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {colors.Palette.dark_purple.value.to_rgb_str()};
        border-radius: 5px;
        padding: 10 120px;
        background-color: {colors.Palette.dark_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.gray.value.to_rgb_str()};
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        border: 1px solid {colors.Palette.light_purple.value.to_rgb_str()};
        background-color: {colors.Palette.light_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_wgt_light_top_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {colors.Palette.dark_purple.value.to_rgb_str()};
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        padding: 10 120px;
        background-color: {colors.Palette.dark_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.gray.value.to_rgb_str()};
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        border: 1px solid {colors.Palette.light_purple.value.to_rgb_str()};
        background-color: {colors.Palette.light_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_wgt_light_corn_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {colors.Palette.dark_purple.value.to_rgb_str()};
        border-top-right-radius: 5px;
        padding: 10 120px;
        background-color: {colors.Palette.dark_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.gray.value.to_rgb_str()};
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        border: 1px solid {colors.Palette.light_purple.value.to_rgb_str()};
        background-color: {colors.Palette.light_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


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


def tab_set_light_sys(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 20px;
        border: 1px solid {win_palette.accent_color};
        padding: 10 40px;
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


def tab_wgt_light_sys_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {win_palette.accent_color};
        border-radius: 5px;
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


def tab_set_light_sys_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}
    
    QTabBar::tab {{
        height: 20px;
        border: 1px solid {win_palette.accent_color};
        border-radius: 5px;
        padding: 10 40px;
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


def tab_wgt_light_sys_top_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {win_palette.accent_color};
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
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


def tab_set_light_sys_top_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}
    
    QTabBar::tab {{
        height: 20px;
        border: 1px solid {win_palette.accent_color};
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        padding: 10 40px;
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


def tab_wgt_light_sys_corn_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {win_palette.accent_color};
        border-top-right-radius: 5px;
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


def tab_set_light_sys_corn_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}
    
    QTabBar::tab {{
        height: 20px;
        border: 1px solid {win_palette.accent_color};
        border-top-right-radius: 5px;
        padding: 10 40px;
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


def tab_wgt_dark(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.mine_shaft.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {colors.Palette.dark_liver.value.to_rgb_str()};
        padding: 10 120px;
        background-color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        background-color: {colors.Palette.tundora.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_wgt_dark_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.mine_shaft.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {colors.Palette.dark_liver.value.to_rgb_str()};
        border-radius: 5px;
        padding: 10 120px;
        background-color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        background-color: {colors.Palette.tundora.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_wgt_dark_top_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.mine_shaft.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {colors.Palette.dark_liver.value.to_rgb_str()};
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        padding: 10 120px;
        background-color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        background-color: {colors.Palette.tundora.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_wgt_dark_corn_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.mine_shaft.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {colors.Palette.dark_liver.value.to_rgb_str()};
        border-top-right-radius: 5px;
        padding: 10 120px;
        background-color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        background-color: {colors.Palette.tundora.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_wgt_dark_sys(tab_wgt_obj):
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
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        border: 1px solid {win_palette.complementary_color};
        background-color: {win_palette.complementary_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_set_dark_sys(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 20px;
        border: 1px solid {win_palette.accent_color};
        padding: 10 40px;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        border: 1px solid {win_palette.complementary_color};
        background-color: {win_palette.complementary_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_wgt_dark_sys_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {win_palette.accent_color};
        border-radius: 5px;
        padding: 10 120px;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        border: 1px solid {win_palette.complementary_color};
        background-color: {win_palette.complementary_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_set_dark_sys_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 20px;
        border: 1px solid {win_palette.accent_color};
        border-radius: 5px;
        padding: 10 40px;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        border: 1px solid {win_palette.complementary_color};
        background-color: {win_palette.complementary_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_wgt_dark_sys_top_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {win_palette.accent_color};
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        padding: 10 120px;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        border: 1px solid {win_palette.complementary_color};
        background-color: {win_palette.complementary_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_set_dark_sys_top_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 20px;
        border: 1px solid {win_palette.accent_color};
        border-top-left-radius: 5px;
        border-top-right-radius: 5px;
        padding: 10 40px;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        border: 1px solid {win_palette.complementary_color};
        background-color: {win_palette.complementary_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_wgt_dark_sys_corn_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 25px;
        border: 1px solid {win_palette.accent_color};
        border-top-right-radius: 5px;
        padding: 10 120px;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:hover {{
        border: 1px solid {win_palette.complementary_color};
        background-color: {win_palette.complementary_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    tab_wgt_obj.setStyleSheet(tab_stylesheet)


def tab_set_dark_sys_corn_rad(tab_wgt_obj):
    tab_stylesheet = f'''
    QTabWidget::pane {{
        background: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab {{
        height: 20px;
        border: 1px solid {win_palette.accent_color};
        border-top-right-radius: 5px;
        padding: 10 40px;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}

    QTabBar::tab:selected {{
        border: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
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
        selection-color: {colors.Palette.gray.value.to_rgb_str()};
        selection-background-color: {win_palette.complementary_color};
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
        selection-color: {colors.Palette.gray.value.to_rgb_str()};
        selection-background-color: {win_palette.complementary_color};
    }}
    
    QTextEdit:focus {{
        border: 1px solid {win_palette.complementary_color};
    }}
    '''
    text_edit_obj.setStyleSheet(text_edit_stylesheet)


def menu_bar_dark(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
        border-bottom: 1px solid {colors.Palette.dark_charcoal.value.to_rgb_str()};
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


def menu_bar_dark_color(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
        background-color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
        border-bottom: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
    }}

    QMenuBar::item:selected {{
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
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


def menu_bar_dark_color_sys(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
        border-bottom: 1px solid {colors.Palette.eerie_black.value.to_rgb_str()};
    }}

    QMenuBar::item:selected {{
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
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


def menu_bar_light_color(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
        background-color: {colors.Palette.dark_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
        border-bottom: 1px solid {colors.Palette.gray.value.to_rgb_str()};
    }}

    QMenuBar::item:selected {{
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
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


def menu_bar_light_color_sys(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
        border-bottom: 1px solid {colors.Palette.gray.value.to_rgb_str()};
    }}

    QMenuBar::item:selected {{
        background-color: {colors.Palette.gray.value.to_rgb_str()};
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
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


def panel_push_btn_light_sys(push_btn_obj):
    push_btn_stylesheet = f'''
    QPushButton {{
        border: none;
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}

    QPushButton:hover {{
        border: 1px solid {win_palette.complementary_color};
        background-color: {win_palette.complementary_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    '''
    push_btn_obj.setStyleSheet(push_btn_stylesheet)


def panel_push_btn_dark_sys(push_btn_obj):
    push_btn_stylesheet = f'''
    QPushButton {{
        border: none;
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


def frame_bottom_sys(frame_obj):
    frame_stylesheet = f'''
    QFrame {{
        border-radius: 0px;
        border: none;
        border-bottom: 1px solid {win_palette.accent_color};
    }}
    '''
    frame_obj.setStyleSheet(frame_stylesheet)


def label_back_light_sys(label_obj):
    label_stylesheet = f'''
    QLabel {{
        border: none;
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}
    
    QLabel:hover {{
        color: {colors.Palette.gray.value.to_rgb_str()};
        background-color: {win_palette.complementary_color};
    }}
    '''
    label_obj.setStyleSheet(label_stylesheet)


def label_back_dark_sys(label_obj):
    label_stylesheet = f'''
    QLabel {{
        border: none;
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    
    QLabel:hover {{
        color: {colors.Palette.gray.value.to_rgb_str()};
        background-color: {win_palette.complementary_color};
    }}
    '''
    label_obj.setStyleSheet(label_stylesheet)


def frame_bottom_color_sys(frame_obj):
    frame_stylesheet = f'''
    QFrame {{
        border-radius: 0px;
        background-color: {win_palette.accent_color};
    }}
    '''
    frame_obj.setStyleSheet(frame_stylesheet)


def msg_box_light():
    return f'''
    QMessageBox {{
        background-color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    QMessageBox QLabel {{
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}
    QMessageBox QPushButton {{
        border: none;
        border-radius: 3px;
        width: 105px;
        height: 30px;
        background-color: {colors.Palette.dark_purple.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    QMessageBox QPushButton:hover {{
        background-color: {colors.Palette.light_purple.value.to_rgb_str()};
    }}
    '''


def msg_box_light_sys():
    return f'''
    QMessageBox {{
        background-color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    QMessageBox QLabel {{
        color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
    }}
    QMessageBox QPushButton {{
        border: none;
        border-radius: 3px;
        width: 105px;
        height: 30px;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    QMessageBox QPushButton:hover {{
        background-color: {win_palette.complementary_color};
    }}
    '''


def msg_box_dark():
    return f'''
    QMessageBox {{
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
    }}
    QMessageBox QLabel {{
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    QMessageBox QPushButton {{
        border: 1px solid {colors.Palette.dark_liver.value.to_rgb_str()};
        border-radius: 3px;
        width: 105px;
        height: 30px;
        background-color: {colors.Palette.dark_charcoal.value.to_rgb_str()};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    QMessageBox QPushButton:hover {{
        background-color: {colors.Palette.dark_liver.value.to_rgb_str()};
    }}
    '''


def msg_box_dark_sys():
    return f'''
    QMessageBox {{
        background-color: {colors.Palette.eerie_black.value.to_rgb_str()};
    }}
    QMessageBox QLabel {{
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    QMessageBox QPushButton {{
        border: none;
        border-radius: 3px;
        width: 105px;
        height: 30px;
        background-color: {win_palette.accent_color};
        color: {colors.Palette.gray.value.to_rgb_str()};
    }}
    QMessageBox QPushButton:hover {{
        background-color: {win_palette.complementary_color};
    }}
    '''
