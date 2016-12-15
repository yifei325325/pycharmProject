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
  
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  


class BroadCastHeader(object):
    def __init__(self):
        self.bc_name = ''
        self.command = 0
        self.camid = ''
        self.ip = ''
        self.port = 0
        self.mac = ''
        self.version = ''
        self.state = 0
        self.reserve = ''
        self.checksum = 0



class TcpClientSocket(QTcpSocket):  
    def __init__(self,parent=None):  
        super(TcpClientSocket,self).__init__(parent)  
        self.connect(self,SIGNAL("readyRead()"),self.dataReceive)  
        self.connect(self,SIGNAL("disconnected()"),self.slotDisconnected)  
        self.length = 0  
        self.msglist = QByteArray()  
      
    def dataReceive(self):  
        while self.bytesAvailable() > 0:  
            length = self.bytesAvailable()  
            msg = self.read(length)  
            self.emit(SIGNAL("updateClients(QString,int)"),msg,length)  
                      
    def slotDisconnected(self):  
        pass  
          
class Server(QTcpServer):  
    def __init__(self,parent=None,port=0):  
        super(Server,self).__init__(parent)  
        self.listen(QHostAddress.Any,port)  
        self.tcpClientSocketList = []  
      
    def incomingConnection(self,socketDescriptor):  
        tcpClientSocket = TcpClientSocket(self)  
        self.connect(tcpClientSocket,SIGNAL("updateClients(QString,int)"),self.updateClients)  
        self.connect(tcpClientSocket,SIGNAL("disconnetcted(int)"),self.slotDisconnected)  
        tcpClientSocket.setSocketDescriptor(socketDescriptor)  
        self.tcpClientSocketList.append(tcpClientSocket)  
      
    def updateClients(self,msg,length):  
        self.emit(SIGNAL("updateServer(QString,int)"),msg,length)  
        for i in xrange(len(self.tcpClientSocketList)):  
            item = self.tcpClientSocketList[i]  
            length_msg = item.writeData(msg.toUtf8())  
            if length_msg != msg.toUtf8().length():  
                continue  
      
    def slotDisconnected(self,descriptor):  
        for i in xrange(len(self.tcpClientSocketList)):  
            item = self.tcpClientSocketList[i]  
            if item.socketDescriptor() == descriptor:  
                self.tcpClientSocketList.remove[i]  
                return  
        return  
  
class TcpServer(QDialog):  
    def __init__(self,parent=None,f=None):  
        super(TcpServer,self).__init__(parent)  
        self.setWindowTitle("TCP Server")  
        vbMain = QVBoxLayout(self)  
        self.ListWidgetContent = QListWidget(self)  
        vbMain.addWidget(self.ListWidgetContent)  
          
        hb = QHBoxLayout()  
        LabelPort = QLabel(self)  
        LabelPort.setText(self.tr("Port:"))  
        hb.addWidget(LabelPort)  
          
        LineEditPort = QLineEdit(self)  
        hb.addWidget(LineEditPort)  
          
        vbMain.addLayout(hb)  
          
        self.PushButtonCreate = QPushButton(self)  
        self.PushButtonCreate.setText(self.tr("Create"))  
        vbMain.addWidget(self.PushButtonCreate)  
          
        self.connect(self.PushButtonCreate,SIGNAL("clicked()"),self.slotCreateServer)  
        self.port  = 8010  
        LineEditPort.setText(QString.number(self.port))  
      
    def slotCreateServer(self):  
        server = Server(self,self.port)  
        self.connect(server,SIGNAL("updateServer(QString,int)"),self.updateServer)  
        self.PushButtonCreate.setEnabled(False)  
      
    def updateServer(self,msg,length):  
        self.ListWidgetContent.addItem(msg.fromUtf8(msg))  
      
  
                  
  
  
          
          
app=QApplication(sys.argv)  
dialog=TcpServer()  
dialog.show()  
app.exec_()  