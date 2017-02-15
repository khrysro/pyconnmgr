# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.image4 = QtWidgets.QLabel(Dialog)
        self.image4.setAlignment(QtCore.Qt.AlignCenter)
        self.image4.setObjectName("image4")
        self.verticalLayout.addWidget(self.image4)
        self.label_version = QtWidgets.QLabel(Dialog)
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.setObjectName("label_version")
        self.verticalLayout.addWidget(self.label_version)
        self.label_createdby = QtWidgets.QLabel(Dialog)
        self.label_createdby.setAlignment(QtCore.Qt.AlignCenter)
        self.label_createdby.setObjectName("label_createdby")
        self.verticalLayout.addWidget(self.label_createdby)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.image4.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><img src=\":/images/glade/pyconnmgr64x64.png\"/></p></body></html>"))
        self.label_version.setText(_translate("Dialog", "APPNAME APPVERSION"))
        self.label_createdby.setText(_translate("Dialog", "<span size=\"smaller\">Created by: KhrysRo</span>"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00007f;\">http://www.github.com/khrysRo</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Close"))

import RF_rc
