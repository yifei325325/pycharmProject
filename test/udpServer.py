# -*- coding: utf-8 -*-
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from PyQt4.QtNetwork import *

QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))


class Udpserver(QDialog):
    def __init__(self, parent=None):
        super(Udpserver, self).__init__(parent)
        self.setWindowTitle(self.tr("UDP Server"))
        vbMain = QVBoxLayout(self)

        LableTimer = QLabel(self.tr("Timer:"))
        vbMain.addWidget(LableTimer)

        self.LineEditText = QLineEdit()
        vbMain.addWidget(self.LineEditText)

        self.PushButtonStart = QPushButton(self.tr("Start"))
        vbMain.addWidget(self.PushButtonStart)

        self.connect(self.PushButtonStart, SIGNAL("clicked()"), self.slotButton)

        self.port = 5555
        self.isStarted = False
        self.udpSocket = QUdpSocket(self)

        self.timer = QTimer(self)
        self.timer.connect(self.timer,SIGNAL("timeout()"),self.slotTimeout)
        # self.timer.timeout.connect(self.slotTimeout)

    def slotTimeout(self):
        print "push"
        msg = self.LineEditText.text()
        print "msg = %s"%msg
        length = 0
        if msg == "":
            return
        length = self.udpSocket.writeDatagram(msg.toLatin1(), QHostAddress.Broadcast, self.port)
        print "length = %d"%length
        if length != msg.length():
            return

    def slotButton(self):
        print "in"
        if self.isStarted == False:
            print "False"
            self.isStarted = True
            self.PushButtonStart.setText("Stop")
            self.timer.start(1000)
        else:
            self.isStarted = False
            self.PushButtonStart.setText("Start")
            self.timer.stop()


app = QApplication(sys.argv)
dialog = Udpserver()
dialog.show()
app.exec_()