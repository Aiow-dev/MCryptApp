import json

from components import dialogs


def set_color_style(color_style):
    with open('settings.json', 'r+') as settings_file:
        text = settings_file.read()
        settings_file.seek(0)
        parsed_json = json.loads(text)
        parsed_json['theme'] = color_style
        json_str = json.dumps(parsed_json)
        settings_file.write(json_str)
        settings_file.truncate()
    return parsed_json.get('theme')


def light_color_style():
    dialogs.show_info_msg('Успешно применено светлое цветовое оформление!', 'Информация')
    set_color_style('light')


def dark_color_style():
    dialogs.show_info_msg('Успешно применено темное цветовое оформление!', 'Информация')
    set_color_style('dark')


def system_color_style():
    dialogs.show_info_msg('Успешно применено системное цветовое оформление!', 'Информация')
    set_color_style('system')


def time_color_style():
    dialogs.show_info_msg('Успешно применена автоматическая смена цветового оформления!', 'Информация')
    set_color_style('time')


def init_color_styles(ui):
    ui.light_btn.clicked.connect(light_color_style)
    ui.dark_btn.clicked.connect(dark_color_style)
    ui.win_btn.clicked.connect(system_color_style)
    ui.time_color_btn.clicked.connect(time_color_style)
