# coding:utf8

import telnetlib


tn = telnetlib.Telnet("10.0.1.41",port=23)
print tn.read_all()

tn.read_until("GM login:")
tn.write("root\n")
print tn.read_all()
print "test git"