#!/usr/bin/env python
# -*- coding: utf-8 -*-
from  basicService import *
import dao.DBsearch
from config import *
import socket_util

#登录请求处理
class LoginService(BaseService):
    def handle_request(self, json_obj, client):
        res = dao.DBsearch.searchUserIDandPassword(json_obj['userName'],json_obj['password'])
        datatosend = {}
        datatosend['protoName'] = 'LoginResponse'
        if res == PASSWORD_CORRECT:
            datatosend['ResponseMsg'] = PASSWORD_CORRECT
        elif res==PASSWORD_ERROR:
            datatosend['ResponseMsg'] = PASSWORD_ERROR
        else:
            datatosend['ResponseMsg'] = USER_ID_ERROR
        socket_util.send_data_to_client(datatosend,client)
