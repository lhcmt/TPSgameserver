#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from config import *
from services.loginService import *

#任务分发处理器
class DispatchHandler(object):

    login_service = LoginService()

    @staticmethod
    def dispatch(json_obj, client):
        #请求类型
        request_type = DispatchHandler._parse_request_type(json_obj)
        service = DispatchHandler._get_matched_service(request_type)
        if service != None:
            service.handle_request(json_obj, client)
        else:
            logging.error(('can not find matched service with request type: %d' % request_type))

    #获取对应的协议名
    @staticmethod
    def _parse_request_type(json_obj):
        return json_obj['protoName']

    #根据请求类型获取到相应的service类对象
    #param request_type: 请求类型
    @staticmethod
    def _get_matched_service(request_type):

        service = None
        if request_type == LOGIN_PROTO:
            service = DispatchHandler.login_service
        elif request_type == 2:
            pass
        else:
            pass

        return service