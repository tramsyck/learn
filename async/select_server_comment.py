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
# 端口复用
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('', 10000))
server.listen(5)
# 把服务器套接字放入输入套接字组，用于检查读
inputs = [server]

while True:
#select()方法接收并监控3个通信列表， 第一个是所有的输入的data,就是指外部发过来的数据，第2个是监控和接收所有要发出去的data(outgoing data),第3个监控错误信息，接下来我们需要创建2个列表来包含输入和输出信息来传给select().
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
