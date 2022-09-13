from PyQt5.QtWidgets import QMessageBox


def show_error_message(txt: str, title: str = '') -> None:
    msg = QMessageBox()

    msg.setText(txt)
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Critical)
