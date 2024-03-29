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
        self.btn_start_load.setGeometry(QtCore.QRect(755, 330, 171, 45))
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
        self.lock_lbl.setScaledContents(False)
        self.lock_lbl.setObjectName("lock_lbl")
        self.btn_skip_load = QtWidgets.QPushButton(self.page)
        self.btn_skip_load.setGeometry(QtCore.QRect(575, 330, 171, 45))
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
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(320, 90, 321, 201))
        self.frame.setStyleSheet("QFrame {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(98, 79, 130);\n"
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
"    border: none;\n"
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
"    border: none;\n"
"    color: rgb(48, 47, 47);\n"
"}")
        self.label_6.setObjectName("label_6")
        self.frame_11 = QtWidgets.QFrame(self.page_2)
        self.frame_11.setGeometry(QtCore.QRect(700, 90, 321, 201))
        self.frame_11.setStyleSheet("QFrame {\n"
"    border-radius: 5px;\n"
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
        self.frame_4 = QtWidgets.QFrame(self.page_2)
        self.frame_4.setGeometry(QtCore.QRect(320, 380, 321, 201))
        self.frame_4.setStyleSheet("QFrame {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(98, 79, 130);\n"
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
"    border: none;\n"
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
        self.frame_14 = QtWidgets.QFrame(self.page_2)
        self.frame_14.setGeometry(QtCore.QRect(700, 380, 321, 201))
        self.frame_14.setStyleSheet("QFrame {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(98, 79, 130);\n"
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
"    border: none;\n"
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
        self.label = QtWidgets.QLabel(self.page_2)
        self.label.setGeometry(QtCore.QRect(320, 30, 701, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(-150, 120, 441, 373))
        self.label_2.setText("")
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.btn_next_style = QtWidgets.QPushButton(self.page_2)
        self.btn_next_style.setGeometry(QtCore.QRect(166, 510, 130, 45))
        self.btn_next_style.setMinimumSize(QtCore.QSize(130, 45))
        self.btn_next_style.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_next_style.setStyleSheet("QPushButton {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(244, 202, 22);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_next_style.setObjectName("btn_next_style")
        self.btn_back_style = QtWidgets.QPushButton(self.page_2)
        self.btn_back_style.setGeometry(QtCore.QRect(25, 510, 130, 45))
        self.btn_back_style.setMinimumSize(QtCore.QSize(130, 45))
        self.btn_back_style.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_back_style.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(247, 211, 70);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(252, 254, 252);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_back_style.setObjectName("btn_back_style")
        self.light_style_lbl = QtWidgets.QLabel(self.page_2)
        self.light_style_lbl.setGeometry(QtCore.QRect(410, 315, 141, 21))
        self.light_style_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.light_style_lbl.setObjectName("light_style_lbl")
        self.light_style_btn = QtWidgets.QPushButton(self.page_2)
        self.light_style_btn.setGeometry(QtCore.QRect(305, 76, 350, 230))
        self.light_style_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(247, 211, 70, 50);\n"
"}")
        self.light_style_btn.setText("")
        self.light_style_btn.setObjectName("light_style_btn")
        self.dark_style_lbl = QtWidgets.QLabel(self.page_2)
        self.dark_style_lbl.setGeometry(QtCore.QRect(790, 315, 141, 21))
        self.dark_style_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.dark_style_lbl.setObjectName("dark_style_lbl")
        self.dark_style_btn = QtWidgets.QPushButton(self.page_2)
        self.dark_style_btn.setGeometry(QtCore.QRect(685, 76, 350, 230))
        self.dark_style_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(247, 211, 70, 50);\n"
"}")
        self.dark_style_btn.setText("")
        self.dark_style_btn.setObjectName("dark_style_btn")
        self.system_style_btn = QtWidgets.QPushButton(self.page_2)
        self.system_style_btn.setGeometry(QtCore.QRect(305, 365, 350, 230))
        self.system_style_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(247, 211, 70, 50);\n"
"}")
        self.system_style_btn.setText("")
        self.system_style_btn.setObjectName("system_style_btn")
        self.time_style_btn = QtWidgets.QPushButton(self.page_2)
        self.time_style_btn.setGeometry(QtCore.QRect(685, 365, 350, 230))
        self.time_style_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(247, 211, 70, 50);\n"
"}")
        self.time_style_btn.setText("")
        self.time_style_btn.setObjectName("time_style_btn")
        self.system_style_lbl = QtWidgets.QLabel(self.page_2)
        self.system_style_lbl.setGeometry(QtCore.QRect(390, 605, 171, 21))
        self.system_style_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.system_style_lbl.setObjectName("system_style_lbl")
        self.time_style_lbl = QtWidgets.QLabel(self.page_2)
        self.time_style_lbl.setGeometry(QtCore.QRect(780, 605, 161, 21))
        self.time_style_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.time_style_lbl.setObjectName("time_style_lbl")
        self.time_style_btn.raise_()
        self.system_style_btn.raise_()
        self.dark_style_btn.raise_()
        self.light_style_btn.raise_()
        self.frame.raise_()
        self.frame_11.raise_()
        self.frame_4.raise_()
        self.frame_14.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.btn_next_style.raise_()
        self.btn_back_style.raise_()
        self.light_style_lbl.raise_()
        self.dark_style_lbl.raise_()
        self.system_style_lbl.raise_()
        self.time_style_lbl.raise_()
        self.load_wgt.addWidget(self.page_2)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.profile_lbl = QtWidgets.QLabel(self.page_4)
        self.profile_lbl.setGeometry(QtCore.QRect(-105, 120, 441, 373))
        self.profile_lbl.setText("")
        self.profile_lbl.setScaledContents(False)
        self.profile_lbl.setObjectName("profile_lbl")
        self.btn_back_account = QtWidgets.QPushButton(self.page_4)
        self.btn_back_account.setGeometry(QtCore.QRect(25, 510, 130, 45))
        self.btn_back_account.setMinimumSize(QtCore.QSize(130, 45))
        self.btn_back_account.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_back_account.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(247, 211, 70);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(252, 254, 252);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_back_account.setObjectName("btn_back_account")
        self.btn_next_account = QtWidgets.QPushButton(self.page_4)
        self.btn_next_account.setGeometry(QtCore.QRect(166, 510, 130, 45))
        self.btn_next_account.setMinimumSize(QtCore.QSize(130, 45))
        self.btn_next_account.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_next_account.setStyleSheet("QPushButton {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(244, 202, 22);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_next_account.setObjectName("btn_next_account")
        self.account_wgt = QtWidgets.QStackedWidget(self.page_4)
        self.account_wgt.setGeometry(QtCore.QRect(350, 119, 611, 461))
        self.account_wgt.setObjectName("account_wgt")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.label_3 = QtWidgets.QLabel(self.page_5)
        self.label_3.setGeometry(QtCore.QRect(150, 40, 311, 21))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.registration_username_txt = QtWidgets.QLineEdit(self.page_5)
        self.registration_username_txt.setGeometry(QtCore.QRect(100, 110, 391, 45))
        self.registration_username_txt.setMinimumSize(QtCore.QSize(0, 45))
        self.registration_username_txt.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(48, 47, 47);\n"
"    border-radius: 3px;\n"
"    margin: 0 0 0 18px;\n"
"    padding: 0 3px;\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(244, 202, 22);\n"
"    background-color: rgb(244, 202, 22);\n"
"}")
        self.registration_username_txt.setClearButtonEnabled(True)
        self.registration_username_txt.setObjectName("registration_username_txt")
        self.registration_password_txt = QtWidgets.QLineEdit(self.page_5)
        self.registration_password_txt.setGeometry(QtCore.QRect(100, 180, 391, 45))
        self.registration_password_txt.setMinimumSize(QtCore.QSize(0, 45))
        self.registration_password_txt.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(48, 47, 47);\n"
"    border-radius: 3px;\n"
"    margin: 0 0 0 18px;\n"
"    padding: 0 3px;\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(244, 202, 22);\n"
"    background-color: rgb(244, 202, 22);\n"
"}")
        self.registration_password_txt.setClearButtonEnabled(True)
        self.registration_password_txt.setObjectName("registration_password_txt")
        self.registration_confirm_password_txt = QtWidgets.QLineEdit(self.page_5)
        self.registration_confirm_password_txt.setGeometry(QtCore.QRect(100, 250, 391, 45))
        self.registration_confirm_password_txt.setMinimumSize(QtCore.QSize(0, 45))
        self.registration_confirm_password_txt.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(48, 47, 47);\n"
"    border-radius: 3px;\n"
"    margin: 0 0 0 18px;\n"
"    padding: 0 3px;\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(244, 202, 22);\n"
"    background-color: rgb(244, 202, 22);\n"
"}")
        self.registration_confirm_password_txt.setClearButtonEnabled(True)
        self.registration_confirm_password_txt.setObjectName("registration_confirm_password_txt")
        self.btn_registration = QtWidgets.QPushButton(self.page_5)
        self.btn_registration.setGeometry(QtCore.QRect(225, 330, 161, 45))
        self.btn_registration.setStyleSheet("QPushButton {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(244, 202, 22);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_registration.setObjectName("btn_registration")
        self.btn_login_page = QtWidgets.QPushButton(self.page_5)
        self.btn_login_page.setGeometry(QtCore.QRect(120, 400, 371, 31))
        self.btn_login_page.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(247, 211, 70, 50);\n"
"}")
        self.btn_login_page.setObjectName("btn_login_page")
        self.account_wgt.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.label_4 = QtWidgets.QLabel(self.page_6)
        self.label_4.setGeometry(QtCore.QRect(150, 70, 311, 21))
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btn_login = QtWidgets.QPushButton(self.page_6)
        self.btn_login.setGeometry(QtCore.QRect(225, 290, 161, 45))
        self.btn_login.setStyleSheet("QPushButton {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(244, 202, 22);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_login.setObjectName("btn_login")
        self.btn_registration_page = QtWidgets.QPushButton(self.page_6)
        self.btn_registration_page.setGeometry(QtCore.QRect(120, 360, 371, 31))
        self.btn_registration_page.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(247, 211, 70, 50);\n"
"}")
        self.btn_registration_page.setObjectName("btn_registration_page")
        self.login_username_txt = QtWidgets.QLineEdit(self.page_6)
        self.login_username_txt.setGeometry(QtCore.QRect(100, 140, 391, 45))
        self.login_username_txt.setMinimumSize(QtCore.QSize(0, 45))
        self.login_username_txt.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(48, 47, 47);\n"
"    border-radius: 3px;\n"
"    margin: 0 0 0 18px;\n"
"    padding: 0 3px;\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(244, 202, 22);\n"
"    background-color: rgb(244, 202, 22);\n"
"}")
        self.login_username_txt.setClearButtonEnabled(True)
        self.login_username_txt.setObjectName("login_username_txt")
        self.login_password_txt = QtWidgets.QLineEdit(self.page_6)
        self.login_password_txt.setGeometry(QtCore.QRect(100, 210, 391, 45))
        self.login_password_txt.setMinimumSize(QtCore.QSize(0, 45))
        self.login_password_txt.setStyleSheet("QLineEdit {\n"
"    border: 1px solid rgb(48, 47, 47);\n"
"    border-radius: 3px;\n"
"    margin: 0 0 0 18px;\n"
"    padding: 0 3px;\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgb(244, 202, 22);\n"
"    background-color: rgb(244, 202, 22);\n"
"}")
        self.login_password_txt.setClearButtonEnabled(True)
        self.login_password_txt.setObjectName("login_password_txt")
        self.account_wgt.addWidget(self.page_6)
        self.load_wgt.addWidget(self.page_4)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.btn_next_link = QtWidgets.QPushButton(self.page_7)
        self.btn_next_link.setGeometry(QtCore.QRect(166, 510, 130, 45))
        self.btn_next_link.setMinimumSize(QtCore.QSize(130, 45))
        self.btn_next_link.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_next_link.setStyleSheet("QPushButton {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(244, 202, 22);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_next_link.setObjectName("btn_next_link")
        self.link_lbl = QtWidgets.QLabel(self.page_7)
        self.link_lbl.setGeometry(QtCore.QRect(-80, 70, 501, 421))
        self.link_lbl.setText("")
        self.link_lbl.setScaledContents(False)
        self.link_lbl.setObjectName("link_lbl")
        self.btn_back_link = QtWidgets.QPushButton(self.page_7)
        self.btn_back_link.setGeometry(QtCore.QRect(25, 510, 130, 45))
        self.btn_back_link.setMinimumSize(QtCore.QSize(130, 45))
        self.btn_back_link.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btn_back_link.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(247, 211, 70);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(252, 254, 252);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_back_link.setObjectName("btn_back_link")
        self.link_chk = QtWidgets.QCheckBox(self.page_7)
        self.link_chk.setGeometry(QtCore.QRect(490, 290, 501, 45))
        self.link_chk.setMinimumSize(QtCore.QSize(0, 45))
        self.link_chk.setStyleSheet("QCheckBox {\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    border: 1px solid rgb(247, 211, 70);\n"
"    border-radius: 2px;\n"
"    background-color: rgb(252, 254, 252);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1px solid rgb(247, 211, 70);\n"
"    border-radius: 2px;\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.link_chk.setChecked(True)
        self.link_chk.setObjectName("link_chk")
        self.load_wgt.addWidget(self.page_7)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.rocket_lbl = QtWidgets.QLabel(self.page_3)
        self.rocket_lbl.setGeometry(QtCore.QRect(-50, 130, 498, 373))
        self.rocket_lbl.setText("")
        self.rocket_lbl.setScaledContents(False)
        self.rocket_lbl.setObjectName("rocket_lbl")
        self.btn_complete_load = QtWidgets.QPushButton(self.page_3)
        self.btn_complete_load.setGeometry(QtCore.QRect(748, 360, 171, 45))
        self.btn_complete_load.setStyleSheet("QPushButton {\n"
"    border-radius: 3px;\n"
"    background-color: rgb(244, 202, 22);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_complete_load.setObjectName("btn_complete_load")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.page_3)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(530, 220, 441, 121))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.plainTextEdit_4.setFont(font)
        self.plainTextEdit_4.setStyleSheet("QPlainTextEdit {\n"
"    border: none;\n"
"    color: rgb(48, 47, 47);\n"
"}")
        self.plainTextEdit_4.setReadOnly(True)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.btn_back_end_load = QtWidgets.QPushButton(self.page_3)
        self.btn_back_end_load.setGeometry(QtCore.QRect(568, 360, 171, 45))
        self.btn_back_end_load.setStyleSheet("QPushButton {\n"
"    border: 1px solid rgb(247, 211, 70);\n"
"    border-radius: 3px;\n"
"    background-color: rgb(252, 254, 252);\n"
"    color: rgb(48, 47, 47);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(247, 211, 70);\n"
"}")
        self.btn_back_end_load.setObjectName("btn_back_end_load")
        self.load_wgt.addWidget(self.page_3)
        self.horizontalLayout.addWidget(self.load_wgt)

        self.retranslateUi(load_form)
        self.load_wgt.setCurrentIndex(0)
        self.account_wgt.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(load_form)

    def retranslateUi(self, load_form):
        _translate = QtCore.QCoreApplication.translate
        load_form.setWindowTitle(_translate("load_form", "MCrypt"))
        self.btn_start_load.setText(_translate("load_form", "Начать"))
        self.plainTextEdit_3.setPlainText(_translate("load_form", "Добро пожаловать в MCrypt! Давайте настроим это приложение для вас! Это займет не более 5 минут :)"))
        self.btn_skip_load.setText(_translate("load_form", "Пропустить настройку"))
        self.label_6.setText(_translate("load_form", "☀"))
        self.label_9.setText(_translate("load_form", "🌙"))
        self.label_8.setText(_translate("load_form", "☀"))
        self.label_11.setText(_translate("load_form", "🌙"))
        self.label_10.setText(_translate("load_form", "☀"))
        self.label_12.setText(_translate("load_form", "🌙"))
        self.label.setText(_translate("load_form", "Выберите цветовую схему приложения (наведите на область для получения информации)"))
        self.btn_next_style.setText(_translate("load_form", "Далее"))
        self.btn_back_style.setText(_translate("load_form", "Назад"))
        self.light_style_lbl.setText(_translate("load_form", "Светлая"))
        self.light_style_btn.setToolTip(_translate("load_form", "<FONT>Стандартное светлое цветовое оформление</FONT>"))
        self.dark_style_lbl.setText(_translate("load_form", "Темная"))
        self.dark_style_btn.setToolTip(_translate("load_form", "<FONT>Стандартное темное цветовое оформление</FONT>"))
        self.system_style_btn.setToolTip(_translate("load_form", "<FONT>Системное оформление позволяет отображать цвета элементов в зависимости от выбранных в персонализации Windows цветов</FONT>"))
        self.time_style_btn.setToolTip(_translate("load_form", "<FONT>Временное оформление позволяет автоматически сменять цветовое оформление (стандратное светлое и темное) в зависимости от текущего времени суток</FONT>"))
        self.system_style_lbl.setText(_translate("load_form", "Системная"))
        self.time_style_lbl.setText(_translate("load_form", "Временная"))
        self.btn_back_account.setText(_translate("load_form", "Назад"))
        self.btn_next_account.setText(_translate("load_form", "Далее"))
        self.label_3.setText(_translate("load_form", "Создайте новую учетную запись MCrypt!"))
        self.registration_username_txt.setPlaceholderText(_translate("load_form", "Имя пользователя"))
        self.registration_password_txt.setPlaceholderText(_translate("load_form", "Пароль"))
        self.registration_confirm_password_txt.setPlaceholderText(_translate("load_form", "Подтвердите пароль"))
        self.btn_registration.setText(_translate("load_form", "Создать"))
        self.btn_login_page.setText(_translate("load_form", "Уже есть учетная запись MCrypt? Войдите в нее!"))
        self.label_4.setText(_translate("load_form", "Войдите в учетную запись MCrypt!"))
        self.btn_login.setText(_translate("load_form", "Войти"))
        self.btn_registration_page.setText(_translate("load_form", "Еще нет учетной записи MCrypt? Создайте ее!"))
        self.login_username_txt.setPlaceholderText(_translate("load_form", "Имя пользователя"))
        self.login_password_txt.setPlaceholderText(_translate("load_form", "Пароль"))
        self.btn_next_link.setText(_translate("load_form", "Далее"))
        self.btn_back_link.setText(_translate("load_form", "Назад"))
        self.link_chk.setText(_translate("load_form", "Создать ярлык приложения на рабочем столе"))
        self.btn_complete_load.setText(_translate("load_form", "Завершить"))
        self.plainTextEdit_4.setPlainText(_translate("load_form", "Поздравляем, настройка приложения завершена! Теперь мы готовы к запуску данного приложения! Также вы можете дополнительно настроить приложение в настройках :)"))
        self.btn_back_end_load.setText(_translate("load_form", "Назад"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    load_form = QtWidgets.QWidget()
    ui = Ui_load_form()
    ui.setupUi(load_form)
    load_form.show()
    sys.exit(app.exec_())
