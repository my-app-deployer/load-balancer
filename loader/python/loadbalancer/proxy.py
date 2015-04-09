#!/usr/bin/env python 

# This is a simple port-forward / proxy, written using only the default python
# library. If you want to make a suggestion or fix something you can contact-me
# at voorloop_at_gmail.com
# Distributed over IDC(I Don't Care) license
import socket
import select
import time
import sys
from deamon import Deamon
from pymongo import MongoClient
# Changing the buffer_size and delay, you can improve the speed and bandwidth.
# But when buffer get to high or delay go too down, you can broke things
buffer_size = 4096
delay = 0.0001
forward_to = ('localhost', 80)

# the Forwarder of the connection
class Forward:
    def __init__(self):
        self.forward = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a new socket to talk to the remote server
        self.mongo = MongoClient('mongodb://localhost:27017/')
        self.db=self.mongo.servers

    def start(self, host, port):
        try:
            self.forward.connect((host, port)) #connects to remote
            return self.forward
        except Exception, e:
            print e
            return False
    #returns the server on which the proxy must forward
    def getServer(self,type,domaine,load=75):
        server=self.db.type.find_one({"domaine":domaine,"load":load}) #gets a server by domaine and workload less than 75%
# a proxy deamon
class Proxy(Deamon):
    input_list = []
    channel = {}

    def __init__(self, host, port):
        self.max_connection=200
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((host, port))
        self.server.listen(self.max_connection)
        self.attributes={
            server:self.server
            ,running:True
            ,delay:0.0001 #delay between requests are treated, clock speed kinda
            ,buffer:4096 #buffer for the socket size
        }
        
    def set(self,key,value):
        self.attributes[key]=value
    def get(self,key):
        return self.attributes[key]
    def select(self,rlist, wlist, xlist, Timout=null):
        return select.select(rlist,wlist,xlist,Timout)


    def main_loop(self):
        self.input_list.append(self.server)
        while self.running:
            time.sleep(delay)
            inputready, outputready, exceptready = self.select(self.input_list, [], [])
            for self.s in inputready:
                if self.s == self.server:
                    self.on_accept()#accepts the socket connection if we are looping on the proxy
                    break
                #otherwise it is a client connection, 
                self.data = self.s.recv(buffer_size)
                if len(self.data) == 0: #if we donnot have data, close the connections
                    self.on_close()
                    break
                else: #otherwise send buffered data to client
                    self.on_recv()

    def on_accept(self):
        forward = Forward().start(forward_to[0], forward_to[1])
        clientsock, clientaddr = self.server.accept()
        if forward:
            print clientaddr, "has connected"
            self.input_list.append(clientsock)
            self.input_list.append(forward)
            self.channel[clientsock] = forward
            self.channel[forward] = clientsock
        else:
            print "Can't establish connection with remote server.",
            print "Closing connection with client side", clientaddr
            clientsock.close()

    def on_close(self):
        print self.s.getpeername(), "has disconnected"
        #remove objects from input_list
        self.input_list.remove(self.s)
        self.input_list.remove(self.channel[self.s])
        out = self.channel[self.s]
        # close the connection with client
        self.channel[out].close()  # equivalent to do self.s.close()
        # close the connection with remote server
        self.channel[self.s].close()
        # delete both objects from channel dict
        del self.channel[out]
        del self.channel[self.s]

    def on_recv(self):
        data = self.data
        # here we can parse and/or modify the data before send forward
        print data
        self.channel[self.s].send(data)
    def run(self):
      self.main_loop()

if __name__ == '__main__':
        server = Proxy(host='',port= 9000)
        try:
            server.main_loop()
        except KeyboardInterrupt:
            print "Ctrl C - Stopping server"
            sys.exit(1)
