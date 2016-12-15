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


//iON 开关
typedef struct iONCtrlRequestCommand
{
    MJPEG_MsgHeader msgHeader;
    int ion_stast;// 1:开2:关
}MJPEG_iONCtrlRequestCommand;

typedef struct iONCtrlRequestCommandReply
{
    short result;
}MJPEG_iONCtrlRequestCommandReply;


//LED 开关
typedef struct lEDCtrlRequestCommand
{
    MJPEG_MsgHeader msgHeader;
    int led_stast;// 1:开2:关
}MJPEG_lEDCtrlRequestCommand;

typedef struct lEDCtrlRequestCommandReply
{
    short result;
}MJPEG_lEDCtrlRequestCommandReply;

//空气质量
typedef struct airQualityRequestCommand
{
    MJPEG_MsgHeader msgHeader;
    char reserved;
}MJPEG_airQualityRequestCommand;

typedef struct airQualityRequestCommandReply
{
    int airQualityLevel;//1234
}MJPEG_airQualityRequestCommandReply;
