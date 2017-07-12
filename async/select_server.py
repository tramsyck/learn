#!/usr/bin/env python
#coding=utf8

##########################
# select 服务器
# Date 2017-7-10
##########################
#


import socket
import select

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', 10000))
server.listen(5)
inputs = [server]

while True:
    rs, ws, es = select.select(inputs, [], [], 1)
    for r in rs:
        if r is server:
            clientsock, clientaddr = r.accept()
            inputs.append(clientsock)
        else:
            data = r.recv(1024);
            if not data:
                inputs.remove(r)
            else:
                print data
