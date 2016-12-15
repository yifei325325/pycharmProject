#!/usr/bin/python
#coding:utf8
'''
Created on 2016年7月5日

@author: Kenny
'''
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
from PyQt4.QtNetwork import *

import ctypes
  
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  

NETWORK_LEN = 20

class BroadCastHeader(object):
    '''
    #固件定义的广播结构体
typedef struct{
        char bc_name[NETWORK_LEN];	/* broadcast packet name */
        int  command;
        char camid[NETWORK_LEN];
        char ip[NETWORK_LEN];
        int  port;
        char mac[NETWORK_LEN];
        char version[NETWORK_LEN];
        int  state; /* 1:registered, 0:unregistered */
        char reserve[16]; /* reserve for future */
        int  checksum;
}BROADCAST_PACKET;


#define BUFLENGTH	sizeof(LOCAL_MSG)
#define NETWORK_LEN		20
#define BC_PORT			3759

typedef struct _BroadcastPacket{
	char bc_name[NETWORK_LEN];	/* broadcast packet name */
	int  command;
	char camid[NETWORK_LEN];
	char ip[NETWORK_LEN];
	int  port;
	char mac[NETWORK_LEN];
	char version[NETWORK_LEN];
	int  state; /* 1:registered 0:un-registered. */
	int  p2pType;	/* 0:TUTK 1:SY */
	char camType; /* H1 H1N M6 M6S AIR max 1 bytes */
	char reserve[11]; /* reserve for future */
	int  checksum;
}BROADCAST_PACKET;


    '''
    def __init__(self):
        self.packet = QByteArray(132,chr(0))

        self.bc_name = QByteArray(NETWORK_LEN-5,chr(0))
        self.bc_name.insert(0,"iBaby")
        self.command = QByteArray(3,chr(0))
        self.command.insert(3,chr(1))
        self.camid = QByteArray(NETWORK_LEN,chr(0))
        self.ip = QByteArray(NETWORK_LEN,chr(0))
        self.port = QByteArray(4,chr(0))
        self.mac = QByteArray(NETWORK_LEN,chr(0))
        self.version = QByteArray(NETWORK_LEN,chr(0))
        self.state = QByteArray(4,chr(0))
        self.reserve = QByteArray(16,chr(0))
        self.checksum = QByteArray(4,chr(0))
        self.checksum.resize(4)

        self.packet = QByteArray()
        self.packet.append(self.bc_name)
        self.packet.append(self.command)
        self.packet.append(self.camid)
        self.packet.append(self.ip)
        self.packet.append(self.port)
        self.packet.append(self.mac)
        self.packet.append(self.version)
        self.packet.append(self.state)
        self.packet.append(self.reserve)
        self.packet.append(self.checksum)


myBroadCast = BroadCastHeader()


class MyServer(QDialog):
    def __init__(self):
        super(MyServer,self).__init__()
        self.setWindowTitle("server")
        vboxMain = QVBoxLayout(self)

        timerLabel = QLabel(self.tr("Timer"))
        vboxMain.addWidget(timerLabel)

        self.lineEdit = QListWidget()
        vboxMain.addWidget(self.lineEdit)

        self.button = QPushButton(self.tr('Send'))
        vboxMain.addWidget(self.button)

        self.connect(self.button,SIGNAL('clicked()'),self.slotButton)

        self.port = 3759
        self.isStarted = False
        self.myUdpSocket = QUdpSocket(self)
        self.myUdpSocket.bind(QHostAddress.Any ,self.port)

        self.timer = QTimer(self)
        self.timer.connect(self.timer,SIGNAL("timeout()"),self.slotTimeout)
        self.connect(self.myUdpSocket,SIGNAL("readyRead()"),self.recData)

    def slotTimeout(self):
        msg = myBroadCast.packet
        length = 0
        if msg == "":
            return
        length = self.myUdpSocket.writeDatagram(msg, QHostAddress.Broadcast, self.port)
        if length != msg.length():
            return

    def slotButton(self):
        if self.isStarted == False:
            self.isStarted = True
            self.button.setText("Stop")
            self.timer.start(1000)

        else:
            self.isStarted = False
            self.button.setText("Send")
            self.timer.stop()

    def recData(self):
        data = self.myUdpSocket.readDatagram(132)
        print data
        print type(data)
        print len(data[0])
        print data[1].toString()



app = QApplication(sys.argv)
dialog = MyServer()
dialog.show()
app.exec_()