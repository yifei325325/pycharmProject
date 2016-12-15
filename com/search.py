#!/usr/bin/python
# coding:utf8

'''
typedef struct searchBrodcastHeader
{
    char            protocolHeader[4];   //协议头
    short           controlMask;         //操作码
    char            reserved;            //保留
    char            reserved2[8];        //保留
    int             contentLength;       //正文长度
    int             reserved3;           //保留
    
}MJPEG_searchBrodcastHeader;  len = 24

typedef struct searchCommandContent
{
    char            reserved0;
    char            reserved1;
    char            reserved2;
    char            reserved3;
    
}MJPEG_searchCommandContent; len = 4

typedef struct searchCommandContentReply
{
    MJPEG_searchBrodcastHeader  header; //头部
    char            camID[13];          //摄像头ID
    char            camName[21];        //摄像头名称,p2p
    unsigned int    IP;                 //IP; 大端
    unsigned int    netMask;            //掩码  大端
    unsigned int    getwayIP;           //网关IP;  大端
    unsigned int    DNS;                //DNS;  大端
    char p2pType;
    char workState;          //工装状态
    char            reserved[2];        //保留
    char            sysVersion[4];      //系统版本
    char            camtype[4];       //App software 版本 修改为 设备类型
    unsigned short           port;       //端口 大端
    char            dhcpEnabled;        //DHCP状态
    
}MJPEG_searchCommandContentReply; len = 92
'''


import time
import telnetlib
import struct
import socket
import os

host_ip = socket.gethostbyname(socket.gethostname())#获取主机IP地址

class searchCamera(object):
#     定义要广播的字符串（需要固件提供）
    '''
        typedef struct searchBrodcastHeader
        {
            char            protocolHeader[4];   //协议头
            short           controlMask;         //操作码
            char            reserved;            //保留
            char            reserved2[8];        //保留
            int             contentLength;       //正文长度
            int             reserved3;           //保留
            
            
        }MJPEG_searchBrodcastHeader;
    '''
    def __init__(self):
        self.protocolHeader = ' '
        self.controlMask = 0
        self.reserved = ' '
        self.reserved2 = ' '
        self.contentLength = 0 
        self.reserved3 = 0
        self.reserved0 = ' '
    #     将要广播的字符串（broadcastString），转化成网络传输的字节码
        self.broadcastString = struct.pack('4shc8sii4s',self.protocolHeader,self.controlMask,
                                           self.reserved,self.reserved2,self.contentLength,
                                           self.reserved3,self.reserved0)
#     广播字节码并接收回应
    def getIp(self,values): 
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
# 重复发送5次广播包，每次间隔0.1秒，接收时不停的循环接收，提高搜索成功率
        for i in xrange(7): #@UnusedVariable
            s.sendto(values,('<broadcast>',10000))#10000是端口号，要和固件方对应
            time.sleep(0.1)
        s.setblocking(0)#设置为非阻塞模式
        #定义一个空列表，用来接收camID和IP
        l = []
        while True:
            try:
                sock,addr = s.recvfrom(1024)
                reply = struct.unpack('!23s13s21sIIII2c2s4s4sHc',sock)
                # reply = struct.unpack('@4shc8sii4s',sock)
                l.append(reply)
#                 print reply  
#               #列表去重，因为有多次搜索，可能会有很多重复的返回值
                j = list(set(l))
            except socket.error:
                break
        try:
            return j
        except:
            return 0

class Update():
        
    def update(self,target_ip,camType,fileName):
        username = 'root'  
        password = 'iBabyVP8019'  
        finish = '#'  
#         filename = self.GetFileName(camType)
        print "my file name = ",fileName
        print type(fileName)

        try:
            tn = telnetlib.Telnet(target_ip,port = 23,timeout = 5)
        except:
            return 0
      
        if camType == 0:
            tn.read_until('iBaby login: ')
        elif camType == 1 or camType == 2 or camType == 3:
            tn.read_until('GM login: ') 
             
        tn.write(username + '\n')  
        tn.read_until('Password: ')  
        tn.write(password + '\n')
        tn.read_until(finish) 
        tn.write('tftp -g -l /tmp/kenny.sh -r kenny.sh %s;/bin/sh /tmp/kenny.sh  %s  %s\n'%(host_ip,str(fileName),host_ip))
        tn.read_until("$")
        tn.close()
    def GetFileName(self,camType):
        if camType == 0:
            files = os.listdir('./updatePackage_m6')
        elif camType == 1:
            files = os.listdir('./updatePackage_h1')
        elif camType == 2:
            files = os.listdir('./updatePackage_m6s')
        elif camType == 3:
            files = os.listdir('./updatePackage_a1')
        filename = files[0]
        print "filename = ",filename

        return filename
    
class CheckVerison():
    def checkVersion(self,target_ip,camType):

        username = 'root'  
        password = 'iBabyVP8019'  
        finish = '#'
        try:
            tn = telnetlib.Telnet(target_ip,port = 23,)
        except:
            return 0
        
        if camType == 0:
            tn.read_until('iBaby login: ')
        elif camType == 1 or camType == 2 or camType == 3:
            tn.read_until('GM login: ')   
            
        tn.write(username + '\n')  
        tn.read_until('Password: ')  
        tn.write(password + '\n')      
        tn.read_until(finish)
        tn.write('cat /mnt/mtd/firmware_version\n')
        version =  tn.read_until(finish).splitlines()[1]
        return target_ip,version
    
if __name__ == "__main__":
    # test = searchCamera()
    print 'main'
