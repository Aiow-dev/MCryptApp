import enum
from typing import Dict

from PyQt5.QtGui import QColor


class Color(enum.Enum):
    dark_charcoal = 'rgb(48, 47, 47)'
    dark_liver = 'rgb(77, 77, 77)'
    orange_red = 'rgb(255, 82, 82)'
    white = 'rgb(255, 255, 255)'
    q_white = QColor(255, 255, 255)


DEFAULT_COLORS: Dict[str, Color] = {
    'default': Color.dark_charcoal,
    'error': Color.orange_red
}
