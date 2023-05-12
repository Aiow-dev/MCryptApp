import math


def hex_to_rgb(color):
    dec_r = int(color[1:3], 16)
    dec_g = int(color[3:5], 16)
    dec_b = int(color[5:7], 16)
    return dec_r, dec_g, dec_b


def brighten(r, g, b):
    r = r if r >= 30 else 30
    g = g if g >= 30 else 30
    b = b if b >= 30 else 30
    brighten_r = math.floor(r * 1.1)
    brighten_g = math.floor(g * 1.1)
    brighten_b = math.floor(b * 1.1)
    brighten_r = brighten_r if brighten_r <= 255 else 255
    brighten_b = brighten_b if brighten_b <= 255 else 255
    brighten_g = brighten_g if brighten_g <= 255 else 255
    return brighten_r, brighten_g, brighten_b
