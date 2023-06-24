def init_page(ui):
    ui.enc_combo_box.currentIndexChanged.connect(lambda: page_combo_box(ui))


def page_combo_box(ui):
    ui.enc_widget.setCurrentIndex(ui.enc_combo_box.currentIndex())


def switch_page(ui, index):
    return lambda: ui.enc_combo_box.setCurrentIndex(index)


def set_page_combo_box(ui, index):
    ui.enc_widget.setCurrentIndex(index)
    ui.enc_combo_box.setCurrentIndex(index)


def to_page_combo_box(ui, index):
    return lambda: set_page_combo_box(ui, index)


def to_page(ui, index):
    ui.enc_widget.setCurrentIndex(index)


def to_next_page(ui):
    current_index = ui.enc_widget.currentIndex()
    ui.enc_widget.setCurrentIndex(current_index + 1)


def to_prev_page(ui):
    current_index = ui.enc_widget.currentIndex()
    ui.enc_widget.setCurrentIndex(current_index - 1)
