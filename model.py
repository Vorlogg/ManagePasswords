# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 373)
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(240, 240, 240);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setStyleSheet("gridline-color: rgb(160, 160, 160);\n"
"selection-background-color: rgb(230, 230, 230);\n"
"selection-color: rgb(0, 0, 0);")
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_1.sizePolicy().hasHeightForWidth())
        self.pushButton_1.setSizePolicy(sizePolicy)
        self.pushButton_1.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-style: outset;\n"
"    border-top-left-radius: 10;\n"
"    border-bottom-left-radius: 10;\n"
"    border-width: 1px;\n"
"    border-color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(220,220,220);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(200,200,200);\n"
" }")
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-style: outset;\n"
"    border-top-width: 1px;\n"
"    border-bottom-width: 1px;\n"
"    border-right-width: 1px;\n"
"    border-color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(220,220,220);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(200,200,200);\n"
" }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-style: outset;\n"
"    border-top-right-radius: 10;\n"
"    border-bottom-right-radius: 10;\n"
"    border-width: 1px;\n"
"    border-left-width: 0px;\n"
"    border-color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(220,220,220);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(200,200,200);\n"
" }")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    background-color:  qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(230, 230, 230, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    border-style: outset;\n"
"    border-top-right-radius: 10;\n"
"    border-bottom-right-radius: 10;\n"
"    border-width: 1px;\n"
"    border-left-width: 0px;\n"
"    border-color: rgb(110, 110, 110);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color:rgb(220,220,220);\n"
" }\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgb(200,200,200);\n"
" }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Учет материалов"))
        self.tableWidget.setSortingEnabled(False)
        self.pushButton_1.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_3.setText(_translate("MainWindow", "Найти"))
        self.pushButton_4.setText(_translate("MainWindow", "Назад"))
