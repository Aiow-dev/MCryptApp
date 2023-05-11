import json

from components import colors


def get_app_theme():
    with open('settings.json') as settings_file:
        text = settings_file.read()
    parsed_json = json.loads(text)
    return parsed_json.get('theme')


def set_app_theme(color_style):
    with open('settings.json', 'r+') as settings_file:
        text = settings_file.read()
        settings_file.seek(0)
        parsed_json = json.loads(text)
        parsed_json['theme'] = color_style
        json_str = json.dumps(parsed_json)
        settings_file.write(json_str)
        settings_file.truncate()


def is_confirm_quit():
    with open('settings.json') as settings_file:
        text = settings_file.read()
    parsed_json = json.loads(text)
    return parsed_json.get('confirm-quit')


def set_confirm_quit(status):
    with open('settings.json', 'r+') as settings_file:
        text = settings_file.read()
        settings_file.seek(0)
        parsed_json = json.loads(text)
        parsed_json['confirm-quit'] = status
        json_str = json.dumps(parsed_json)
        settings_file.write(json_str)
        settings_file.truncate()


def get_table_item_color():
    theme = get_app_theme()
    if theme == 'light':
        return colors.Palette.dark_charcoal.value.to_rgb_q()
    elif theme == 'dark':
        return colors.Palette.gray.value.to_rgb_q()


def get_table_item_background():
    theme = get_app_theme()
    if theme == 'light':
        return colors.Palette.gray.value.to_rgb_q()
    elif theme == 'dark':
        return colors.Palette.eerie_black.value.to_rgb_q()
