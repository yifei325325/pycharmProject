#!/usr/bin/python
#coding:utf8
'''
Created on 2016年6月30日

@author: Kenny
'''
import socket,struct,time

def convertData():
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
    """
    //协议头文件.
    typedef struct MJPEG_MessageHeader
    {
        unsigned char           messageHeader[4];    //协议头  摄像头操作协议: "MO_O" 摄像头传输协议 "MO_V"  搜索协议头： MO_I
        short                   controlMask;         //操作码，区分同一协议中不同命令.
        unsigned char           reserved0;            //保留，默认=0;
        unsigned char           reserved1[8];           //保留
        int                     commandLength;        //命令中正文的长度
        int                     reserved2;            //保留
        
    }MJPEG_MsgHeader;

    
    //网络连接信息结构体
    typedef struct NetConnectInfomation
    {
        char server_ip[64];   //camIP
        int  port;            //端口
        char user_name[13];      //用户名
        char pass_word[13];      //密码
    
    }MJPEG_NetConnectInfo;

    
    //登陆响应结构体
    typedef struct LoginRequestReply
    {
    
        MJPEG_MsgHeader msgHeader;
        short           result;   //返回 0 OK,2 已经达到最大连接许可，连接将断开.
        unsigned char   devID[13];  //返回设备id.
        unsigned char   reserved0[4];  //保留
        unsigned char   reserved1[4];  //保留
        unsigned char   devVersion[4];  //摄像头系统固件版本.
        
    }MJPEG_LoginRequestReply;

    """
    """
    //较验请求正文结构体
    typedef struct VerifyRequestCommContent
    {
        //协议正文
        MJPEG_MsgHeader msgHeader;
        unsigned char   userName[13];      //用户名
        unsigned char   password[13];      //密码
        
    }MJPEG_VerifyRequestCommContent;



    //较验响应结构体
    typedef struct verifyRequestReply
    {
        MJPEG_MsgHeader msgHeader;
        short           result; //0 较验正确 1 用户名出错 2 密码出错.
        char            reserved;    //保留
    
        
    }MJPEG_VerifyRequestReply;
    
    //温湿度
    typedef struct temperaterHumlityRequest
    {
        MJPEG_MsgHeader msgHeader;
        char            reserved;
    }MJPEG_temperaterHumlityRequest;
    
    typedef struct temperaterHumlityReply
    {
        double            temperature;
        double            wetness;
    }MJPEG_temperaterHumlityReply;


    """
    
    hostip = "10.0.1.18"
    port = 80
    data1 = struct.pack("4shc8siih13s4s4s4s","MO-O",0," "," ",0,0,0," "," "," "," ")#LoginRequestReply#登录响应结构体
    data2 = struct.pack("4shc8siic","MO-O",32," "," ",0,0," ")#请求温湿度
    #allData = [data1,data2]
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ifcontinue = True
    while ifcontinue:
        data = data1
        s.connect((hostip,port))
        while True:
            s.sendall(data) 
            r1 = s.recv(23)
            if r1 == 0:
                print "r1 = ",r1
                data = data2
                break
            elif r1 == 2:
                s.close()
                ifcontinue = False
            
            #else:
                

convertData()
print "end"