def init_page(ui):
    ui.enc_combo_box.currentIndexChanged.connect(lambda: page_combo_box(ui))


def page_combo_box(ui):
    ui.enc_widget.setCurrentIndex(ui.enc_combo_box.currentIndex())


def switch_page(ui, index):
    return lambda: ui.enc_combo_box.setCurrentIndex(index)
