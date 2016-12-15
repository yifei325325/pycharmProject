#!/usr/bin/python
#coding:utf8
'''
Created on 2016年7月1日

@author: Kenny
'''
from PyQt4 import QtGui,QtCore
import sys,random

class myTimer(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        
        self.resize(500,500)
        self.t = QtCore.QTimer()
        
        self.t.timeout.connect(self.changeColor)
        self.t.start(400)
        
    def changeColor(self):
        colors = {1:"red",2:"green",3:"blue",4:"pink",5:"black"}
        r = random.randint(1,5)
        self.setStyleSheet("background-color:%s"%colors[r])
        
app = QtGui.QApplication(sys.argv)
mt = myTimer()
mt.show()
sys.exit(app.exec_())
        