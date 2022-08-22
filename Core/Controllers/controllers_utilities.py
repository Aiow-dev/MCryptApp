from typing import Dict

from Core.Controllers import event_controllers_wrapper
from Core.Helpers.HelpersUI import styles
from Core.Helpers.HelpersUI import style_helpers


def number_text_handler_connect(
        text_obj,
        event_controllers_wrapper_obj: event_controllers_wrapper.EventControllersWrapper
) -> None:
    text_obj.textChanged.connect(
        lambda: event_controllers_wrapper_obj.number_text_handler(text_obj)
    )


def number_text_handler_multi_connect(
        text_obj_list,
        event_controllers_wrapper_obj: event_controllers_wrapper.EventControllersWrapper
) -> None:
    for text_obj in text_obj_list:
        number_text_handler_connect(text_obj, event_controllers_wrapper_obj)


def page_combo_box(combo_box_obj, stacked_widget_obj):
    stacked_widget_obj.setCurrentIndex(combo_box_obj.currentIndex())


def multi_set_status_handler(text_obj_list, colors: Dict[str, styles.Color],
                             tool_tips: Dict[str, str], error_status: bool = False) -> None:
    color: styles.Color = colors['default']
    tool_tip: str = tool_tips['default']

    if error_status:
        color = colors['error']
        tool_tip = tool_tips['error']

    for text_obj in text_obj_list:
        style_helpers.set_line_edit_border_color(text_obj, color)
        style_helpers.set_tool_tip(text_obj, tool_tip)
