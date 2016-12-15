#!/usr/bin/python
# coding:utf8

'this is iBaby Company product'
__author__ = "Kenny.Li"
__date__ = "2016/6/26"



import logging

import sys

import time
import struct
import os
import tftpy
# import  binascii


from PyQt4 import QtCore
from PyQt4 import QtGui


# import com.search
from com.iBabyAirUi import Ui_Form

logging.basicConfig(format='%(asctime)s--#--%(message)s',filename="run.log",level=logging.DEBUG)


QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))
class MyWidget(QtGui.QWidget):
    def __init__(self):
        super(MyWidget,self).__init__()
        self.win = Ui_Form()
        self.win.setupUi(self)
        # self.setWindowTitle('test')
        # self.resize(250,150)
        logging.info("info")
        logging.debug("debug")
        logging.warning("warning")
        logging.critical("critical")
        # self.win.pushButton.clicked.connect(self.fo1)
        # self.connect(self.win.pushButton,QtCore.SIGNAL("clicked()"),self,QtCore.SLOT("close()"))
    def fo1(self):
        print "hh"
        logging.debug("call me")
        QtCore.qDebug("i am test")

app = QtGui.QApplication(sys.argv)
w = MyWidget()
w.show()
sys.exit(app.exec_())


