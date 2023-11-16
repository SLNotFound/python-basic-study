#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time     : 2023/11/16 11:32
# @Author   : SLNotFound
# @File     : tsTserv.py

from socket import *
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connection...")
    tcpCliSock, addr = tcpSerSock.accept()
    print("...connected from:", addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(data)

    tcpCliSock.close()

tcpSerSock.close()
