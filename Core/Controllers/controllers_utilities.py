def number_text_handler_connect(text_obj, event_controllers_wrapper_obj):
    return text_obj.textChanged.connect(
        lambda: event_controllers_wrapper_obj.number_text_handler(text_obj)
    )


def number_text_handler_multi_connect(text_obj_list, event_controllers_wrapper_obj):
    for text_obj in text_obj_list:
        number_text_handler_connect(text_obj, event_controllers_wrapper_obj)


def page_combo_box(combo_box_obj, stacked_widget_obj):
    stacked_widget_obj.setCurrentIndex(combo_box_obj.currentIndex())
