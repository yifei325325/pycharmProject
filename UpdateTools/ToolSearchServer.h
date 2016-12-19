

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
//�û���½���ص����� iParam1
#define VS_O_USERERROR  		1    	//�û�������
#define VS_O_PASSERROR  		2    	//�������
#define VS_O_LEVELERROR  		3   	//�û�������� 
#define L_LOGIN_RETURNFAILURE 4  	//��������  
#define L_LOGIN_RETURNADMIN  5  		//�����û�
#define L_LOGIN_RETURNGEN  	6     	//��ͨ�û�
#define L_LOGIN_RETURNSUP 	7     	// �����û�
#define L_SETIP_SUCCEED  	8    	//��������ɹ�
#define L_SETIP_FIELD 		9     	// ��������ʧ��

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
   	int scanPort;            //   ɨ��˿�
   	int serverUPdata;         //  �����˿�
   	int conPort    ;        //   ���ƶ˿�
   	int dataPort;            //   ���ݶ˿�
   	int	videocPort;			//��Ƶ���ƶ˿�
	int	reserver  ;          //   ����
 
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
  BYTE1   dir:1;      /*ͨ��״̬ REQUEST(0)  REPLY(1)Ӧ��*/
  BYTE1   result;   /*ͨ�Ž�� VS_O_OK��1��--- �ɹ��� VS_O_FR��0�� ---- ����ʧ��*/
  LONG1   lChannel ;  /*ͨ����ţ����Ҫ���õĲ�����ͨ��û�й�ϵ����Ϊ0*/
  LONG1   lPacketLen; /*���ư��ĳ��ȣ�����ͷ���ĳ���*/ 
  BYTE1   username[16] ;
  BYTE1   userpass[16];
  BYTE1   reset[16];
}VS_C_PACKET0, *LPVS_C_PACKET0; 



typedef struct channelinfo  /*ͨ����Ϣ*/
{
	BYTE1 nChannelno;     /*ͨ����*/
       BYTE1 reset;

	BYTE1 Channelname[100];      /*ͨ������*/
}VS_CHANNELCFG,*LPVS_VS_CHANNELCFG;


typedef struct setnetinfo
{ 
	char		sDVRtype[16];/*�豸�ͺ�*/ 
	char		sDVR[256];/*�豸����*/
	char		sDVRNumChl;/*ͨ����*/
	char		sDVRMAC[20];/*�����ַ*/
	char	 	sDVRIP[32]; /* DVR IP��ַ */ 
	char 	sDVRIPMask[32]; /* DVR IP��ַ���� */ 
	char 	sGatewayIP[32]; /* ���ص�ַ */ 
	char 	sDns[32]; /* DNS��ַ */ 
	int  		sWebPort;/*Web�˿�*/
	int		onvifPort;/*ɨ��˿�*/
	int		rtspPort;/*���ƶ˿�*/
	int		dataPort;/*���ݶ�*/
 	char 	softwareVersion[32];/*����������汾��*/
	char 	hardwareVersion[32];/*�ͻ�������汾��*/
	char 	username[32];
	unsigned char 	pwd_pkt_md5[16];
	unsigned char		conn_mod;	/*0-static ip 1-DHCP 2-pppoe*/
}VS_NETCFG, *LPHY_VS_NETCFG; 

#define MAXTRANFILEDATALEN  1024 
 
//�ļ��������Э��
typedef struct  FILECONTROL
{
    BYTE1    control;               //0  delete // 1  ��ѯ 
    BYTE1    reserv[3] ;           //
    WORD1		numbers;            // �ܹ��ļ��Ĵ�С
    WORD1		receivelen;         //  �Ѿ����յĳ���
    WORD1		thislen;                // ���η��͵�����
    BYTE1    filedata[MAXTRANFILEDATALEN]  ;         // ÿ��1024 �ֽ� 
}VS_FILE_CONTROL,* LPVS_FILE_CONTROL;   

//�ļ��������Э��
//#define L_DVS_NFSSET 133   // ����NFS  ������


#pragma pack(1)


//ibaby************************************************
typedef struct searchBrodcastHeader
{
    char            protocolHeader[4];   //Э��ͷ
    short           controlMask;         //������
    char            reserved;            //����
    char            reserved2[8];        //����
    int             contentLength;       //���ĳ���
    int             reserved3;           //����
    
}IB_searchBrodcastHeader;

typedef struct searchCommandContentReply
{
    IB_searchBrodcastHeader  header; //ͷ��
    char            camID[13];          //����ͷID
    char            camName[21];        //����ͷ����
    unsigned int    ip;                 //IP; ���
    unsigned int    netMask;            //����  ���
    unsigned int    getwayIP;           //����IP;  ���
    unsigned int    DNS;                //DNS;  ���
    char			p2pType;			// 0:TUTK 1:SY P2P
    char            reserved[3];        //����
    char            sysVersion[4];      //ϵͳ�汾   �̼��汾 = sysVersion[0].sysVersion[1].sysVersion[2]
    char            appVersion[4];       //App software �汾  appVersion[0]����ͷ����
    unsigned short  port;               //�˿� ���
    char            dhcpEnabled;        //DHCP״̬
}IB_searchCommandContentReply;
#pragma pack()


//�㲥���������
#define CONTROLLCODE_SEARCH_BROADCAST_REQUEST   0 
//�㲥��Ӧ������
#define CONTROLLCODE_SEARCH_BROADCAST_REPLY     1


//ibaby************************************************
#include "CheckSum.h"
//������Ϣ
typedef struct tag_remote_equinfo
{
    char  	sSerialNumber[16];/*���к�*/
    char 	softwareVersion[32];/*����汾�Ű汾��*/
    char 	hardwareVersion[32];/*Ӳ���汾�Ű汾��*/
    char 	camDesc[24];/*���������*/
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
	int 	onvif_port;					/*onvifͨѶ�˿�*/
	int 	rtsp_port;					/*RTSPͨѶ�˿�*/
	BYTE	conn_mod;					/*0-��̬��ַ 1-DHCP 2-pppoe*/
	char 	ipcamIP[16]; 				/* ipcam IP��ַ */ 
	char 	ipcamIPMask[16]; 			/* ipcam IP��ַ���� */ 
	char 	ipcamGatewayIP[16]; 		/* ���ص�ַ */ 
	char 	byMACAddr[MACADDR_LEN]; 	/* ֻ�����������������ַ */ 
	char 	byDnsaddr[2][16]; 			/* DNS��ַ */ 
	BYTE 	dwPPPOE; 					/* 0-������,1-���� */ 
	char 	sPPPoEUser[NAME_LEN]; 		/* PPPoE�û��� */ 
	char 	sPPPoEPassword[PASSWD_LEN];	/* PPPoE���� */ 
	char 	sPPPoEIP[16]; 				//PPPoE IP��ַ(ֻ��)
	BYTE	ddns_enable;				/*0-�ر� 1-����*/
	char 	ddnsaddress[58]; 			/* ddns������ */ 
	char 	ddnsUser[NAME_LEN]; 		/* ddns�û��� */ 
	char 	ddnsPassword[PASSWD_LEN];	/* ddns���� */ 
	BYTE 	ddns_service;              /*ddns��������  0-FACTORY 1-3322 2-9229 */
	char 	mddnsaddress[58]; 			/* ����ddns������ */ 
	char 	mddnsUser[NAME_LEN]; 		/* ����ddns�û��� */ 
	char 	mddnsPassword[PASSWD_LEN];	/* ����ddns���� */ 
}REMOTE_NETCFG; 


extern	int BroadcastSendService();

#endif
