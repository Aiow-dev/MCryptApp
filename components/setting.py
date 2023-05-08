import json

from components import colors


def app_theme():
    with open('settings.json') as settings_file:
        text = settings_file.read()
    parsed_json = json.loads(text)
    return parsed_json.get('theme')


def table_item_color():
    theme = app_theme()
    if theme == 'light':
        return colors.Palette.dark_charcoal.value.to_rgb_q()
    elif theme == 'dark':
        return colors.Palette.gray.value.to_rgb_q()


def table_item_background():
    theme = app_theme()
    if theme == 'light':
        return colors.Palette.gray.value.to_rgb_q()
    elif theme == 'dark':
        return colors.Palette.eerie_black.value.to_rgb_q()
