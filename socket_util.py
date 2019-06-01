#!/usr/bin/env python
# -*- coding: utf-8 -*-

from config import *
import json

#修改 处理半包占包问题，协议修改
def read_data_from_socket(socket):
    #方式2：长度+数据
    data_len = int(socket.recv(BUFSIZE))
    left_len = data_len
    res = ''

    while left_len != 0:
        if left_len < BUFSIZE:
            data = socket.recv(left_len)
        else:
            data = socket.recv(BUFSIZE)

        left_len -= len(data)
        res += data

    return res

def read_data_from_socket_origin(socket):
    res = socket.recv(BUFSIZE)
    if(res):
        reslist = res.split('|')
        res = reslist[1]
    return res



def send_data_to_client(diction_data_tosend,clientsocket):
    data = json.dumps(diction_data_tosend)
    data = diction_data_tosend['protoName'] +'|'+data
    print data
    clientsocket.send(data)

