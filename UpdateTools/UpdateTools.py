#!/usr/bin/python
# coding:utf8

'this is iBaby Company product'
__author__ = "Kenny.Li"
__date__ = "2016/12/15"


import sys
import thread
import time
import telnetlib
import socket

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui import Ui_Form
from test4 import *


QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))

host_ip = socket.gethostbyname(socket.gethostname())

class myWidget(QWidget):
    def __init__(self):
        super(myWidget,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.initUi()

        self.connect(self.ui.pushButton,SIGNAL("clicked()"),self.search)
        self.ui.listWidget.itemDoubleClicked.connect(self.update)

    def initUi(self):
        self.ui.pushButton_2.setEnabled(False)

    def search(self):
        self.ui.listWidget.clear()
        sc = searchCamera()
        lis = sc.getIp(sc.broadcastString)
        # print lis
        flag = 0
        for j in xrange(len(lis)):
            camid = lis[j][2]
            ip = lis[j][3]
            # port = lis[j][4]
            # mac = lis[j][5]
            version = lis[j][6]
            state = lis[j][7]
            # p2pType = lis[j][8]
            camType = lis[j][9]
            # reserve = lis[j][10]
            # checksum = lis[j][11]
            # print "bc_name = ",bc_name
            # print "command = ",command
            # print "camid = ",camid
            # print "ip = ",ip
            # # print "port = ",port
            # # print "mac = ",mac
            # print "version = ",version
            # print "state = ",R[state]
            # # print "p2pType = ",p2pType
            # print "camType = ",D[int(binascii.b2a_hex(camType),base=16)]
            # # print "reserve = ",reserve
            # # print "checksum = ",checksum

            result = QString()
            result.append("Camid:\t%s\n" % QString(camid)
                          + "IP:\t%s\n" % QString(ip)
                          + "Version:\t%s\n" % QString(version)
                          + "State:\t%s\n" % QString(R[state])
                          +"CamType:\t%s\n"%QString(D[int(binascii.b2a_hex(camType),base=16)]))

            for i in xrange(self.ui.listWidget.count()):
                if self.ui.listWidget.item(i).text().contains(QString(ip)):
                    flag = 1
                    break
            if not flag:
                self.ui.listWidget.addItem(result)
        # self.ui.listWidget.connect(self.ui.listWidget,SIGNAL('doubleClicked()'),self.update)
    def update(self):
        currentItem =  self.ui.listWidget.currentItem().text()
        ip = currentItem.section("\n",1,1)
        ip = ip.section(':',1,1,QString.SectionSkipEmpty).remove('\t')


        username = 'root'
        password = 'iBabyVP8019'
        finish = '#'
        #         filename = self.GetFileName(camType)
        # print "my file name = ", fileName
        # print type(fileName)
        #
        try:
            tn = telnetlib.Telnet(str(ip), port=23, timeout=10)
        except BaseException,e:
            print e
            return 0
        #
        # if camType == 0:
        #     tn.read_until('iBaby login: ')
        # elif camType == 1 or camType == 2 or camType == 3:
        tn.read_until('GM login: ')

        tn.write(username + '\n')
        tn.read_until('Password: ')
        tn.write(password + '\n')
        tn.read_until(finish)
        tn.write('tftp -g -l /tmp/test.file -r test.file %s'%host_ip)

        # tn.read_until("$")
        # tn.close()





app = QApplication(sys.argv)
mw = myWidget()
mw.show()
sys.exit(app.exec_())