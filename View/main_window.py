# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../View/DesignUI/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1200, 800)
        main_window.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(30, 30, 30);\n"
"}")
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setStyleSheet("QWidget {\n"
"    background-color: rgb(30, 30, 30);\n"
"}")
        self.central_widget.setObjectName("central_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.central_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.main_frame = QtWidgets.QFrame(self.central_widget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.enc_widget = QtWidgets.QStackedWidget(self.main_frame)
        self.enc_widget.setObjectName("enc_widget")
        self.page_smp = QtWidgets.QWidget()
        self.page_smp.setObjectName("page_smp")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_smp)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.types_tab = QtWidgets.QTabWidget(self.page_smp)
        self.types_tab.setStyleSheet("QTabWidget::pane {\n"
"    background: rgb(46, 44, 44);\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    height: 25px;\n"
"    border: 1px solid rgb(77, 77, 77);\n"
"    padding: 10 120px;\n"
"    background-color: rgb(48, 47, 47);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border: 1px solid rgb(30, 30, 30);\n"
"    background-color: rgb(30, 30, 30);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: rgb(67, 67, 67);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.types_tab.setElideMode(QtCore.Qt.ElideNone)
        self.types_tab.setDocumentMode(False)
        self.types_tab.setMovable(True)
        self.types_tab.setObjectName("types_tab")
        self.enc_tab_smp = QtWidgets.QWidget()
        self.enc_tab_smp.setObjectName("enc_tab_smp")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.enc_tab_smp)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.enc_smp = QtWidgets.QFrame(self.enc_tab_smp)
        self.enc_smp.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(77, 77, 77);\n"
"}")
        self.enc_smp.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.enc_smp.setFrameShadow(QtWidgets.QFrame.Plain)
        self.enc_smp.setObjectName("enc_smp")
        self.horizontalLayout_4.addWidget(self.enc_smp)
        self.types_tab.addTab(self.enc_tab_smp, "")
        self.dec_tab = QtWidgets.QWidget()
        self.dec_tab.setObjectName("dec_tab")
        self.types_tab.addTab(self.dec_tab, "")
        self.horizontalLayout_2.addWidget(self.types_tab)
        self.enc_widget.addWidget(self.page_smp)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.enc_widget.addWidget(self.page_4)
        self.verticalLayout.addWidget(self.enc_widget)
        self.status_frame = QtWidgets.QFrame(self.main_frame)
        self.status_frame.setMinimumSize(QtCore.QSize(0, 15))
        self.status_frame.setStyleSheet("QFrame {\n"
"    border: 1px solid rgb(77, 77, 77);\n"
"    background-color: rgb(48, 47, 47);\n"
"}")
        self.status_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.status_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.status_frame.setObjectName("status_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.status_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.enc_combo_box = QtWidgets.QComboBox(self.status_frame)
        self.enc_combo_box.setStyleSheet("QComboBox {\n"
"    border: none;\n"
"    background-color: rgb(48, 47, 47);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    outline: none;\n"
"    color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(60, 60, 60);\n"
"}")
        self.enc_combo_box.setObjectName("enc_combo_box")
        self.enc_combo_box.addItem("")
        self.enc_combo_box.addItem("")
        self.horizontalLayout_3.addWidget(self.enc_combo_box)
        self.verticalLayout.addWidget(self.status_frame)
        self.horizontalLayout.addWidget(self.main_frame)
        main_window.setCentralWidget(self.central_widget)
        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 1200, 18))
        self.menu_bar.setObjectName("menu_bar")
        self.file_menu = QtWidgets.QMenu(self.menu_bar)
        self.file_menu.setObjectName("file_menu")
        self.enc_menu = QtWidgets.QMenu(self.menu_bar)
        self.enc_menu.setObjectName("enc_menu")
        main_window.setMenuBar(self.menu_bar)
        self.action_program_info = QtWidgets.QAction(main_window)
        self.action_program_info.setObjectName("action_program_info")
        self.action_help = QtWidgets.QAction(main_window)
        self.action_help.setObjectName("action_help")
        self.file_menu.addAction(self.action_program_info)
        self.file_menu.addAction(self.action_help)
        self.menu_bar.addAction(self.file_menu.menuAction())
        self.menu_bar.addAction(self.enc_menu.menuAction())

        self.retranslateUi(main_window)
        self.types_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "MCrypt"))
        self.types_tab.setTabText(self.types_tab.indexOf(self.enc_tab_smp), _translate("main_window", "Шифрование"))
        self.types_tab.setTabText(self.types_tab.indexOf(self.dec_tab), _translate("main_window", "Дешифрование"))
        self.enc_combo_box.setItemText(0, _translate("main_window", "Простая перестановка"))
        self.enc_combo_box.setItemText(1, _translate("main_window", "Перестановка по ключу"))
        self.file_menu.setTitle(_translate("main_window", "Файл"))
        self.enc_menu.setTitle(_translate("main_window", "Шифрование"))
        self.action_program_info.setText(_translate("main_window", "О программе"))
        self.action_help.setText(_translate("main_window", "Справка"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
