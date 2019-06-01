#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
项目配置常量
'''

#服务器相关配置
HOST = '127.0.0.1'
PORT = 6666
POOLSIZE = 10
BUFSIZE = 1024
MAX_SOCKET_CONNECTION = 30
TIMEOUT = 2
g_select_timeout = 10



#协议名称
LOGIN_PROTO = "LoginProto"

#常量
PASSWORD_CORRECT = "PASSWORD_CORRECT"
PASSWORD_ERROR = "PASSWORD_ERROR"
USER_ID_ERROR = "USER_ID_ERROR"