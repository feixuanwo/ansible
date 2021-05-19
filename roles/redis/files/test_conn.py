#!/usr/bin/python
import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((sys.argv[1], int(sys.argv[2])))
if result == 0:
   print("host:%s, redis_port:%s is UP" % (sys.argv[1], sys.argv[2]))
else:
   print "Not OK"
   print("host:%s, redis_port:%s is NOT UP" % (sys.argv[1], sys.argv[2]))
