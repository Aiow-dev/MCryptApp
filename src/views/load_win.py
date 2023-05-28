# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../src/views/templates/load_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_load_form(object):
    def setupUi(self, load_form):
        load_form.setObjectName("load_form")
        load_form.resize(1050, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(load_form.sizePolicy().hasHeightForWidth())
        load_form.setSizePolicy(sizePolicy)
        load_form.setStyleSheet("QWidget {\n"
"    background-color: rgb(252, 254, 252);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(load_form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.load_wgt = QtWidgets.QStackedWidget(load_form)
        self.load_wgt.setObjectName("load_wgt")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.btn_start_load = QtWidgets.QPushButton(self.page)
        self.btn_start_load.setGeometry(QtCore.QRect(755, 330, 201, 51))
        self.btn_start_load.setStyleSheet("QPushButton {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(244, 202, 22);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_start_load.setObjectName("btn_start_load")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.page)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(530, 220, 451, 91))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.plainTextEdit_3.setFont(font)
        self.plainTextEdit_3.setStyleSheet("QPlainTextEdit {\n"
"    border: none;\n"
"    color: rgb(48, 47, 47);\n"
"}")
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.lock_lbl = QtWidgets.QLabel(self.page)
        self.lock_lbl.setGeometry(QtCore.QRect(-100, 90, 498, 373))
        self.lock_lbl.setText("")
        self.lock_lbl.setScaledContents(True)
        self.lock_lbl.setObjectName("lock_lbl")
        self.btn_skip_load = QtWidgets.QPushButton(self.page)
        self.btn_skip_load.setGeometry(QtCore.QRect(545, 330, 201, 51))
        self.btn_skip_load.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(247, 211, 70);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(252, 254, 252);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_skip_load.setObjectName("btn_skip_load")
        self.load_wgt.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.load_wgt.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.load_wgt)

        self.retranslateUi(load_form)
        QtCore.QMetaObject.connectSlotsByName(load_form)

    def retranslateUi(self, load_form):
        _translate = QtCore.QCoreApplication.translate
        load_form.setWindowTitle(_translate("load_form", "Настройка MCrypt"))
        self.btn_start_load.setText(_translate("load_form", "Начать"))
        self.plainTextEdit_3.setPlainText(_translate("load_form", "Добро пожаловать в MCrypt! Давайте настроим это приложение для вас! Это займет не более 5 минут :)"))
        self.btn_skip_load.setText(_translate("load_form", "Пропустить настройку"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    load_form = QtWidgets.QWidget()
    ui = Ui_load_form()
    ui.setupUi(load_form)
    load_form.show()
    sys.exit(app.exec_())
