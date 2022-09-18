from typing import Dict

from Controllers import event_controllers_wrapper

from Utils.StyleUtils import style_utils

from Assets import styles


def num_text_changed_connect(
        text_obj,
        event_controllers_wrapper_obj: event_controllers_wrapper.EventControllersWrapper
) -> None:
    text_obj.textChanged.connect(
        lambda: event_controllers_wrapper_obj.num_text_handler(text_obj)
    )


def num_text_changed_multi_connect(
        text_obj_list,
        event_controllers_wrapper_obj: event_controllers_wrapper.EventControllersWrapper
) -> None:
    for text_obj in text_obj_list:
        num_text_changed_connect(text_obj, event_controllers_wrapper_obj)


def text_changed_connect(
        text_obj,
        event_controllers_wrapper_obj: event_controllers_wrapper.EventControllersWrapper
) -> None:
    text_obj.textChanged.connect(
        lambda: event_controllers_wrapper_obj.text_handler(text_obj)
    )


def text_changed_multi_connect(
        text_obj_list,
        event_controllers_wrapper_obj: event_controllers_wrapper.EventControllersWrapper
) -> None:
    for text_obj in text_obj_list:
        text_changed_connect(text_obj, event_controllers_wrapper_obj)


def page_combo_box(combo_box_obj, stacked_widget_obj):
    stacked_widget_obj.setCurrentIndex(combo_box_obj.currentIndex())


def set_combo_box(combo_box_obj, item_index):
    combo_box_obj.setCurrentIndex(item_index)


def multi_set_status_handler(text_obj_list, colors: Dict[str, styles.Color],
                             tool_tips: Dict[str, str], error_status: bool = False) -> None:
    color: styles.Color = colors['default']
    tool_tip: str = tool_tips['default']

    if error_status:
        color = colors['error']
        tool_tip = tool_tips['error']

    for text_obj in text_obj_list:
        style_utils.set_line_edit_border_color(text_obj, color)
        style_utils.set_tool_tip(text_obj, tool_tip)
