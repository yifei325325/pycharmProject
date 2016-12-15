#!/usr/bin/python
# coding:utf8

'this is iBaby Company product'
__author__ = "Kenny.Li"
__date__ = "2016/6/26"

import binascii
import logging
import socket
import struct
import sys
import thread
import time

from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtNetwork import *

import search
from iBabyAirUi import Ui_Form

logging.basicConfig(format='%(asctime)s--#--%(message)s',level=logging.INFO)


QtCore.QTextCodec.setCodecForTr(QtCore.QTextCodec.codecForName("utf8"))
class MyTest(QtGui.QWidget):
    def __init__(self):
        super(MyTest,self).__init__()
        # QtGui.QWidget.__init__(self) 上面的写法和本写法等同
        self.search_page = Ui_Form()
        self.search_page.setupUi(self)
        self.defaultUi()
        self.setWindowTitle(u"本 机 IP: %s ####  iBaby Air Tools V1.0"%self.getHostIp())

        self.setWindowIcon(QtGui.QIcon('../res/1.PNG'))

        # self.setWindowIcon(QIcon='2.PNG')
        self.myTimer = QtCore.QTimer()
        self.myTimer.timeout.connect(self.myTimeOut)
#         self.myTimer.start(2000)

#         self.refreshData()

        #几个按钮关联的信号与槽
        self.search_page.scanBtn.clicked.connect(self.scanBtnClickedTread)

        self.search_page.resultListWidget.itemDoubleClicked.connect(self.doubleClickedThread)
        self.search_page.openLEDBtn.clicked.connect(self.openLedClickedThread)
        self.search_page.listenBtn.clicked.connect(self.listenBtnClickedThread)
        self.search_page.speakBtn.clicked.connect(self.speakBtnClickedThread)
        self.search_page.setBtn.clicked.connect(self.setBtnClickedThread)
        #几个滑块关联的信号与槽
        self.search_page.brightneSlider.sliderMoved.connect(self.brightnessSliderMovedThread)
        self.search_page.redSlider.sliderMoved.connect(self.redSliderMovedThread)
        self.search_page.greenSlider.sliderMoved.connect(self.greenSliderMovedThread)
        self.search_page.blueSlider.sliderMoved.connect(self.blueSliderMovedThread)

    def defaultUi(self):
        states = u"用户态"
        self.search_page.wetLabel.clear()
        self.search_page.vocLabel.clear()
        self.search_page.TempLabel.clear()
        self.search_page.connStutesLabel.clear()
        self.search_page.setBtn.setText(u"设为%s"%states)
        self.search_page.deviceCountLabel.clear()
        #设置几个按钮的显示样式
        self.search_page.openLEDBtn.setStyleSheet("background-color:green;border-width:2px;border-style:inset")
        self.search_page.listenBtn.setStyleSheet("background-color:green;border-width:2px;border-style:inset")
        self.search_page.speakBtn.setStyleSheet("background-color:green;border-width:2px;border-style:inset")
        self.search_page.setBtn.setStyleSheet("background-color:green;border-width:2px;border-style:inset")
        #设置几个滑块的取值范围和默认值
        self.search_page.brightneSlider.setRange(0,100)
        self.search_page.brightneSlider.setValue(50)
        self.search_page.redSlider.setRange(0,255)
        self.search_page.redSlider.setValue(50)
        self.search_page.greenSlider.setRange(0,255)
        self.search_page.blueSlider.setRange(0,255)
                
    def scanBtnClickedTread(self):
        thread.start_new_thread(self.scanBtnClicked, ())
    def scanBtnClicked(self):
        self.search_page.resultListWidget.clear()
        self.setWindowTitle(u" ## 本 机 IP: %s ##  iBaby Air Tools V1.0"%self.getHostIp())
        s = search.searchCamera()
        ips_and_cams = s.getIp(s.broadcastString)
        print ips_and_cams
#         print ips_and_cams
        if ips_and_cams == 0:
            self.search_page.deviceCountLabel.setText(u"共搜索到 %d 台设备"%self.search_page.resultListWidget.count())
            return
        index = 1
        for item in ips_and_cams:
            ip = socket.inet_ntoa(struct.pack('I',socket.htonl(item[3])))
            p2p_uid = item[2]
          
            work_State = binascii.b2a_hex(item[-6])
            if work_State == "02":
                work_State = u"工装态"
            else:
                work_State = u"用户态"
                
            items = QtGui.QListWidgetItem()
            items.setText("ID:\t%d\n"%index+
                          "camID:\t%s\n"%item[1][:8]+
                          "ip:\t%s\n"%ip+
                          "camType:\t%s\n"%item[-3]+
                          "p2p_uid:\t%s\n"%p2p_uid+
                          "version:\t%d.%d.%d\n"%(int(binascii.b2a_hex(item[-4][:1]),base=16),
                                                int(binascii.b2a_hex(item[-4][1:2]),base=16),
                                                int(binascii.b2a_hex(item[-4][2:3]),base=16))+
                          "work_State:\t%s\n"%work_State+
                          "*"*34)
            self.search_page.resultListWidget.addItem(items)
            index += 1
        self.search_page.deviceCountLabel.setText(u"共搜索到 %d 台设备"%self.search_page.resultListWidget.count())
     
    def doubleClickedThread(self):
        thread.start_new_thread(self.doubleClicked, ()) 
    def doubleClicked(self):
        result = self.search_page.resultListWidget.selectedItems()[0].text().toUtf8()
        if result.contains("ip: "):
            ip = result.split("\n")[2]
            target = ip[3:].trimmed()
            self.search_page.vocLabel.setText("56")
            self.search_page.connStutesLabel.setText("Connect OK")
            self.search_page.TempLabel.setText(u"26.5℃")
            self.search_page.wetLabel.setText("10%")
        else:
            print "no camera searched ,retry!"
            return
        self.convertData(target)
        
    def openLedClickedThread(self):
        thread.start_new_thread(self.openLedClicked, ())    
    def openLedClicked(self):
        if self.search_page.openLEDBtn.isChecked():
            self.search_page.openLEDBtn.setText(u"关闭LED")
            self.search_page.openLEDBtn.setStyleSheet("background-color:red;border-width:2px;border-style:outset")
        else:
            self.search_page.openLEDBtn.setText(u"打开LED")
            self.search_page.openLEDBtn.setStyleSheet("background-color:green;border-width:2px;border-style:inset")

    def listenBtnClickedThread(self):
        thread.start_new_thread(self.listenBtnClicked, ())
    def listenBtnClicked(self):
        if self.search_page.listenBtn.isChecked():
            self.search_page.listenBtn.setText(u"关闭监听")
            self.search_page.listenBtn.setStyleSheet("background-color:red;border-width:2px;border-style:outset")
        else:
            self.search_page.listenBtn.setText(u"打开监听")
            self.search_page.listenBtn.setStyleSheet("background-color:green;border-width:2px;border-style:inset")

    def speakBtnClickedThread(self):
        thread.start_new_thread(self.speakBtnClicked, ())
    def speakBtnClicked(self):
        if self.search_page.speakBtn.isChecked():
            self.search_page.speakBtn.setText(u"关闭对讲")
            self.search_page.speakBtn.setStyleSheet("background-color:red;border-width:2px;border-style:outset")
        else:
            self.search_page.speakBtn.setText(u"打开对讲")
            self.search_page.speakBtn.setStyleSheet("background-color:green;border-width:2px;border-style:inset")
        
    def setBtnClickedThread(self):
        thread.start_new_thread(self.setBtnClicked, ())
    def setBtnClicked(self):
        if self.search_page.setBtn.isChecked():
            self.search_page.setBtn.setText(self.tr("设为工装态"))
            self.search_page.setBtn.setStyleSheet("background-color:red;border-width:2px;border-style:outset")
        else:
            self.search_page.setBtn.setText(u"设为用户态")
            self.search_page.setBtn.setStyleSheet("background-color:green;border-width:2px;border-style:inset")
    
    def brightnessSliderMovedThread(self):
        thread.start_new_thread(self.brightnessSliderMoved, ())         
    def brightnessSliderMoved(self):
        print "brightness slider moved"
        print self.search_page.brightneSlider.sliderPosition()
            
    def redSliderMovedThread(self):
        thread.start_new_thread(self.redSliderMoved, ())
    def redSliderMoved(self):
        print "redSlider slider moved"
        print self.search_page.redSlider.sliderPosition()
            
    def greenSliderMovedThread(self):
        thread.start_new_thread(self.greenSliderMoved, ())
    def greenSliderMoved(self):
        print "greenSlider slider moved"
        print self.search_page.greenSlider.sliderPosition()
            
    def blueSliderMovedThread(self):
        thread.start_new_thread(self.blueSliderMoved, ())
    def blueSliderMoved(self):
        print "blueSlider slider moved"
        print self.search_page.blueSlider.sliderPosition()
        
    def convertData(self,ip):
        """
        typedef struct searchBrodcastHeader
        {
            char            protocolHeader[4];   //协议头
            short           controlMask;         //操作码
            char            reserved;            //保留
            char            reserved2[8];        //保留
            int             contentLength;       //正文长度
            int             reserved3;           //保留
            
            
        }MJPEG_searchBrodcastHeader;
        
        '4shc8sii'
        """
        
        port = 80
#         data = struct.pack("4shc8sii","MO-O",0," "," ",0,0)
#         print "data = ",data
#         port = 80
        data1 = struct.pack("4shc8siih13s4s4s4s","MO-O",0," "," ",0,0,0," "," "," "," ")
    #     data2 = struct.pack("4shc8sii64si13s13s","MO-O",0," "," ",0,0," ",0," "," ")
    #     data2 = struct.pack("")
#         print "data = ",data1
#         print "len(data)= ",len(data1)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
    #     while True:
        s.sendall(data1)
        recv = s.recv(1024)
            
        
        print "length of header = ",len(recv)
        print "header = ",struct.unpack("!4shc8sii",recv)
         
        r = s.recv(1024)
        print "lenght of body= ",len(r)
        print "body =",struct.unpack("!h13s4s4s4s",r)
        
    #     s.sendall(data2)
    #     rr = s.recv(1024)
    #     print "yuanshishuju= ",rr
    #     print "len(rr)= ", len(rr)
    #     print "rr = ",struct.unpack("!64si13s13s",rr)
    #     
    
        s.close()
        
    def myTimeOut(self):
        t = thread.start_new_thread(self.testddd,())
        
        
        
    def testddd(self):
        print "refresh Data!"
        time.sleep(4)
        
    def getHostIp(self):
        localHostName = QHostInfo.localHostName()#获取本主机名
        info = QHostInfo.fromName(localHostName)#通过主机名获取所有ip地址的QHostInfo对象（包含ipV4 和 IP V6）
        for addr in info.addresses():#info.addresses()返回的是所有ip地址的列表
            if addr.protocol()==QAbstractSocket.IPv4Protocol:
                hostIp =  addr.toString()
                return hostIp
                
        
if __name__ == "__main__":
        
    app = QtGui.QApplication(sys.argv)
    m = MyTest()
    m.show()
    sys.exit(app.exec_())
