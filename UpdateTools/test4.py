# coding:utf8
import struct
import socket
import time
import logging
import binascii

logging.basicConfig(level=logging.INFO)

BC_PORT = 3759

CT_NONE = 0
CT_H1 = 1
CT_H1N = 2
CT_M6S = 3
CT_AIR = 4
CT_M2PRO = 5
CT_M6TT = 6

D = {0:'NONE',
     1:'H1',
     2:'H1N',
     3:'M6S',
     4:'AIR',
     5:'M2PRO',
     6:'M6TT'
}
R = {0:"Unregistered",
     1:"Registered"
}

class searchCamera(object):
    """
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
    """
    def __init__(self):
        self.bc_name = 'iBaby'
        self.command = 1
        self.camid = ' '
        self.ip = ' '
        self.port = 0
        self.mac = ' '
        self.version = ' '
        self.state = 0
        self.p2pType = 0
        self.camType = ' '
        self.reserve = ' '
        self.checksum = 0
        #将要广播的字符串（broadcastString），转化成网络传输的字节码
        self.broadcastString = struct.pack('20si20s20si20s20siic11si', self.bc_name, self.command,
                                           self.camid, self.ip, self.port,
                                           self.mac, self.version,self.state,
                                           self.p2pType,self.camType,self.reserve,self.checksum)

    #广播字节码并接收回应
    def getIp(self, values):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # 重复发送5次广播包，每次间隔0.1秒，接收时不停的循环接收，提高搜索成功率
        for i in xrange(7):  # @UnusedVariable
            s.sendto(values, ('<broadcast>', BC_PORT))  # BC_PORT=3759是端口号，要和固件方对应
            time.sleep(0.1)
        s.setblocking(0)  # 设置为非阻塞模式
        # 定义一个空列表，用来接收camID和IP
        l = []
        while True:
            try:
                sock, addr = s.recvfrom(1024)

                reply = struct.unpack('@20si20s20si20s20siic11si', sock)
                # print reply
                l.append(reply)
                # print l
                #列表去重，因为有多次搜索，可能会有很多重复的返回值
                j = list(set(l))
                # print j
            except socket.error:
                break
        try:
            return j
        except:
            return 0

# s = searchCamera()
# lis = s.getIp(s.broadcastString)
# print lis
# for j in xrange(len(lis)):
#     bc_name = lis[j][0]
#     command = lis[j][1]
#     camid = lis[j][2]
#     ip = lis[j][3]
#     port = lis[j][4]
#     mac = lis[j][5]
#     version = lis[j][6]
#     state = lis[j][7]
#     p2pType = lis[j][8]
#     camType = lis[j][9]
#     reserve = lis[j][10]
#     checksum = lis[j][11]
#     # print "bc_name = ",bc_name
#     # print "command = ",command
#     print "camid = ",camid
#     print "ip = ",ip
#     # print "port = ",port
#     print "mac = ",mac
#     print "version = ",version
#     print "state = ",state
#     print "p2pType = ",p2pType
#     print "camType = ",D[int(binascii.b2a_hex(camType),base=16)]
#     print "reserve = ",reserve
#     print "checksum = ",checksum
#
#
#             # print "camType = ", D[int(binascii.b2a_hex(lis[j][i]),base=16)]
