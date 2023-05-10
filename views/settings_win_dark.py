# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../views/templates/settings_win_dark.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_settings_form(object):
    def setupUi(self, settings_form):
        settings_form.setObjectName("settings_form")
        settings_form.resize(1060, 740)
        settings_form.setStyleSheet("QWidget {\n"
"    background-color: rgb(30, 30, 30);\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(settings_form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.section_frame = QtWidgets.QFrame(settings_form)
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
        font.setPointSize(8)
        self.btn_program_info.setFont(font)
        self.btn_program_info.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(240, 243, 249);\n"
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
        font.setPointSize(8)
        self.btn_color_style.setFont(font)
        self.btn_color_style.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(240, 243, 249);\n"
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
        font.setPointSize(8)
        self.btn_privacy_policy.setFont(font)
        self.btn_privacy_policy.setStyleSheet("QPushButton {\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(240, 243, 249);\n"
"    border: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(77, 77, 77);\n"
"}")
        self.btn_privacy_policy.setObjectName("btn_privacy_policy")
        self.horizontalLayout.addWidget(self.section_frame)
        self.section_widget = QtWidgets.QStackedWidget(settings_form)
        self.section_widget.setObjectName("section_widget")
        self.program_info_page = QtWidgets.QWidget()
        self.program_info_page.setObjectName("program_info_page")
        self.label = QtWidgets.QLabel(self.program_info_page)
        self.label.setGeometry(QtCore.QRect(0, 10, 751, 261))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel {\n"
"    color: rgb(240, 243, 249);\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.program_info_page)
        self.label_2.setGeometry(QtCore.QRect(0, 290, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {\n"
"    background-color: rgb(240, 243, 249);\n"
"    color: rgb(30, 30, 30);\n"
"    border-radius: 3px;\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.program_info_page)
        self.label_3.setGeometry(QtCore.QRect(0, 330, 751, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel {\n"
"    color: rgb(240, 243, 249);\n"
"}")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.section_widget.addWidget(self.program_info_page)
        self.color_style_page = QtWidgets.QWidget()
        self.color_style_page.setObjectName("color_style_page")
        self.label_4 = QtWidgets.QLabel(self.color_style_page)
        self.label_4.setGeometry(QtCore.QRect(0, 10, 751, 111))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("QLabel {\n"
"    color: rgb(240, 243, 249);\n"
"}")
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.frame = QtWidgets.QFrame(self.color_style_page)
        self.frame.setGeometry(QtCore.QRect(0, 150, 321, 201))
        self.frame.setStyleSheet("QFrame {\n"
"    border-radius: 5px;\n"
"    background-color: rgb(240, 243, 249);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(180, 160, 120, 30))
        self.frame_2.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(98, 79, 130);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(180, 120, 120, 30))
        self.frame_3.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(159, 115, 171);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel {\n"
"    color: rgb(48, 47, 47);\n"
"}")
        self.label_6.setObjectName("label_6")
        self.light_btn = QtWidgets.QPushButton(self.color_style_page)
        self.light_btn.setGeometry(QtCore.QRect(70, 370, 180, 45))
        self.light_btn.setMinimumSize(QtCore.QSize(130, 45))
        self.light_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.light_btn.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(98, 79, 130);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(98, 79, 130);\n"
"    color: rgb(240, 243, 249);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid rgb(159, 115, 171);\n"
"    background-color: rgb(159, 115, 171);\n"
"}")
        self.light_btn.setObjectName("light_btn")
        self.dark_btn = QtWidgets.QPushButton(self.color_style_page)
        self.dark_btn.setGeometry(QtCore.QRect(440, 370, 180, 45))
        self.dark_btn.setMinimumSize(QtCore.QSize(130, 45))
        self.dark_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.dark_btn.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(77, 77, 77);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(48, 47, 47);\n"
"    color: rgb(240, 243, 249);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(77, 77, 77);\n"
"}")
        self.dark_btn.setObjectName("dark_btn")
        self.frame_11 = QtWidgets.QFrame(self.color_style_page)
        self.frame_11.setGeometry(QtCore.QRect(370, 150, 321, 201))
        self.frame_11.setStyleSheet("QFrame {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(77, 77, 77);\n"
"    background-color: rgb(30, 30, 30);\n"
"}")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setGeometry(QtCore.QRect(180, 160, 120, 30))
        self.frame_12.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    border: none;\n"
"    background-color: rgb(48, 47, 47);\n"
"}")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setGeometry(QtCore.QRect(180, 120, 120, 30))
        self.frame_13.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    border: none;\n"
"    background-color: rgb(77, 77, 77);\n"
"}")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_9 = QtWidgets.QLabel(self.frame_11)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}")
        self.label_9.setObjectName("label_9")
        self.win_btn = QtWidgets.QPushButton(self.color_style_page)
        self.win_btn.setGeometry(QtCore.QRect(70, 660, 180, 45))
        self.win_btn.setMinimumSize(QtCore.QSize(130, 45))
        self.win_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.win_btn.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(98, 79, 130);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(98, 79, 130);\n"
"    color: rgb(240, 243, 249);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid rgb(159, 115, 171);\n"
"    background-color: rgb(159, 115, 171);\n"
"}")
        self.win_btn.setObjectName("win_btn")
        self.frame_4 = QtWidgets.QFrame(self.color_style_page)
        self.frame_4.setGeometry(QtCore.QRect(0, 440, 321, 201))
        self.frame_4.setStyleSheet("QFrame {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(77, 77, 77);\n"
"    background-color: rgb(240, 243, 249);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.accent_light_win_color = QtWidgets.QFrame(self.frame_4)
        self.accent_light_win_color.setGeometry(QtCore.QRect(20, 160, 120, 30))
        self.accent_light_win_color.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    border: none;\n"
"    background-color: rgb(98, 79, 130);\n"
"}")
        self.accent_light_win_color.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accent_light_win_color.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accent_light_win_color.setObjectName("accent_light_win_color")
        self.compl_light_win_color = QtWidgets.QFrame(self.frame_4)
        self.compl_light_win_color.setGeometry(QtCore.QRect(20, 120, 120, 30))
        self.compl_light_win_color.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    border: none;\n"
"    background-color: rgb(159, 115, 171);\n"
"}")
        self.compl_light_win_color.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.compl_light_win_color.setFrameShadow(QtWidgets.QFrame.Raised)
        self.compl_light_win_color.setObjectName("compl_light_win_color")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    color: rgb(48, 47, 47);\n"
"}")
        self.label_8.setObjectName("label_8")
        self.frame_17 = QtWidgets.QFrame(self.frame_4)
        self.frame_17.setGeometry(QtCore.QRect(160, 0, 161, 201))
        self.frame_17.setStyleSheet("QFrame {\n"
"    border-top-left-radius: 0;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 0;\n"
"    background-color: rgb(30, 30, 30);\n"
"}")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label_11 = QtWidgets.QLabel(self.frame_17)
        self.label_11.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}")
        self.label_11.setObjectName("label_11")
        self.compl_dark_win_color = QtWidgets.QFrame(self.frame_17)
        self.compl_dark_win_color.setGeometry(QtCore.QRect(20, 120, 120, 30))
        self.compl_dark_win_color.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    border: none;\n"
"    background-color: rgb(77, 77, 77);\n"
"}")
        self.compl_dark_win_color.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.compl_dark_win_color.setFrameShadow(QtWidgets.QFrame.Raised)
        self.compl_dark_win_color.setObjectName("compl_dark_win_color")
        self.accent_dark_win_color = QtWidgets.QFrame(self.frame_17)
        self.accent_dark_win_color.setGeometry(QtCore.QRect(20, 160, 120, 30))
        self.accent_dark_win_color.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    border: none;\n"
"    background-color: rgb(48, 47, 47);\n"
"}")
        self.accent_dark_win_color.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.accent_dark_win_color.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accent_dark_win_color.setObjectName("accent_dark_win_color")
        self.time_color_btn = QtWidgets.QPushButton(self.color_style_page)
        self.time_color_btn.setGeometry(QtCore.QRect(440, 660, 180, 45))
        self.time_color_btn.setMinimumSize(QtCore.QSize(130, 45))
        self.time_color_btn.setMaximumSize(QtCore.QSize(200, 16777215))
        self.time_color_btn.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(98, 79, 130);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(98, 79, 130);\n"
"    color: rgb(240, 243, 249);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 1px solid rgb(159, 115, 171);\n"
"    background-color: rgb(159, 115, 171);\n"
"}")
        self.time_color_btn.setObjectName("time_color_btn")
        self.frame_14 = QtWidgets.QFrame(self.color_style_page)
        self.frame_14.setGeometry(QtCore.QRect(370, 440, 321, 201))
        self.frame_14.setStyleSheet("QFrame {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(77, 77, 77);\n"
"    background-color: rgb(240, 243, 249);\n"
"}")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setGeometry(QtCore.QRect(20, 160, 120, 30))
        self.frame_15.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    border: none;\n"
"    background-color: rgb(98, 79, 130);\n"
"}")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setGeometry(QtCore.QRect(20, 120, 120, 30))
        self.frame_16.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    border: none;\n"
"    background-color: rgb(159, 115, 171);\n"
"}")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_10 = QtWidgets.QLabel(self.frame_14)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("QLabel {\n"
"    border: none;\n"
"    color: rgb(48, 47, 47);\n"
"}")
        self.label_10.setObjectName("label_10")
        self.frame_20 = QtWidgets.QFrame(self.frame_14)
        self.frame_20.setGeometry(QtCore.QRect(160, 0, 161, 201))
        self.frame_20.setStyleSheet("QFrame {\n"
"    border-top-left-radius: 0;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"    border-bottom-left-radius: 0;\n"
"    background-color: rgb(30, 30, 30);\n"
"}")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.label_12 = QtWidgets.QLabel(self.frame_20)
        self.label_12.setGeometry(QtCore.QRect(10, 10, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("QLabel {\n"
"    border: none;\n"
"}")
        self.label_12.setObjectName("label_12")
        self.frame_21 = QtWidgets.QFrame(self.frame_20)
        self.frame_21.setGeometry(QtCore.QRect(20, 120, 120, 30))
        self.frame_21.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    border: none;\n"
"    background-color: rgb(77, 77, 77);\n"
"}")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.frame_22 = QtWidgets.QFrame(self.frame_20)
        self.frame_22.setGeometry(QtCore.QRect(20, 160, 120, 30))
        self.frame_22.setStyleSheet("QFrame {\n"
"    border-radius: 3px;\n"
"    border: none;\n"
"    background-color: rgb(48, 47, 47);\n"
"}")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.section_widget.addWidget(self.color_style_page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(0, 10, 751, 441))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("QLabel {\n"
"    color: rgb(240, 243, 249);\n"
"}")
        self.label_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.section_widget.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.section_widget)

        self.retranslateUi(settings_form)
        self.section_widget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(settings_form)

    def retranslateUi(self, settings_form):
        _translate = QtCore.QCoreApplication.translate
        settings_form.setWindowTitle(_translate("settings_form", "Настройки"))
        self.btn_program_info.setText(_translate("settings_form", "О приложении"))
        self.btn_color_style.setText(_translate("settings_form", "Цветовая схема"))
        self.btn_privacy_policy.setText(_translate("settings_form", "Политика конфиденциальности"))
        self.label.setText(_translate("settings_form", "MCrypt - программное обеспечение, позволяющее выполнять шифрование, дешифрование, хеширование и множество других преобразований быстро и эффективно. При этом, MCrypt позволяет просмотреть каждый шаг выполнения данных преобразований, а также содержит справочник по различным алгоритмам шифрования, применяемых в данном программном обеспечении, что позволяет более подробно рассмотреть различные процессы преобразования данных. Также MCrypt содержит множество различных алгоритмов шифрования, включая более сложные алгоритмы шифрования, предоставляя возможность автоматического заполнения параметров шифрования, что позволяет существенно сократить время на шифрование данных"))
        self.label_2.setText(_translate("settings_form", "Версия: MCrypt 1.9.1 Preview"))
        self.label_3.setText(_translate("settings_form", "©MCryptTeam, 2023, все права защищены"))
        self.label_4.setText(_translate("settings_form", "Цветовая схема позволяет настроить цветовое оформление элементов интерфейса приложения. Вы можете настроить отображение светлого или темного оформления, а также оформления Windows. Оформление Windows позволяет отображать цвета элементов в зависимости от настроек цветов Windows. Также вы можете выбрать автоматический режим смены цветового оформления в зависимости от времени суток"))
        self.label_6.setText(_translate("settings_form", "☀"))
        self.light_btn.setText(_translate("settings_form", "Применить"))
        self.dark_btn.setText(_translate("settings_form", "Применить"))
        self.label_9.setText(_translate("settings_form", "🌙"))
        self.win_btn.setText(_translate("settings_form", "Применить"))
        self.label_8.setText(_translate("settings_form", "☀"))
        self.label_11.setText(_translate("settings_form", "🌙"))
        self.time_color_btn.setText(_translate("settings_form", "Применить"))
        self.label_10.setText(_translate("settings_form", "☀"))
        self.label_12.setText(_translate("settings_form", "🌙"))
        self.label_5.setText(_translate("settings_form", "MCrypt - программное обеспечение, позволяющее выполнять различные преобразования данных в целях обеспечения безопасности и конфиденциальности данных, а также для безопасного способа их передачи и обмена. Данное программное обеспечение не хранит исходную информацию, предназначенную для ее передачи и обмена, поэтому после завершения работы приложения данная информация будет утеряна без возможности восстановления. В MCrypt пользовательские учетные данные хранятся в формате, не позволяющем получить к ним какой-либо доступ. Однако в случае утери каких-либо данных, MCryptTeam не несет никакой ответственности за утерю или получение доступа сторонних лиц к вашим данным. ВАЖНО: Данное программное обеспечение предназначено для изучения различных методов шифрования и хеширования данных. Несмотря на то, что в MCrypt есть возможность шифровать и хешировать информацию, данные возможности, как правило, предназначены также для дополнительного и более подробного изучения. В MCrypt различные алгоритмы обладают достаточной степенью надежности, чтобы защитить ваши данные, однако мы настоятельно не рекомендуем использовать данное программное обеспечение, если вам действительно необходимо обеспечить реальную защиту данных!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    settings_form = QtWidgets.QWidget()
    ui = Ui_settings_form()
    ui.setupUi(settings_form)
    settings_form.show()
    sys.exit(app.exec_())