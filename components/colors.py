import enum

from PyQt5.QtGui import QColor


class ConvertColor:
    def __init__(self, r, g, b):
        self.__r = r
        self.__g = g
        self.__b = b

    def get_r(self):
        return self.__r

    def get_g(self):
        return self.__g

    def get_b(self):
        return self.__b

    def set_r(self, r):
        if r >= 0:
            self.__r = r

    def set_g(self, g):
        if g >= 0:
            self.__g = g

    def set_b(self, b):
        if b >= 0:
            self.__b = b

    def to_rgb_str(self):
        return f'rgb({self.get_r()}, {self.get_g()}, {self.get_b()})'

    def to_rgb_q(self):
        return QColor(self.get_r(), self.get_g(), self.get_b())


class ColorSet(enum.Enum):
    dark_charcoal = ConvertColor(48, 47, 47)
    dark_liver = ConvertColor(77, 77, 77)
    orange_red = ConvertColor(255, 82, 82)
    white = ConvertColor(255, 255, 255)
    eerie_black = ConvertColor(30, 30, 30)
    snow = ConvertColor(250, 249, 249)
    navy = ConvertColor(63, 59, 108)
    dark_purple = ConvertColor(98, 79, 130)
    light_purple = ConvertColor(159, 115, 171)
    light_blue = ConvertColor(163, 199, 214)
    gray = ConvertColor(240, 243, 249)
