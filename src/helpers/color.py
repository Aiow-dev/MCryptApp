import math


def hex_to_rgb(color):
    dec_r = int(color[1:3], 16)
    dec_g = int(color[3:5], 16)
    dec_b = int(color[5:7], 16)
    return dec_r, dec_g, dec_b


def brighten(r, g, b):
    r = max(r, 30)
    g = max(g, 30)
    b = max(b, 30)
    brighten_r = math.floor(r * 1.1)
    brighten_g = math.floor(g * 1.1)
    brighten_b = math.floor(b * 1.1)
    brighten_r = min(brighten_r, 255)
    brighten_b = min(brighten_b, 255)
    brighten_g = min(brighten_g, 255)
    return brighten_r, brighten_g, brighten_b
