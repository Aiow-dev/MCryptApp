from components import colors
from helpers import styles


def menu_bar_dark(menu_bar_obj):
    menu_bar_stylesheet = f'''
    QMenuBar {{
    background-color: {colors.Color.dark_charcoal.value};
    color: {colors.Color.white.value};
    }}

    QMenuBar::item:selected {{
    background-color: {colors.Color.dark_liver.value};
    }}

    QMenu {{
    background-color: {colors.Color.dark_charcoal.value};
    color: {colors.Color.white.value};
    }}

    QMenu::item:selected {{
    background-color: {colors.Color.dark_liver.value};
    }}'''

    styles.set_style(menu_bar_obj, menu_bar_stylesheet)
