# coding:utf8

import sys
import telnetlib
import socket
import os

local_ip = socket.gethostbyname(socket.gethostname())
os.startfile(os.getcwd()+'/tftpd32/tftpd32.exe')

def update(ip):
    username = "root"
    password = "iBabyVP8019"
    finish = "#"
    try:
        tn = telnetlib.Telnet(ip,port=23,)
    except BaseException,error:
        print 'error: \t%s'%error
        return 0
    tn.read_until('GM login: ')
    tn.write(username + '\n')
    tn.read_until('Password: ')
    tn.write(password + '\n')
    tn.read_until(finish)
    print "updateing ...... please wait......"
    tn.write('cd /mnt/mtd/update/file;tftp -gr %s -l ipcam %s;chmod 777 ipcam;echo 1 > /mnt/mtd1/workstate;reboot\n'%(sys.argv[2],local_ip))
    tn.read_until(finish)
    tn.close()

if update(sys.argv[1]) == 0:
    print "check you device connection!!!" 
else:
    print "the device is rebooting......"
    print 'the device ip = %s has been updated'%sys.argv[1]










