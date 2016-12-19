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
import binascii

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
        self.state = 0

        self.connect(self.ui.pushButton,SIGNAL("clicked()"),self.search)
        self.ui.listWidget.itemDoubleClicked.connect(self.update)

        self.connect(self.ui.checkBox,SIGNAL("clicked()"),self.select_all)


    def initUi(self):
        self.ui.pushButton_2.setEnabled(False)

    def search(self):
        self.ui.listWidget.clear()
        sc = searchCamera()

        lis = sc.getIp(sc.broadcastString)
        if lis == 0:
            self.ui.listWidget_2.addItem(self.tr("没有搜索到摄像头，请重试！\n"))
            return 0
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
    def update(self):
        currentItem =  self.ui.listWidget.currentItem().text()
        ip = currentItem.section("\n",1,1)
        ip = ip.section(':',1,1,QString.SectionSkipEmpty).remove('\t')

        username = "root"
        password = "iBabyVP8019"
        finish = "#"

        print "start"
        try:
            tn = telnetlib.Telnet(str(ip), port=23, )
        except BaseException, error:
            print 'error: \t%s' % error
            return 0
        tn.read_until('GM login: ')
        tn.write(username + '\n')
        tn.read_until('Password: ')
        tn.write(password + '\n')
        tn.read_until(finish)
        tn.write('cd /mnt/mtd/update/file;tftp -gr ipcam_flash -l ipcam %s;chmod 777 ipcam;reboot\n' % host_ip)
        tn.close()

    def select_all(self):
        print 'select all'
        self.ui.pushButton_2.setEnabled(True)
        print self.ui.listWidget.count()
        # self.ui.listWidget.setItemSelected(self.ui.listWidget.item(0),True)

        # print self.ui.listWidget.selectedItems()

app = QApplication(sys.argv)
mw = myWidget()
mw.show()
sys.exit(app.exec_())