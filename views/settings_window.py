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
        self.btn_program_info = QtWidgets.QPushButton(self.section_frame)
        self.btn_program_info.setGeometry(QtCore.QRect(0, 0, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_program_info.setFont(font)
        self.btn_program_info.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(77, 77, 77);\n"
"}")
        self.btn_program_info.setObjectName("btn_program_info")
        self.btn_color_style = QtWidgets.QPushButton(self.section_frame)
        self.btn_color_style.setGeometry(QtCore.QRect(0, 40, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_color_style.setFont(font)
        self.btn_color_style.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(77, 77, 77);\n"
"}")
        self.btn_color_style.setObjectName("btn_color_style")
        self.btn_privacy_policy = QtWidgets.QPushButton(self.section_frame)
        self.btn_privacy_policy.setGeometry(QtCore.QRect(0, 80, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_privacy_policy.setFont(font)
        self.btn_privacy_policy.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(77, 77, 77);\n"
"}")
        self.btn_privacy_policy.setObjectName("btn_privacy_policy")
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
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 751, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.section_widget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 751, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel {\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.section_widget.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.section_widget)

        self.retranslateUi(Form)
        self.section_widget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Настройки"))
        self.btn_program_info.setText(_translate("Form", "О приложении"))
        self.btn_color_style.setText(_translate("Form", "Цветовая схема"))
        self.btn_privacy_policy.setText(_translate("Form", "Политика конфиденциальности"))
        self.label.setText(_translate("Form", "MCrypt - программное обеспечение, позволяющее выполнять шифрование, дешифрование, хеширование и множество других преобразований быстро и эффективно. При этом, MCrypt позволяет просмотреть каждый шаг выполнения данных преобразований, а также содержит справочник по различным алгоритмам шифрования, применяемых в данном программном обеспечении, что позволяет более подробно рассмотреть различные процессы преобразования данных. Также MCrypt содержит множество различных алгоритмов шифрования, включая более сложные алгоритмы шифрования, предоставляя возможность автоматического заполнения параметров шифрования, что позволяет существенно сократить время на шифрование данных"))
        self.label_2.setText(_translate("Form", "Версия: MCrypt 1.9.1 Preview"))
        self.label_3.setText(_translate("Form", "©MCryptTeam, 2023, все права защищены"))
        self.label_4.setText(_translate("Form", "Цветовая схема позволяет настроить цветовое оформление элементов интерфейса приложения. Вы можете настроить отображение светлого или темного оформления, а также оформления Windows. Оформление Windows позволяет отображать цвета элементов в зависимости от настроек цветов Windows. Также вы можете выбрать автоматический режим смены цветового оформления в зависимости от времени суток"))
        self.label_5.setText(_translate("Form", "MCrypt - программное обеспечение, позволяющее выполнять различные преобразования данных в целях обеспечения безопасности и конфиденциальности данных, а также для безопасного способа их передачи и обмена. Данное программное обеспечение не хранит исходную информацию, предназначенную для ее передачи и обмена, поэтому после завершения работы приложения данная информация будет утеряна без возможности восстановления. В MCrypt пользовательские учетные данные хранятся в формате, не позволяющем получить к ним какой-либо доступ. Однако в случае утери каких-либо данных, MCryptTeam не несет никакой ответственности за утерю или получение доступа сторонних лиц к вашим данным"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
