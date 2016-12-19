# coding:utf8

import sys
import telnetlib
import socket

local_ip = socket.gethostbyname(socket.gethostname())

def update(ip,local_ip):
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
    # tn.write("echo \"test\"\n")
    tn.write('cd /mnt/mtd/update/file;tftp -gr ipcam_flash -l ipcam %s;chmod 777 ipcam;reboot\n'%local_ip)
    print tn.read_until(finish)
    tn.close()

update(sys.argv[1],local_ip)
print 'the device ip = %s has been updated'%sys.argv[1]










