from src.helpers import color, win
from src.components import colors


def win_accent_converted():
    accent = win.win_accent_color()
    r, g, b = color.hex_to_rgb(accent)
    return colors.ConvertedColor(r, g, b)


def win_complementary_converted(accent):
    r, g, b = color.brighten(accent.get_r(), accent.get_g(), accent.get_b())
    return colors.ConvertedColor(r, g, b)


accent_color = 'rgb(0, 120, 212)'
accent_transparent_color = 'rgba(0, 120, 212, 50)'
complementary_color = 'rgb(0, 147, 255)'
complementary_q_color = colors.ConvertedColor(0, 147, 255).to_rgb_q()
