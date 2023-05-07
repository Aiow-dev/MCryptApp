import winreg


def windows_accent_color():
    location = winreg.HKEY_CURRENT_USER
    key = winreg.OpenKeyEx(location, r'SOFTWARE\\Microsoft\\Windows\\DWM')
    color = winreg.QueryValueEx(key, 'ColorizationColor')
    if key:
        winreg.CloseKey(key)
    return f'#{hex(color[0])[4:]}'
