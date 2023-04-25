from PyQt5.QtWidgets import QMessageBox


def show_err_msg(txt, title=''):
    msg = QMessageBox()
    msg.setText(txt)
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Critical)
    msg.exec()


def show_info_msg(txt, title=''):
    msg = QMessageBox()
    msg.setText(txt)
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Information)
    msg.exec()
