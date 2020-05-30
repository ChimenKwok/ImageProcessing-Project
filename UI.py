# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 471)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(145, 400, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(255, 400, 113, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(550, 290, 151, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(15)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(0)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 240, 171, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 210, 51, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 180, 171, 32))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 210, 61, 32))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(650, 210, 61, 32))
        self.pushButton_7.setObjectName("pushButton_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 521, 381))
        self.label.setObjectName("label")
        self.label.setScaledContents(True)
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(540, 135, 171, 32))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(600, 280, 60, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 719, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(MainWindow.image)
        self.pushButton_2.clicked.connect(MainWindow.video_open)
        self.pushButton_3.clicked.connect(MainWindow.RGBToWhite)
        self.pushButton_4.clicked.connect(MainWindow.rotate)
        self.pushButton_5.clicked.connect(MainWindow.histogram_equalization)
        self.pushButton_6.clicked.connect(MainWindow.upsidedown)
        self.pushButton_7.clicked.connect(MainWindow.flipLeftToRight)
        self.pushButton_11.clicked.connect(MainWindow.save)
        self.horizontalSlider.valueChanged.connect(MainWindow.adjustS)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PhVio Editor"))
        self.pushButton.setText(_translate("MainWindow", "Image"))
        self.pushButton_2.setText(_translate("MainWindow", "Video"))
        self.pushButton_3.setText(_translate("MainWindow", "Black and White"))
        self.pushButton_4.setText(_translate("MainWindow", "⟲"))
        self.pushButton_5.setText(_translate("MainWindow", "Histogram Equalization"))
        self.pushButton_6.setText(_translate("MainWindow", "⇵"))
        self.pushButton_7.setText(_translate("MainWindow", "⇄"))
        self.label.setText(_translate("MainWindow", "                                                      Welcome to Phvio."
                                                    "\n        This is a light version of Photoshop to help enhance your images and videos."))
        self.pushButton_11.setText(_translate("MainWindow", "Record/Save"))
        self.label_2.setText(_translate("MainWindow", "Saturation"))
