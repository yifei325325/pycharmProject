# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(538, 659)
        self.listWidget = QtGui.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(30, 40, 261, 251))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.listWidget_2 = QtGui.QListWidget(Form)
        self.listWidget_2.setGeometry(QtCore.QRect(30, 310, 471, 211))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(350, 170, 81, 61))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 540, 81, 61))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.checkBox = QtGui.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(350, 110, 71, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Air升级工具V1.0", None))
        self.pushButton.setText(_translate("Form", "搜索", None))
        self.pushButton_2.setText(_translate("Form", "升级", None))
        self.checkBox.setText(_translate("Form", "全选", None))

