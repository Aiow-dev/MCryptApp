# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../views/templates/settings_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1066, 744)
        Form.setStyleSheet("QWidget {\n"
"    background-color: rgb(48, 47, 47);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.section_frame = QtWidgets.QFrame(Form)
        self.section_frame.setMinimumSize(QtCore.QSize(300, 0))
        self.section_frame.setStyleSheet("QFrame {\n"
"    background-color: rgb(30, 30, 30);\n"
"}")
        self.section_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.section_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.section_frame.setObjectName("section_frame")
        self.pushButton = QtWidgets.QPushButton(self.section_frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(77, 77, 77);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.section_frame)
        self.section_widget = QtWidgets.QStackedWidget(Form)
        self.section_widget.setObjectName("section_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(0, 10, 751, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(0, 290, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgb(30, 30, 30);\n"
"    border-radius: 3px;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setGeometry(QtCore.QRect(0, 330, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.section_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.section_widget.addWidget(self.page_2)
        self.horizontalLayout.addWidget(self.section_widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Настройки"))
        self.pushButton.setText(_translate("Form", "О приложении"))
        self.label.setText(_translate("Form", "MCrypt - программное обеспечение, позволяющее выполнять шифрование, дешифрование, хеширование и множество других преобразований быстро и эффективно. При этом MCrypt позволяет просмотреть каждый шаг выполнения данных преобразований, а также содержит справочник по различным алгоритмам шифрования, применяемых в данном программном обеспечении, что позволяет более подробно рассмотреть различные процессы преобразования данных. Также MCrypt содержит множество различных алгоритмов шифрования, включая более сложные алгоритмы шифрования, предоставляя возможность автоматического заполнения параметров шифрования, что позволяет существенно сократить время на шифрование данных"))
        self.label_2.setText(_translate("Form", "Версия: MCrypt 1.9.1 Preview"))
        self.label_3.setText(_translate("Form", "©MCryptTeam, 2023, все права защищены"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
