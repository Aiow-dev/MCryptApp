from components import colors


def menu_bar_dark(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
    background-color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
    color: {colors.ColorSet.white.value.to_rgb_str()};
    }}

    QMenuBar::item:selected {{
    background-color: {colors.ColorSet.dark_liver.value.to_rgb_str()};
    }}

    QMenu {{
    background-color: {colors.ColorSet.dark_charcoal.value.to_rgb_str()};
    color: {colors.ColorSet.white.value.to_rgb_str()};
    }}

    QMenu::item:selected {{
    background-color: {colors.ColorSet.dark_liver.value.to_rgb_str()};
    }}'''

    menu_bar_obj.setStyleSheet(menu_bar_stylesheet)
