import winreg


def is_light_win_theme():
    location = winreg.HKEY_CURRENT_USER
    key = winreg.OpenKeyEx(location, r'SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Themes\\Personalize')
    is_light = winreg.QueryValueEx(key, 'AppsUseLightTheme')
    if key:
        winreg.CloseKey(key)
    return bool(is_light[0])


def win_accent_color():
    location = winreg.HKEY_CURRENT_USER
    key = winreg.OpenKeyEx(location, r'SOFTWARE\\Microsoft\\Windows\\DWM')
    color = winreg.QueryValueEx(key, 'ColorizationColor')
    if key:
        winreg.CloseKey(key)
    hex_color = hex(color[0])
    color_index = 2 if len(hex_color) == 8 else 4
    return f'#{hex_color[color_index:]}'
