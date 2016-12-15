# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from PyQt4.QtNetwork import *

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class UdpClient(QDialog):
    def __init__(self, parent=None):
        super(UdpClient, self).__init__(parent)
        self.setWindowTitle(self.tr("UDP Client"))
        vbMain = QVBoxLayout(self)

        self.LineEditReceive = QTextEdit()
        vbMain.addWidget(self.LineEditReceive)
        self.PushButtonClose = QPushButton(self.tr("Close"))
        vbMain.addWidget(self.PushButtonClose)
        self.connect(self.PushButtonClose, SIGNAL("clicked()"), self.slotButton)
        self.port = 5555
        self.udpSocket = QUdpSocket(self)
        self.connect(self.udpSocket, SIGNAL("readyRead()"), self.dataReceive)
        self.connect(self.PushButtonClose,SIGNAL("clicked()"),self.slotButton)

        result = self.udpSocket.bind(self.port)
        if not result:
            QMessageBox.information(self, self.tr("error"), self.tr("udpserver create error!"))
            return

    def dataReceive(self):
        while self.udpSocket.hasPendingDatagrams():
            msglist = self.udpSocket.readDatagram(self.port)
            msg = msglist[0]
            self.LineEditReceive.insertPlainText(msg)

    def slotButton(self):
        self.close()


app = QApplication(sys.argv)
dialog = UdpClient()
dialog.show()
app.exec_()