from PyQt5.QtWidgets import QMessageBox


def show_err_msg(txt, title):
    msg = QMessageBox()
    msg.setText(txt)
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Critical)
    msg.exec()


def show_info_msg(txt, title):
    msg = QMessageBox()
    msg.setText(txt)
    msg.setWindowTitle(title)
    msg.setIcon(QMessageBox.Information)
    msg.exec()


def question_msg(parent, txt, title):
    result = QMessageBox.question(parent, title, txt, QMessageBox.Yes | QMessageBox.No)
    return result == QMessageBox.Yes
