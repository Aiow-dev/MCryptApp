from typing import Dict

from Core.Helpers.HelpersUI import style_helpers
from Core.Helpers.HelpersUI import styles


class EventControllersWrapper:
    def __init__(self, colors: Dict[str, styles.Color]):
        self.colors = colors

    def number_text_handler(self, ui_obj):
        color: styles.Color = self.colors['default']
        tool_tip_text: str = ''

        if not ui_obj.text().isdigit():
            color = self.colors['error']
            tool_tip_text = 'Поле должно содержать только цифры'
        
        style_helpers.set_line_edit_border_color(ui_obj, color)
        ui_obj.setToolTip(tool_tip_text)
