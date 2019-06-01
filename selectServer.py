#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time
import socket
import select
import logging
import Queue
import socket_util
import json

from config import *
from handler.dispatchHandler import DispatchHandler


class GameServer(object):

    #服务器类
    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setblocking(False)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #keepalive
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #端口复用
        self.server.bind((host, port))
        self.inputs = [] #select 接收文件描述符列表
        self.outputs = [] #输出文件描述符列表
        self.client_info = {}
        self.message_queues = {}  # 消息队列,发送给客户端的消息会先保存在这里


    #启动服务器
    def start(self):
        self.server.listen(MAX_SOCKET_CONNECTION)
        self.inputs.append(self.server)
        print('waiting for connection...')
        while True:
            readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs, g_select_timeout)
            if not (readable or writable or exceptional) :
                continue
            #服务端接收消息
            for s in readable:
                if s is self.server:#服务器接收到客户端连接请求
                    client_socket, client_address = s.accept()
                    #print "connection", connection
                    print "%s connect." % str(client_address)
                    client_socket.setblocking(0) #非阻塞
                    self.inputs.append(client_socket) #客户端添加到inputs
                    self.client_info[client_socket] = str(client_address)
                    self.message_queues[client_socket] = Queue.Queue()  #每个客户端一个消息队列
                else:#接收客户端的数据
                    data = socket_util.read_data_from_socket_origin(s)
                    if data:
                        #处理消息
                        #self.message_queues[s].put(data)  # 队列添加消息
                        self.process_request(s,data)
                    else:  # 客户端断开
                        # Interpret empty result as closed connection
                        print "Client:%s Close." % str(self.client_info[s])
                        if s in self.outputs:
                            self.outputs.remove(s)
                        self.inputs.remove(s)
                        s.close()
                        del self.message_queues[s]
                        del self.client_info[s]

            #服务端发送消息
            for s in writable:
                pass

            for s in exceptional:
                logging.error("Client:%s Close Error." % str(self.client_info[s]))
                if s in self.inputs:
                    self.inputs.remove(s)
                    s.close()
                if s in self.outputs:
                    self.outputs.remove(s)
                if s in self.message_queues:
                    del self.message_queues[s]
                del self.client_info[s]


    #以后增加多线程处理
    def process_request(self, client,socketdata):
        try:
            DispatchHandler.dispatch(json.loads(socketdata), client)
        except Exception, e:
            logging.error(e)

