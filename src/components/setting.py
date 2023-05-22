import json
import pathlib

from src.components import colors


def get_parameter(parameter):
    text = pathlib.Path('../settings.json').read_text()
    parsed_json = json.loads(text)
    return parsed_json.get(parameter)


def set_parameter(parameter, value):
    with open('../settings.json', 'r+') as settings_file:
        text = settings_file.read()
        settings_file.seek(0)
        parsed_json = json.loads(text)
        parsed_json[parameter] = value
        json_str = json.dumps(parsed_json)
        settings_file.write(json_str)
        settings_file.truncate()


def get_table_item_color():
    theme = get_parameter('theme')
    if theme == 'light':
        return colors.Palette.dark_charcoal.value.to_rgb_q()
    elif theme == 'dark':
        return colors.Palette.gray.value.to_rgb_q()


def get_table_item_background():
    theme = get_parameter('theme')
    if theme == 'light':
        return colors.Palette.gray.value.to_rgb_q()
    elif theme == 'dark':
        return colors.Palette.eerie_black.value.to_rgb_q()
