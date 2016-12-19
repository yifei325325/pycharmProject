

#ifndef L_H_MANAGER_H
#define L_H_MANAGER_H


#define	L_DVS_GET_IP 10
#define	L_DVS_GET_IP_RPLY 11
#define	L_DVS_SET_IP	12
#define	L_DVS_SET_IP_RPLY	13
//#define	L_DVS_SET_NETCFG	11
//#define	L_DVS_GET_NETCFG	12
#define	L_DVS_SEND_FILE	12
#define	L_DVS_SEND_FILE_RPLY	12


//#define DVR_NET_COMMAND_GET_NETINFO	125
//#define DVR_NET_COMMAND_GET_NETINFO_RPLY	126



#define IPCAM_NET_COMMAND_GET_NETINFO			200
#define IPCAM_NET_COMMAND_GET_NETINFO_RPLY		201
#define IPCAM_NET_COMMAND_SET_NETINFO        	202
#define IPCAM_NET_COMMAND_SET_NETINFO_RPLY      203
////
//用户登陆返回的数字 iParam1
#define VS_O_USERERROR  		1    	//用户名错误
#define VS_O_PASSERROR  		2    	//密码错误
#define VS_O_LEVELERROR  		3   	//用户级别错误 
#define L_LOGIN_RETURNFAILURE 4  	//其他错误  
#define L_LOGIN_RETURNADMIN  5  		//管理用户
#define L_LOGIN_RETURNGEN  	6     	//普通用户
#define L_LOGIN_RETURNSUP 	7     	// 超级用户
#define L_SETIP_SUCCEED  	8    	//更改密码成功
#define L_SETIP_FIELD 		9     	// 更改密码失败

#define MAXLOGINNAME 16
#define MAXLOGINPASS 16
////
typedef unsigned char 	BYTE1;
typedef long  					LONG1;
typedef short 					SHORT1;
typedef unsigned short 	WORD1;

////WORD1 g_webport =80;


////int 		L_byLinkMode = 0;
 typedef struct portinfo
{
	int	visitport;
   	int scanPort;            //   扫描端口
   	int serverUPdata;         //  升级端口
   	int conPort    ;        //   控制端口
   	int dataPort;            //   数据端口
   	int	videocPort;			//视频控制端口
	int	reserver  ;          //   保留
 
}VS_PORTINFO,*LPVS_PORTINFO;

 typedef struct VS_CONTROL_PACKET 
{
	unsigned long iCmdType;
	unsigned long iDataLen;
	unsigned long ulTimeSecond;
	unsigned long ulTimeMicrosecond;
	unsigned long iParam1;
	unsigned long iParam2;//timesnamp
	unsigned long iParam3;
	unsigned long iFlag1;
	unsigned long iFlag2;
	unsigned char cData[256];//mac
	
}VS_C_PACKET, *LPVS_C_PACKET; 
 
typedef struct VS_CONTROL_PACKET0
{ 
  BYTE1   bytCommand;
  BYTE1   dir:1;      /*通信状态 REQUEST(0)  REPLY(1)应答*/
  BYTE1   result;   /*通信结果 VS_O_OK（1）--- 成功， VS_O_FR（0） ---- 操作失败*/
  LONG1   lChannel ;  /*通道编号，如果要设置的参数跟通道没有关系，设为0*/
  LONG1   lPacketLen; /*控制包的长度，包含头部的长度*/ 
  BYTE1   username[16] ;
  BYTE1   userpass[16];
  BYTE1   reset[16];
}VS_C_PACKET0, *LPVS_C_PACKET0; 



typedef struct channelinfo  /*通道信息*/
{
	BYTE1 nChannelno;     /*通道号*/
       BYTE1 reset;

	BYTE1 Channelname[100];      /*通道名称*/
}VS_CHANNELCFG,*LPVS_VS_CHANNELCFG;


typedef struct setnetinfo
{ 
	char		sDVRtype[16];/*设备型号*/ 
	char		sDVR[256];/*设备名称*/
	char		sDVRNumChl;/*通道数*/
	char		sDVRMAC[20];/*物理地址*/
	char	 	sDVRIP[32]; /* DVR IP地址 */ 
	char 	sDVRIPMask[32]; /* DVR IP地址掩码 */ 
	char 	sGatewayIP[32]; /* 网关地址 */ 
	char 	sDns[32]; /* DNS地址 */ 
	int  		sWebPort;/*Web端口*/
	int		onvifPort;/*扫描端口*/
	int		rtspPort;/*控制端口*/
	int		dataPort;/*数据端*/
 	char 	softwareVersion[32];/*主机端软件版本号*/
	char 	hardwareVersion[32];/*客户端软件版本号*/
	char 	username[32];
	unsigned char 	pwd_pkt_md5[16];
	unsigned char		conn_mod;	/*0-static ip 1-DHCP 2-pppoe*/
}VS_NETCFG, *LPHY_VS_NETCFG; 

#define MAXTRANFILEDATALEN  1024 
 
//文件传输控制协议
typedef struct  FILECONTROL
{
    BYTE1    control;               //0  delete // 1  查询 
    BYTE1    reserv[3] ;           //
    WORD1		numbers;            // 总共文件的大小
    WORD1		receivelen;         //  已经接收的长度
    WORD1		thislen;                // 本次发送的字数
    BYTE1    filedata[MAXTRANFILEDATALEN]  ;         // 每次1024 字节 
}VS_FILE_CONTROL,* LPVS_FILE_CONTROL;   

//文件传输控制协议
//#define L_DVS_NFSSET 133   // 设置NFS  服务器


#pragma pack(1)


//ibaby************************************************
typedef struct searchBrodcastHeader
{
    char            protocolHeader[4];   //协议头
    short           controlMask;         //操作码
    char            reserved;            //保留
    char            reserved2[8];        //保留
    int             contentLength;       //正文长度
    int             reserved3;           //保留
    
}IB_searchBrodcastHeader;

typedef struct searchCommandContentReply
{
    IB_searchBrodcastHeader  header; //头部
    char            camID[13];          //摄像头ID
    char            camName[21];        //摄像头名称
    unsigned int    ip;                 //IP; 大端
    unsigned int    netMask;            //掩码  大端
    unsigned int    getwayIP;           //网关IP;  大端
    unsigned int    DNS;                //DNS;  大端
    char			p2pType;			// 0:TUTK 1:SY P2P
    char            reserved[3];        //保留
    char            sysVersion[4];      //系统版本   固件版本 = sysVersion[0].sysVersion[1].sysVersion[2]
    char            appVersion[4];       //App software 版本  appVersion[0]摄像头类型
    unsigned short  port;               //端口 大端
    char            dhcpEnabled;        //DHCP状态
}IB_searchCommandContentReply;
#pragma pack()


//广播请求操作码
#define CONTROLLCODE_SEARCH_BROADCAST_REQUEST   0 
//广播回应操作码
#define CONTROLLCODE_SEARCH_BROADCAST_REPLY     1


//ibaby************************************************
#include "CheckSum.h"
//主机信息
typedef struct tag_remote_equinfo
{
    char  	sSerialNumber[16];/*序列号*/
    char 	softwareVersion[32];/*软件版本号版本号*/
    char 	hardwareVersion[32];/*硬件版本号版本号*/
    char 	camDesc[24];/*摄像机描述*/
    char 	serverName[24]; 
    char 	serverIP[16];
	BYTE	upnp_status;
	BYTE	ddns_status;
	char 	ddnsaddress[58];
	int		infrared_led_stat;
	char 	reserve[60]; 
	
}REMOTE_EQUINFO;
#define MACADDR_LEN 	20  
#define NAME_LEN      	32
#define PASSWD_LEN 		16

typedef struct tag_remote_netcfg
{ 
	int 	web_port;
	int 	video_port;
	int 	onvif_port;					/*onvif通讯端口*/
	int 	rtsp_port;					/*RTSP通讯端口*/
	BYTE	conn_mod;					/*0-静态地址 1-DHCP 2-pppoe*/
	char 	ipcamIP[16]; 				/* ipcam IP地址 */ 
	char 	ipcamIPMask[16]; 			/* ipcam IP地址掩码 */ 
	char 	ipcamGatewayIP[16]; 		/* 网关地址 */ 
	char 	byMACAddr[MACADDR_LEN]; 	/* 只读：服务器的物理地址 */ 
	char 	byDnsaddr[2][16]; 			/* DNS地址 */ 
	BYTE 	dwPPPOE; 					/* 0-不启用,1-启用 */ 
	char 	sPPPoEUser[NAME_LEN]; 		/* PPPoE用户名 */ 
	char 	sPPPoEPassword[PASSWD_LEN];	/* PPPoE密码 */ 
	char 	sPPPoEIP[16]; 				//PPPoE IP地址(只读)
	BYTE	ddns_enable;				/*0-关闭 1-开启*/
	char 	ddnsaddress[58]; 			/* ddns主机名 */ 
	char 	ddnsUser[NAME_LEN]; 		/* ddns用户名 */ 
	char 	ddnsPassword[PASSWD_LEN];	/* ddns密码 */ 
	BYTE 	ddns_service;              /*ddns服务类型  0-FACTORY 1-3322 2-9229 */
	char 	mddnsaddress[58]; 			/* 厂家ddns主机名 */ 
	char 	mddnsUser[NAME_LEN]; 		/* 厂家ddns用户名 */ 
	char 	mddnsPassword[PASSWD_LEN];	/* 厂家ddns密码 */ 
}REMOTE_NETCFG; 


extern	int BroadcastSendService();

#endif
