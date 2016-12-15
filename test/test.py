#!/usr/bin/python
#coding:utf8
'''
Created on 2016年7月1日

@author: Kenny
'''
from PyQt4.QtNetwork import *
from PyQt4 import QtGui,QtCore
import struct
import sys

data1 = struct.pack("4shc8siih13s4s4s4s","MO-O",0," "," ",0,0,0," "," "," "," ")#LoginRequestReply#登录响应结构体
data2 = struct.pack("4shc8siic","MO-O",32," "," ",1,0,"0")#请求温湿度
mySocket = QTcpSocket()
class MyTestWidget(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.myBtn = QtGui.QPushButton(self)
        self.myBtn2 = QtGui.QPushButton(self)
        
        self.setGeometry(100,100,300,100)
        self.myBtn.setText("Send")
        self.myBtn2.setText("Send2")
        self.myBtn.setGeometry(20,20,80,50)
        self.myBtn2.setGeometry(120,20,80,50)
        
        self.myBtn.clicked.connect(self.myBtnClicked)
        self.myBtn2.clicked.connect(self.sendData2)
        
        mySocket.connected.connect(self.sendData)
        mySocket.readyRead.connect(self.readData)
        mySocket.disconnected.connect(self.serverDisconnected)
        
        
        
        
    def slotConnected(self):
        pass
    
    def myBtnClicked(self):
        print "clicked"
        mySocket.connectToHost("10.0.1.18",80)
    
    def sendData(self):
        print "connected"
        mySocket.writeData(data1)
        
    def sendData2(self):
        if mySocket.isWritable():
            length = mySocket.writeData(data1)
            print "length = ",length
            print "len(data2)= ",len(data1)
            if length != len(data1):
                return
            
            print "send Data2"
        else:
            print " not ready"
        
        
    def readData(self):
        print "read!"
        while mySocket.bytesAvailable()>0:
            len = mySocket.bytesAvailable()
            print "len = ",len
            r = mySocket.read(len)
            print "r = ", r
        print "end"
        
    def serverDisconnected(self):
        print "disconnected"
        
    
app = QtGui.QApplication(sys.argv)
t = MyTestWidget()
t.show()
sys.exit(app.exec_())






# connect(mysocket,QtCore.SIGNAL("connected()"),QtCoreslotConnected)  
# mysocket.connectToHost("10.0.1.18", 80)
# print mysocket.peerPort()
# print mysocket.peerName()
# print mysocket.isReadable()
# mysocket.writeData(data1)
# print mysocket.isReadable()
# 
# print "recv = ",mysocket.read(1024)