from Core.Helpers.HelpersUI import style_helpers


class EventControllersWrapper:
    def __init__(self, colors):
        self.colors = colors

    def number_text_handler(self, ui_obj):
        color = self.colors['default'] if ui_obj.text().isdigit() else self.colors['error']

        style_helpers.set_line_edit_border_color(ui_obj, color)
