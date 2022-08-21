from Core.Helpers.HelpersUI import style_helpers


def get_equal_tab_padding(tab_widget_obj, main_window_width):
    number_tabs = tab_widget_obj.count()

    tab_text_size = 108

    tab_v_padding = 10

    equal_tab_h_padding = ((main_window_width / number_tabs) - tab_text_size) / 2

    style_helpers.set_tab_padding(tab_widget_obj, f'{tab_v_padding} {equal_tab_h_padding}px')
